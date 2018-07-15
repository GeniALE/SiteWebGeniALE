# -*- coding: utf-8 -*-
import django
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from teamModule.models import Formation, Team, Member, ProjectStatus, TeamRole, MemberExtraInfoType, MemberExtraInfo, \
    Project

"""
 Constants
"""

MEMBERS_SHEET_ID = "1Lo34vLrDqczYRnhawPR35zxOjc75Tcf2BK_IuRBA6qg"
PROJECTS_SHEET_ID = "1Rw4HHv-zZ4ewJylfefShKSnjDZZ582cgCvvKZWGhGh0"

# Member sheet binding
"""
If you ever change the excel sheets, you need to change those bindings
"""
M_FULLNAME = "Prénom,Nom"
M_PERMANENT_CODE = "Code permanent"
M_UNIVERSAL_CODE = "Code d'accès universel"
M_ROLE = "Rôle"
M_PROG = "Prog."
M_TEAM = "Équipe"
M_STUDIES_LEVEL = "Niveau"
M_IN_STAGE = "Stage"
M_EMAIL = "Courriel"
M_PHONE = "# Téléphone"
M_PICTURE = "Photo"
M_STOP_LINE = "Veuillez mettre ci-dessous les étudiants ne faisant plus partie du club."

# Project sheet binding
P_MEMBER = "Membre / Projet"
P_TEAM_LEAD = "Chargé"

"""
Utility functions
"""


def add_extra_type(extra_type):
    try:
        return MemberExtraInfoType.objects.filter(description=extra_type).get()
    except MemberExtraInfoType.DoesNotExist:
        new_extra_type = MemberExtraInfoType()
        new_extra_type.description = extra_type
        new_extra_type.save()
        return new_extra_type


def add_formation(formation_name):
    try:
        return Formation.objects.filter(name=formation_name).get()
    except Formation.DoesNotExist:
        formation = Formation()
        formation.name = formation_name
        formation.save()
        return formation


def add_team(team_name):
    try:
        Team.objects.filter(team_name=team_name).get()
    except Team.DoesNotExist:
        team = Team()
        team.team_name = team_name
        team.save()


def add_status(status_name):
    try:
        return ProjectStatus.objects.filter(status=status_name).get()
    except ProjectStatus.DoesNotExist:
        status = ProjectStatus()
        status.status = status_name
        status.save()
        return status


def add_project(project_name):
    try:
        return Project.objects.filter(name=project_name).get()
    except Project.DoesNotExist:
        project = Project()
        project.name = project_name
        project.description = project_name
        project.status = status_by_name["En cours"]
        project.save()
        return project


def is_row_a_team(row):
    """
    If a fullname is filled and the next cell is empty(permanent code), it must be a team separator
    :param row:
    :return:
    """
    return row[M_FULLNAME] and not row[M_PERMANENT_CODE]


def extract_member_values(client):
    sheet = client.open_by_key(MEMBERS_SHEET_ID).sheet1

    values = sheet.get_all_records()

    current_team = None

    for row in values:
        # We don't add old members
        if row[M_FULLNAME] == M_STOP_LINE:
            break
        if is_row_a_team(row):
            current_team = row[M_FULLNAME]

            if current_team not in roles_per_team:
                roles_per_team[current_team] = set()
        else:
            unique_formation_names.add(row[M_PROG])
            roles_per_team[current_team].add(row[M_ROLE])
            row[M_TEAM] = current_team
            members.append(row)


def is_project_member(row, col):
    val = row[col]
    return val == "x" or val == P_TEAM_LEAD


def get_projects_from_first_row(row):
    projects = list(row.keys())
    projects.remove(P_MEMBER)
    projects.remove('')
    return projects


def extract_projects_values(client):
    global projects
    sheet = client.open_by_key(PROJECTS_SHEET_ID).sheet1

    values = sheet.get_all_records()
    projects = get_projects_from_first_row(values[0])

    for row in values:
        member_name = row[P_MEMBER]
        projects_by_member[member_name] = []

        for p in projects:
            if is_project_member(row, p):
                projects_by_member[member_name].append(p)


"""
Global variables that hold our state
"""
unique_formation_names = set()
roles_per_team = {}
statut = ['Prêt', 'En cours', 'Terminé']
projects = []

# Here we define the extra type that we want to store in the database.
# We also add the mapping for the CSV as a value
extra_info_type_mapping = {
    'permanent_code': M_PERMANENT_CODE,
    'universal_code': M_UNIVERSAL_CODE,
    'level': M_STUDIES_LEVEL,
    'in_stage': M_IN_STAGE,
    'phone_number': M_PHONE
}

"""
Global variables to keep created instances from the database and make them accessible via their name
"""
formations = {}
projects_by_member = {}
extra_info_types = {}
status_by_name = {}
projects_by_name = {}
members = []

# Setup the Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('google_secret.json', scope)
client = gspread.authorize(creds)

# Extract values from spreadsheet to variables
extract_member_values(client)
extract_projects_values(client)

"""
Add prerequisites object for the members
"""
for extra_type in extra_info_type_mapping.keys():
    extra_info_types[extra_type] = add_extra_type(extra_type)

for formation_name in unique_formation_names:
    formations[formation_name] = add_formation(formation_name)

for team_name in roles_per_team.keys():
    add_team(team_name)

for status_name in statut:
    status_by_name[status_name] = add_status(status_name)

for project_name in projects:
    projects_by_name[project_name] = add_project(project_name)

"""
Add role-team join
"""
for team, roles in roles_per_team.items():
    for role in roles:
        try:
            exist = TeamRole.objects.filter(role=role).get()
        except TeamRole.DoesNotExist:
            team_role = TeamRole()
            team_role.role = role
            team_role.team = Team.objects.filter(team_name=team).get()
            team_role.save()

"""
Add members with their good relationships
"""
for member in members:
    try:
        exist = Member.objects.filter(email=member[M_EMAIL]).get()
    except Member.DoesNotExist:
        new_member = Member()
        new_member.email = member[M_EMAIL]
        fullname = member[M_FULLNAME]
        fullname_splitted = fullname.split()
        new_member.first_name = fullname_splitted.pop(0)
        new_member.last_name = ' '.join(fullname_splitted)
        new_member.formation = formations[member[M_PROG]]

        if not member[M_PICTURE]:
            new_member.profilePicUrl = "http://default_avatar.geniale.ca"
        else:
            new_member.profilePicUrl = member[M_PICTURE]

        # We save to have an id for the many to many relationships
        new_member.save()

        # We get a list of role(s)
        team_roles = TeamRole.objects.filter(role=member[M_ROLE]).get()

        # We get the team object for this user
        member_team = Team.objects.filter(team_name=member[M_TEAM]).get()

        # If there is only one teamRole, it must be the good one :)
        if not isinstance(team_roles, list):
            new_member.teamRoles.add(team_roles)
        # If it's iterable, we check for a role that has the good team (this could be replaced by an inner join query)
        else:
            for role in team_roles:
                if role.team.team == member_team:
                    new_member.teamRoles.add(team_roles)
                    break

        # Add other extra_type
        for extra_type_name, extra_type in extra_info_types.items():
            csv_mapping = extra_info_type_mapping[extra_type_name]
            extra_info = MemberExtraInfo()
            extra_info.member = new_member
            extra_info.info_type = extra_type
            extra_info.value = member[csv_mapping]
            extra_info.save()

        if fullname in projects_by_member:
            member_projects = projects_by_member[fullname]
            for project in member_projects:
                new_member.projects.add(projects_by_name[project])
        new_member.save()

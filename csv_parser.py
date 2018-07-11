# -*- coding: utf-8 -*-
import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from teamModule.models import Formation, Team, Member, ProjectStatus, TeamRole, MemberExtraInfoType, MemberExtraInfo


# --------------------------------------------------------
# Projet: SiteWebGeniAle
# Par: GeniALE
# Auteur: Cedric Perreault - perreault.cedric@gmail.com
# Date: 05/06/2018
# --------------------------------------------------------

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
        ProjectStatus.objects.filter(status=status_name).get()
    except ProjectStatus.DoesNotExist:
        status = ProjectStatus()
        status.status = status_name
        status.save()


# Créer les listes d'informations
unique_formation_names = set()
roles_per_team = {}
teams = set()
statut = ['Prêt', 'En cours', 'Terminé']
extra_info_type_mapping = {
    'permanent_code': 'codepermanent ',
    'universal_code': 'codedaccesuniversel',
    'level': 'niveau',
    'in_stage': 'stage',
    'phone_number': 'telephone',
    'skills': 'competences'
}

# Data to keep references
formations = {}
extra_info_types = {}
membres = []

# Lire le fichier csv puis ajouter les informations dans les listes
with open('info.csv', encoding="ISO-8859-1") as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        unique_formation_names.add(row['prog'])
        team = row['equipe']
        if team not in roles_per_team:
            roles_per_team[team] = set()
        roles_per_team[team].add(row['role'])
        teams.add(row['equipe'])
        membres.append(row)

# Add all required base values
for extra_type in extra_info_type_mapping.keys():
    extra_info_types[extra_type] = add_extra_type(extra_type)

for formation_name in unique_formation_names:
    formations[formation_name] = add_formation(formation_name)

for team_name in teams:
    add_team(team_name)

for status_name in statut:
    add_status(status_name)

# Ajouter le rôle des membres de l'équipe en s'assurant de ne pas mettre le même deux fois
for team, roles in roles_per_team.items():
    for role in roles:
        try:
            exist = TeamRole.objects.filter(role=role).get()
        except TeamRole.DoesNotExist:
            teamrole = TeamRole()
            teamrole.role = role
            teamrole.team = Team.objects.filter(team_name=team).get()
            teamrole.save()

# Ajouter le nom des membres en s'assurant de ne pas mettre le même deux fois
for member in membres:
    try:
        exist = Member.objects.filter(email=member['courriel']).get()
    except Member.DoesNotExist:
        new_member = Member()
        new_member.email = member['courriel']
        nom_complet = member['nom'].split()
        new_member.first_name = nom_complet.pop(0)
        new_member.last_name = ' '.join(nom_complet)
        new_member.formation = formations[member['prog']]

        if not member['photo']:
            new_member.profilePicUrl = "http://default_avatar.geniale.ca"
        else:
            new_member.profilePicUrl = member['photo']

        # We save to have an id for the many to many relationships
        new_member.save()

        # We get a list of role(s)
        team_roles = TeamRole.objects.filter(role=member['role']).get()

        # We get the team object for this user
        member_team = Team.objects.filter(team_name=member['equipe']).get()

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

        new_member.save()

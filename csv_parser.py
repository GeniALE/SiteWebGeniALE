import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()
from teamModule.models import Formation, Team, Project, Member, ProjectStatus, TeamRole
import csv
# -*- coding: utf-8 -*-

#--------------------------------------------------------
# Projet: SiteWebGeniAle
# Par: GeniALE
# Auteur: Cedric Perreault - perreault.cedric@gmail.com
# Date: 05/06/2018
#--------------------------------------------------------

# Créer les listes d'informations
formation = set()
roleParEquipe = {}
equipes = set()
statut = ['Prêt','En cours','Terminé']
membres = []

# Lire le fichier csv puis ajouter les informations dans les listes
with open('info.csv', encoding = "ISO-8859-1") as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        formation.add(row['prog'])
        equipe = row['equipe']
        if equipe not in roleParEquipe:
            roleParEquipe[equipe] = set()
        roleParEquipe[equipe].add(row['role'])
        equipes.add(row['equipe'])
        membres.append(row)
        
# Ajouter les formations en s'assurant de ne pas mettre le même deux fois
for nom_formation in formation:
    try:
        exist = Formation.objects.filter(name = nom_formation).get()
    except Formation.DoesNotExist:
        formation = Formation()
        formation.name = nom_formation
        formation.save() 

# Ajouter le nom des équipes en s'assurant de ne pas mettre le même deux fois
for nom_equipe in equipes:
    try:
        exist = Team.objects.filter(team_name = nom_equipe).get()
    except Team.DoesNotExist:
        team = Team()
        team.team_name = nom_equipe
        team.save()

# Ajouter le statut des projets en s'assurant de ne pas mettre le même deux fois
for nom_statut in statut:
    try:
        exist = ProjectStatus.objects.filter(status = nom_statut).get()
    except ProjectStatus.DoesNotExist:
        statut = ProjectStatus()
        statut.status = nom_statut
        statut.save()
    
# Ajouter le rôle des membres de l'équipe en s'assurant de ne pas mettre le même deux fois
for team, roles in roleParEquipe.items():
    for role in roles:
        try:
            exist = TeamRole.objects.filter(role = role).get()
        except TeamRole.DoesNotExist:
            teamrole = TeamRole()
            teamrole.role = role
            teamrole.team = Team.objects.filter(team_name = team).get()
            teamrole.save()

# Ajouter le nom des membres en s'assurant de ne pas mettre le même deux fois
for membre in membres:
    try:
        exist = Member.objects.filter(email = membre['courriel']).get()
    except Member.DoesNotExist:
        member = Member()
        member.email = membre['courriel']
        nom_complet = membre['nom'].split()
        member.first_name = nom_complet.pop(0)
        member.last_name = ' '.join(nom_complet)
        
        #We save to have an id for the many to many relationships
        member.save()

        #We get a list of role(s)
        team_roles = TeamRole.objects.filter(role=membre['role']).get()

        #We get the team object for this user
        member_team = Team.objects.filter(team_name=membre['equipe']).get()

        #If there is only one teamRole, it must be the good one :)
        if not isinstance(team_roles, list):
            member.teamRoles.add(team_roles)
        #If it's iterable, we check for a role that has the good team (this could be replaced by an inner join query)
        else:    
            for role in team_roles:
                if role.team.team == member_team:
                    member.teamRoles.add(team_roles)
                    break

        member.save()


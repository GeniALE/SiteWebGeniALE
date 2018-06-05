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
prenom = set()
courriel = set()

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
        prenom.add(row['nom'])
        courriel.add(row['courriel'])
        
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
for nom in prenom:
    try:
        exist = Member.objects.filter(first_name = nom).get()
    except Member.DoesNotExist:
        member = Member()
        member.first_name = nom
        member.save()

# Ajouter le courriel des membres en s'assurant de ne pas mettre le même deux fois
for courriel in courriel:
    try:
        exist = Member.objects.filter(email = nom).get()
    except Member.DoesNotExist:
        member = Member()
        member.email = courriel
        member.save()
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()
from teamModule.models import Formation, Team, Project, Member, ProjectStatus, TeamRole
# -*- coding: utf-8 -*-

#--------------------------------------------------------
# Projet: SiteWebGeniAle
# Par: GeniALE
# Auteur: Cedric Perreault - perreault.cedric@gmail.com
# Date: 21/03/2018
#--------------------------------------------------------

# from __future__ import absolute_import, print_function, unicode_literals

# from django.contrib.auth import get_user_model

# if __name__ == '__main__':
#     import django

#     django.setup()   

#     User = get_user_model()
#     if not User.objects.filter(is_superuser=True).exists():
#         User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

import csv

formation = []
role = []
equipe = []

with open('info.csv', encoding = "ISO-8859-1") as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        formation.append(row['prog'])
        role.append(row['role'])
        equipe.append(row['equipe'])

    formation = list(set(formation)) 
    role = list(set(role))
    equipe = list(set(equipe))
    print(formation)
    print(equipe)
    print(role)


# Ajouter formation
#formation = Formation()
#formation.name = row['prog']


        #membre = Member()
        #membre.first_name = row['nom']
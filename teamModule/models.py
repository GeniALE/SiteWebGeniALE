from django.db import models


# Create your models here.
class Formation(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length=30)

    def __str__(self):
        return self.team_name


class TeamRole(models.Model):
    role = models.CharField(max_length=20)
    description = models.CharField(max_length=1000, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.role


class ProjectStatus(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    status = models.ForeignKey(ProjectStatus, default=0, on_delete=models.SET_DEFAULT)
    website = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.project_name


class Member(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    bio = models.CharField(max_length=400, null=True)
    email = models.CharField(max_length=75, null=True)
    linkedInUrl = models.CharField(max_length=200, null=True)
    profilePicUrl = models.CharField(max_length=200, null=True)
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL, null=True)
    teamRoles = models.ManyToManyField(TeamRole)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

from django.db import models
from cms.models.pluginmodel import CMSPlugin


class ServiceInstructions(models.Model):
    # Name of the service
    service_name = models.CharField(max_length=100, blank=False, null=False)

    # Url that allows to register a user to that service
    register_url = models.CharField(max_length=255, blank=True, null=True)

    # Url that allows to unregister a user from that service
    unregister_url = models.CharField(max_length=255, blank=True, null=True)

    # Allow to map the username of the service using a field of a member. For example: email would show the member email.
    member_mapping_to_username = models.CharField(max_length=50, blank=False, null=False)

    # Allow to store an instruction file (pdf). Easier to maintain for the admins :)
    instruction_file = models.FileField(upload_to="medias/", blank=True)

    def __str__(self):
        return self.service_name

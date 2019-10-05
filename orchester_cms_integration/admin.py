from orchester_cms_integration.models import ServiceInstructions
from django.contrib import admin


class ServiceInstructionsAdmin(admin.ModelAdmin):
  model = ServiceInstructions


admin.site.register(ServiceInstructions, ServiceInstructionsAdmin)

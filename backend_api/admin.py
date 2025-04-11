from django.contrib import admin
from . import models


class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['question']
admin.site.register(models.Material, MaterialAdmin)
admin.site.register(models.Сategories)
admin.site.register(models.ProjectInformation)


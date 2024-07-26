from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Team

from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('division', 'conference', 'wins', 'losses', 'name', 'logo_path')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from RestAPI.models import Actor, Repository, Event


# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    model = Actor
    list_display = ['id', 'is_active', 'created_at', 'updated_at']


admin.site.register(Actor, ActorAdmin)
admin.site.register(Event)
admin.site.register(Repository)

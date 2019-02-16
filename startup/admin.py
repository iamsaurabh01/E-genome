# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

class StartupAdmin(admin.ModelAdmin):
	list_display = ['email', 'created', 'modified']
	search_fields = ['email', 'created', 'modified']

admin.site.register(Startup, StartupAdmin)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class MentorAdmin(admin.ModelAdmin):
	list_display = ['email', 'created', 'modified', 'name', 'spicialization_field']
	search_fields = ['email', 'created', 'modified', 'name', 'spicialization_field']

admin.site.register(Mentor, MentorAdmin)

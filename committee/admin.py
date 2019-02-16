# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Committee

class CommitteeAdmin(admin.ModelAdmin):
	list_display = ['institute_name', 'city','committee_name', 'description', 'last2activities1', 'last2activities2', 'self_certification', 'email']
	search_fileds=['institute_name','city','committee_name', 'description', 'last2activities1', 'last2activities2', 'self_certification', 'email'] 


admin.site.register(Committee, CommitteeAdmin)
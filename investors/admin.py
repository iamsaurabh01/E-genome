# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class InvestorAdmin(admin.ModelAdmin):
	list_display = ['email', 'created', 'modified']
	search_fields = ['email', 'created', 'modified']

admin.site.register(Investor, InvestorAdmin)


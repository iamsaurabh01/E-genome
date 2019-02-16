# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from news.models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
	list_display = ["headline", "news_image", "news_para", "created", "modified"]
	search_fields = ["headline", "news_para", "news_image", "created", "modified"]

admin.site.register(News,NewsAdmin)


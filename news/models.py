# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class News(models.Model):
	headline = models.CharField(max_length=1000, blank=True, null=True)
	news_para = models.CharField(max_length=5000, blank=True, null=True)
	news_image = models.ImageField(upload_to='news', blank=True, null=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.headline

	def __unicode__(self):
		return self.headline

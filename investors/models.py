from __future__ import unicode_literals

from django.db import models

class Investor(models.Model):
	email = models.CharField(blank=False, null=False, max_length=50)
	password = models.CharField(max_length=20, blank=True, null=True)
	company_name = models.CharField(max_length=50, blank=True, null=True)
	country = models.CharField(max_length=20, blank=True, null=True)
	address = models.TextField(max_length=500, blank=True, null=True)
	company_type = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField(max_length=5000, blank=True, null=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False) 

	def __str__(self):
		return self.email

	def __unicode__(self):
		return self.email

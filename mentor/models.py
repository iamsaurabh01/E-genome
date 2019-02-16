# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

SPECIALIZATION = (
	('software', 'software'),
	('hardware', 'hardware'),
	('marketing', 'marketing'),
	('finances', 'finances'),
	('other', 'other')
)


class Mentor(models.Model):
	email = models.CharField(blank=False, null=False, max_length=50)
	password = models.CharField(max_length=20, blank=True, null=True)
	name = models.CharField(max_length=20, blank=True, null=True)
	spicialization_field = models.CharField(max_length=20, choices=SPECIALIZATION)
	description = models.TextField(max_length=2000, blank=True, null=True)
	document = models.FileField(upload_to='mentor_documents')
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False) 
	
	def __str__(self):
		return self.email	

	def __unicode__(self):
		return self.email


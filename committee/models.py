# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TYPE_CHOICES = (
	('PROFITABLE', 'profitable'),
	('NON-PROFITABLE', 'non-profitable')
)


class Committee(models.Model):
	institute_name = models.CharField(blank=False, null=False, max_length=100)
	state = models.CharField(max_length=20, blank=False, null=False)
	city = models.CharField(max_length=20, blank=True, null=True)
	committee_name = models.CharField(max_length=100, blank=False, null=False)
	description = models.CharField(max_length=5000, blank=True, null=True)
	committee_type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=True)
	last2activities1 = models.FileField(upload_to='committee_documents')
	last2activities2 = models.FileField(upload_to='committee_documents')
	self_certification = models.FileField(upload_to='committee_documents')
	email = models.CharField(blank=False, null=False, max_length=50)
	password = models.CharField(max_length=20, blank=True, null=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False) 
	
	def __str__(self):
		return self.committee_name

	def __unicode__(self):
		return self.committee_name


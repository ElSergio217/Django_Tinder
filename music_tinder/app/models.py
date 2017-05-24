# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from music_tinder import settings
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='photos', default="photos/avatar-1577909_640.png")
	bio = models.TextField(default="")
	website = models.URLField(default="")
	friends = models.ManyToManyField(User, related_name='+')

	def __unicode__(self):
		return self.user.get_full_name()

class UserVote(models.Model):
	user = models.ForeignKey(User)
	voter = models.ForeignKey(User, related_name='given_vote')
	vote = models.BooleanField(default=False)

	class Meta:
		unique_together = (('user', 'voter'))

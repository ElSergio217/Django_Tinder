# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import forms
from django.shortcuts import redirect
from . import models
from models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required
def index(request):
	try:
		user = (User.objects.exclude(id=request.user.id).exclude(uservote__voter=request.user).order_by('?')[0])
	except IndexError:
		user = None
	profile = (User.objects.get(id=request.user.id))
	context = dict(user = user)
	return render(request, 'index.html', context)


def create_vote(request, user_id, vote):
	user = User.objects.get(pk=user_id)
	models.UserVote.objects.create(
		user = user,
		voter = request.user,
		vote = vote
	)
	return redirect('index')

@login_required
def nice(request, user_id):
	return create_vote(request, user_id, True)

@login_required
def nope(request, user_id):
	return create_vote(request, user_id, False)

@login_required
def profile(request):
	try:
		profile = request.user.userprofile
	except models.UserProfile.DoesNotExist:
		profile = None
	if request.method == 'POST':
		form = forms.UserProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			if profile:
				form.save()
			else:
				profile = form.save(commit=False)
				profile.user = request.user
				profile.save()
	form = forms.UserProfileForm(instance=profile)
	context = dict(form=form)
	return render(request, "profile.html", context)

def create_vote(request, user_id, vote):
	user = User.objects.get(pk=user_id)
	models.UserVote.objects.create(
		user=user,
		voter=request.user,
		vote=vote
	)
	if vote:
		if models.UserVote.objects.filter(
			user = request.user,
			voter=user,
			vote=True
		).count():
			return render(request, 'match.html', dict(
				match=user,
			))
	return redirect('index')
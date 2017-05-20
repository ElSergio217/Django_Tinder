# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import forms
from django.shortcuts import redirect
from . import models
from models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
	try:
		user = (User.objects.exclude(id=request.user.id).exclude(uservote__voter=request.user).order_by('?')[0])
	except IndexError:
		user = None
	
	try:
		bio = models.UserProfile.objects.get(user=request.user).bio
	except models.UserProfile.DoesNotExist:
		return redirect('profile')
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
	info = User.objects.get(username=request.user)
	user = models.UserProfile.objects.get(user=request.user)
	name = info.first_name
	last = info.last_name
	email = info.email
	bio = user.bio
	print user.photo.url
	if request.method == 'POST':
		form = UserCreationForm(request.POST, request.FILES)
		if form.is_valid:
			if request.POST['first_name'] != name:
	 			info.first_name = request.POST['first_name']
	 		else:
	 			info.name = name

			if request.POST['last_name'] != last:
				info.last_name = request.POST['last_name']
			else:
				info.last = last

			if request.POST['email'] != email:
				info.email = request.POST['email']
			else:
				info.email = email

			if request.POST['bio'] != bio:
				user.bio = request.POST['bio']
			else:
				user.bio = bio
			if len(request.FILES) != 0:
				user.photo.delete()
				user.photo = request.FILES['image']

			if info.check_password(request.POST['password']) ==True:
				if request.POST['new_password'] != "":
					info.set_password(request.POST['new_password'])
			info.save()
			user.save()
	context = dict(info=info, user = user)
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
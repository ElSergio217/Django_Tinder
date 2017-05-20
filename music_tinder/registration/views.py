# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
	if request.user.is_authenticated():
		return redirect('index')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	context = dict(form=form)
	return render(request, 'registration/register.html', context)
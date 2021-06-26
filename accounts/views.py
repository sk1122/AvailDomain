from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
	'''
		@params - username, password
	'''
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = User(username=username, password=password)
			return redirect('login')
		else:
			form = UserCreationForm(request.POST)
			context = {
				'form': form
			}
			return render(request, "registration/register.html", context)
	else:
		form = UserCreationForm()
		context = {
			'form': form
		}
		return render(request, "registration/register.html", context)

def signin(request):
	'''
		@params - username, password
	'''
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('domain_availablity')
		else:
			messages.info(request, "Wrong Credentials")
			form = AuthenticationForm(request.POST)
			return render(request, 'registration/login.html', {'form': form})
	else:
		form = AuthenticationForm()
		return render(request, 'registration/login.html', {'form': form})

def signout(request):
	logout(request)
	return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register(request):
	print(request.user)
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = User(username=username, password=password)
			return render(request, "base.html")
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
	print('dsa')
	if request.user.is_authenticated:
		return render(request, 'base.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
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
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import *

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def domain_availablity(request):
	if not request.user.is_authenticated:
		return redirect('login')
	return render(request, "check_domain.html")

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def history(request):
	if not request.user.is_authenticated:
		return redirect('login')
	context =  {
		'history': History.objects.filter(user=request.user)
	}
	return render(request, "profile.html", context)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *

from .utils import getDetails, available_tlds

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def check_domain_available(request):
	'''
		Checks if Domain is Taken or Available
	'''
	if request.method == 'POST':
		domain = request.data.get('domain')
		serializer = HistorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			details = getDetails(domain) # Details of Domain from whois package
			return Response({'data': details})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def check_domain_available2(request):
	'''
		Checks if Domain is Taken or Available
	'''
	if request.method == 'POST':
		domain = request.data.get('domain')
		details = getDetails(domain) # Details of Domain from whois package
		return Response({'data': details})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_available_tlds(request):
	'''
		Get All Available TLD's for Searching
	'''
	tld_list = available_tlds()

	return Response({'data': tld_list})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_history(request):
	'''
		Get All Available Searches of Domain
	'''
	history = History.objects.filter(user=request.user)
	serializer = HistorySerializer(history, many=True)
	return Response({"data": serializer.data})

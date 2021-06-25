from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

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

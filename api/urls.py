from django.urls import path
from . import views
from . import template_views
urlpatterns = [
	path('api/check_domain/', views.check_domain_available, name="check_availablity"),
	path('api/check_domain2/', views.check_domain_available2, name="check_availablity2"),
	path('api/get_available_tlds/', views.get_available_tlds, name="get_available_tlds"),
	path('api/get_history/', views.get_history, name="get_history"),
	
	path('', template_views.domain_availablity, name="domain_availablity"),
	path('profile/', template_views.history, name="profile"),
]
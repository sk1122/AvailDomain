from django.urls import path
from . import views
from . import template_views
urlpatterns = [
	path('check_domain/', views.check_domain_available, name="check_availablity"),
	path('other_domains/', views.get_available_tlds, name="get_other_domains"),
	path('', template_views.domain_availablity, name="domain_availablity"),
]
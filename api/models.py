from django.db import models
from django.contrib.auth.models import User

class History(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="platform_user")
	domain = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now_add=True)
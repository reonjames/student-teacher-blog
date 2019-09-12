from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class UserProfile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.name
class Student(models.Model):
	name=models.CharField(max_length=30)
	standard=models.IntegerField()
	bio=models.IntegerField()
	eng=models.IntegerField()
	maths=models.IntegerField()
	# up=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.name	
			
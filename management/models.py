from django.conf import settings
from django.db import models
from django.utils import timezone
class User(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	password=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	student=models.ForeignKey('Student',on_delete=models.CASCADE)
	# academic=models.ForeignKey('Academic',on_delete=models.CASCADE)
	def __str__(self):
		return self.first_name
class Student(models.Model):
	name=models.CharField(max_length=30)
	roll_no=models.IntegerField()
	age=models.IntegerField()
	standard=models.IntegerField()
	year=models.IntegerField()
	def __str__(self):
		return self.name

class Academic(models.Model):
	std=models.ForeignKey('Student',on_delete=models.CASCADE)
	exam=models.CharField(max_length=15)
	bio=models.IntegerField()
	maths=models.IntegerField()
	eng=models.IntegerField()
	chem=models.IntegerField()
	def __str__(self):
		return self.exam

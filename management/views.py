from.models import *
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse




def home(request):
	return render(request,'home.html',{})
def sign_up(request):
	if request.method == 'POST':
		
		
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		print (name,email,password)
		
		# name1 = UserProfile.objects.filter(name=name).exists()
		email1 = UserProfile.objects.filter(email=email).exists()
		
		if not email1:

			user1 = User.objects.create_user(
				username=email,
				password = password 

				)
			# user1.save()
			user = UserProfile.objects.create(
				user=user1,
				name=name,
				email=email,
				
				password=password,
			)

			return render(request, 'login.html', {})
		else:               
			error = " Email or Phone-Number already exists "
			return render(request, 'signup.html', {'error': error})
	else:
		return render(request, 'signup.html',{})

def log_in(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(email,password)
		user = authenticate(username=email, password=password)

		if user:
			print(user)
			login(request, user)
			return render(request, 'academic.html', {})
		else:
			error = " Sorry! Phone Number and Password didn't match, Please try again ! "
			return render(request, 'login.html', {'error': error})
	else:
		return render(request, 'login.html', {})
def student(request):
	if request.method == "POST":
		name=request.POST.get('fname')
		std=request.POST.get('std')
		bio=request.POST.get('bio')
		math=request.POST.get('math')
		eng=request.POST.get('eng')
		stud=Student.objects.create(
			name=name,
			standard=std,
			bio=bio,
			maths=math,
			eng=eng,
			)
		return render(request,'home.html',{})
	else:
		return render(request,'academic.html',{})
def detail(request,pk):
	detl=Student.objects.get(pk=pk)
	return render(request,'detail.html',{'detl':detl})
							








					



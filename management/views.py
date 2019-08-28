from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User,Student,Academic

def home(request):
	return render(request,'registration/home.html',{})

def sign(request):
	if request.method == 'POST':
		user=User()
		user.first_name=request.POST.get('f_name')
		user.last_name=request.POST.get('l_name')
		user.email=request.POST.get('email')
		user.password=request.POST.get('psswd')
		user.save()
		return render(request,'registration/login.html',{})
	else:
		return render(request,'registration/demo.html',{})		

# def pagelogin(request):
  
#     uservalue=''
#     passwordvalue=''

#     form= Loginform(request.POST or None)
#     if form.is_valid():
#         uservalue= form.cleaned_data.get("username")
#         passwordvalue= form.cleaned_data.get("password")

#         user= authenticate(username=uservalue, password=passwordvalue)
#         if user is not None:
#             login(request, user)
#             context= {'form': form,
#                       'error': 'The login has been successful'}
            
#             return render(request, 'siteusers/login.html', context)
#         else:
#             context= {'form': form,
#                       'error': 'The username and password combination is incorrect'}
            
#             return render(request, 'siteusers/login.html', context )

#     else:
#         context= {'form': form}
#         return render(request, 'siteusers/login.html', context)



def login(request):
	if request.method =='POST':
		email=request.POST.get('email')
		password=request.POST.get('psswd')
		if User.objects.filter(email='email',password='password').exists():
			return render(request,'registration/demo.html',{})
		else:
			return render(request,'registration/login.html',{})
	else:
		return render(request,'registration/login.html',{})
def student(request):
	if request.method=='POST':
		std=Student()
		std.name=request.POST.get('name')
		std.roll_no=request.POST.get('rn')
		std.age=request.POST.get('age')
		std.standard=request.POST.get('class')
		std.year=request.POST.get('year')
		std.save()
		return render(request,'registration/demo.html',{})
	else:
		return render(request,'registration/studentdetail.html',{})	
def search(request):
	if request.mathod=='GET'
		nam=request.GET.get('search')
		sname=Student.objects.filter(name=nam)
		return render(request,'registration/academic.html'{"mark":sname})
	else:
		return render(request,'registration/search.html',{})	

def academic(request):
	post=Academic.objects.get()
	acd=Academic()
	acd.bio=request.POST.get('bio')
	acd.maths=request.POST.get('math')
	acd.eng=request.POST.get('eng')
	acd.chem=request.POST.get('chem')
	acd.save()
	return render(request,'registration/academic.html',{'post':post})





					



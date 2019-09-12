from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home_url'),
    path('signup/',views.sign_up,name='sign_url'),
    path('login/',views.log_in,name='login_url'),
    path('student/',views.student,name='student_url'),
    path('detail/<int:pk>/',views.detail,name='detail_url'),
    
]	

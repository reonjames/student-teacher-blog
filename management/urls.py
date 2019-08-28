from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home_url'),
    path('signup/',views.sign,name='sign_url'),
    path('login/',views.login,name='login_url'),
    path('student/',views.student,name='student_url'),
    path('search/'views.search,name='search_url'),
]	

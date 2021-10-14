
from django.urls import path
from django.contrib.auth import  views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('archive', login_required(views.archive), name='archive'),
    path('archive/<str:pk>', login_required(views.subject_detail), name='details'),
    path('login/', auth_views.LoginView.as_view(template_name='demo/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='demo/registration/login.html'), name='logout'),
]
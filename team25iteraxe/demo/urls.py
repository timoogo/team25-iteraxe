from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/<str:pk>', views.subject_detail, name='details')
]
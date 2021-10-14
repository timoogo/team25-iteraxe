from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('demo.urls'), name='demo_urls'),
    path('admin/', admin.site.urls),
]

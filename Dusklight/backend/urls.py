"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sunset-azimuth/', views.sunset_azimuth, name='sunset_azimuth'),
    path('api/sun-aligned-time/', views.sun_aligned_time, name='sun_aligned_time'),
    path('api/sun-aligned-time-batch/', views.sun_aligned_time_batch, name='sun_aligned_time_batch'),
    path('api/sun-altitude/', views.sun_altitude, name='sun_altitude'),
    path('api/sun-altitude-batch/', views.sun_altitude_batch, name='sun_altitude_batch'),
    path('', views.dusklight_map, name='dusklight_map'),
]

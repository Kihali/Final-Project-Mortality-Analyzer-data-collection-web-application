"""
URL configuration for ChildMortalityAnalyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from data_collector import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('admin/', admin.site.urls),
    path('add/', views.add_data, name='add_data'),
    path('export/', views.export_data, name='export_data'),
    path('clear/', views.clear_data, name='clear_data'),
]
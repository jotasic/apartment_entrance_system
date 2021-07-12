"""apartmentsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest 프레임워크에서 쓰려고rest_auth.registration.urls
    path('api-auth/', include('rest_framework.urls')),

    # api로 제공
    path('api/users/registration/', include('rest_auth.registration.urls')),
    path('api/users/', include('rest_auth.urls')),
    path('api', include('api.urls')),
]

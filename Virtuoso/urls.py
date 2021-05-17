"""Virtuoso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from doc.views import homepage
from company.views import companypage
from services.views import servicepage,Enterpriseapp,Mobileapp,Webapp
from contact.views import contactpage,showformdata

urlpatterns= [
    path('admin/', admin.site.urls),
    path('home/',homepage),
    path('company/',companypage),
    path('services/',servicepage), 
    path('services/Enterprise-app/',Enterpriseapp),
    path('services/Mobile-app/',Mobileapp),
    path('services/Web-app/',Webapp),
   # path('contact/',contactpage),
    path('contact/',showformdata),
]

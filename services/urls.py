from django.contrib import admin
from django.urls import path
from views import Enterpriseapp


urlpatterns= [
    path('admin/', admin.site.urls),
   
]

from django.shortcuts import render

# Create your views here.

def servicepage(request):
   # return HttpResponse("<h1>Pabon Shaha</h1>")

   return render(request,"service.html")

def Enterpriseapp(request):
   # return HttpResponse("<h1>Pabon Shaha</h1>")

   return render(request,"Enterprise.html")


def Mobileapp(request):
   # return HttpResponse("<h1>Pabon Shaha</h1>")

   return render(request,"Mobileapp.html")



def Webapp(request):
   # return HttpResponse("<h1>Pabon Shaha</h1>")

   return render(request,"Webapp.html")
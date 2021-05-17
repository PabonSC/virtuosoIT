from django.shortcuts import render

# Create your views here.
def companypage(request):
   # return HttpResponse("<h1>Pabon Shaha</h1>")

   return render(request,"company.html")
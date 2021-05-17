from django.shortcuts import render
from contact.forms import Registration
from contact.models import Contact

# Create your views here.
def contactpage(request):
   # return HttpResponse("<h1>Pabon Shaha</h1>")

   return render(request,"contact.html")


def showformdata(request):
   if request.method=="POST":
      fm = Registration(request.POST)

      name=request.POST["name"]
      email=request.POST["email"]
      password=request.POST["password"]
      note=request.POST["note"]

      obj=Contact(name="name",email="email",password="password",note="note")
      obj.save
      

   else:
      fm=Registration()

   return render(request,"contact.html",{'form':fm})

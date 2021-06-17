from django.shortcuts import render,HttpResponse
from .models import Project
from .models import Contact
from django.contrib import messages
from datetime import date, datetime

def home(request):
    project=Project.objects.all()
    return render(request,'home.html',{'project':project})

def contact(request):
     if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your feedback has been sent.')

     return render(request,'contact.html')

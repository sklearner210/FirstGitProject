from django.shortcuts import render, HttpResponse
from datetime import datetime
from app.models import Contact
#from django.contrib import messages

# Create your views here.
def index(request):
    #messages.success(request,"This is for testing")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        contact = Contact(fname=fname,lname=lname,email=email,phone=phone,comment=comment,date=datetime.today())
        contact.save()
       # messages.success(request,"Your data has been saved")
    return render(request, 'contact.html')

def Services(request):
    return render(request, 'services.html')
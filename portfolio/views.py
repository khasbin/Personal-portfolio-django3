from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .models import Contact
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/portfolio.html', {'projects':projects})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = Contact(name= name,email = email,message = message)
        ins.save()

    return render(request, 'portfolio/contact.html')

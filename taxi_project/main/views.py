from django.shortcuts import render
from . import models

# Create your views here.
def index_page(request):
    print("request is accepted")
    return render(request, "main/index.html", {})

def login_page(request):
    return render(request, "main/login.html", {})

def drivers_page(request):
    return render(request, "main/drivers.html", {})

def drivers_application_page(request):
    return render(request, "main/drivers_application.html", {})

def passengers_page(request):
    return render(request, "main/passengers.html", {})

def helpdesk_page(request):
    return render(request, "main/helpdesk_page.html", {})

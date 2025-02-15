from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def contact(request):
    return render(request, "pages/contact.html")

def about(request):
    return render(request, "pages/about.html")
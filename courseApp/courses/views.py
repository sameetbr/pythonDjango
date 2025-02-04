from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request): #Bu metodlar view diye adlandırılıyo
    return HttpResponse("Anasayfa")

def kurslar(request): #Bu metodlar view diye adlandırılıyo
    return HttpResponse("Kurs Listesi")

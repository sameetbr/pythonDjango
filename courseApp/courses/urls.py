from django.http import HttpResponse
from django.urls import path
from . import views

#http://127.0.0.1:8000/client => anasayfa
#http://127.0.0.1:8000/client/home 
#http://127.0.0.1:8000/client/kurslar => kurs listesi


urlpatterns = [
    path("", views.index),
    path("<kursAdi>", views.details),
    path("category/<int:categoryID>", views.getCoursesByCategoryID),
    path("category/<str:categoryName>", views.getCoursesByCategory, name="courses_by_category")
]

from datetime import date
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

data = {
    "programlama":"Programlama kategorisine ait kurslar",
    "web-gelistirme":"Web gelistirme kategorisine ait kurslar",
    "mobil-uygulamalar":"Mobil kategorisine ait kurslar",
}

db = {
    "courses" : [
        {
            "title" : "Javascript Kursu",
            "description" : "Javascript kurs açıklaması",
            "imageUrl" : "1.jpg",
            "slug" : "javascript-kursu",
            "date" : date(2022,10,2),
            "isActive" : True,
            "isUpdated" : True
        },
        {
            "title" : "Python Kursu",
            "description" : "Python kurs açiklamasi",
            "imageUrl" : "2.jpg",
            "slug" : "python-kursu",
            "date" : date(2022,9,2),
            "isActive" : False,
            "isUpdated" : True
        },
        {
            "title" : "Web Geliştirme Kursu",
            "description" : "Web Geliştirme kurs açıklaması",
            "imageUrl" : "3.jpg",
            "slug" : "web-geliştirme-kursu",
            "date" : date(2022,8,2),
            "isActive" : True,
            "isUpdated" : False
        },
    ]
    ,"categories" : [
        {"id" : 1  ,"name" : "programlama", "slug" : "programlama"}, 
        {"id" : 2, "name" : "web geliştirme", "slug" : "web-gelistirme"}, 
        {"id" : 3, "name" : "mobil uygulamalar", "slug" : "mobil-uygulamalar"}
    ]
}

#http://127.0.0.1:8000/kurs/ 

def index(request):
    kurslar = [course for course in db["courses"] if course["isActive"] == 1 ]
    kategoriler = db["categories"]

    # for kurs in db["courses"]:
    #     if kurs["isActive"]== 1:
    #         kurslar.append(kurs)

    return render(request, "courses/index.html", {
        "categories" : kategoriler,
        "courses" : kurslar
    })


def details(request, kursAdi):
    return HttpResponse(f"{kursAdi} detay sayfası")

def getCoursesByCategory(request, categoryName):
    try: 
        categoryText = data[categoryName]
        return render(request, "courses/courses.html",{
            "category" : categoryName,
            "category_text" : categoryText
        })
    except:
        return HttpResponseNotFound("Yanliş Kategori Seçimi")


def getCoursesByCategoryID(request, categoryID):
   # return redirect("/kurs/category/programlama")
    categories = list(data.keys())

    if categoryID > len(categories):
        return HttpResponseNotFound("Yanlış ID ile Kategori Seçme")
    
    categoryName = categories[categoryID - 1]
    redirect_url = reverse("courses_by_category", args=[categoryName])

    return redirect(redirect_url)

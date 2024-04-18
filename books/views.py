from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
data = {
    "tarih" : "tarih kategorisindeki kitap listesi",
    "roman" : "roman kategorisindeki kitap listesi",
    "psikoloji" : "psikoloji kategorisindeki kitap listesi"
}
def index(request):
    return HttpResponse("Anasayfa")

def books(request):
    return HttpResponse("Kitaplar Sayfası")

def getBooksByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi, lütfen gitmek istediğiniz sayfayı kontrol ediniz.")

def getBooksByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("Yanlış kategori Seçimi...")
    redirect_text = category_list[category_id-1]

    return redirect("/books/category/" + redirect_text)
def getBooksByAuthor(request):
    return HttpResponse("Yazara göre kitap listesi")


def authors(request):
    return HttpResponse("Yazarlar Sayfası")

def categories(request):
    return HttpResponse("Kategoriler Sayfası")

def bookdetail(request, id):
    return HttpResponse(f"{id} numaralı Kitap detay sayfası")

def bookdetailname(request, name):
    liste = (name.split("-"))
    name = ""
    new = [i.title() for i in liste]
    for n in new:
        name+= n + " "
    return HttpResponse(f"{name} adlı Kitap detay sayfası")



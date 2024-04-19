from django.shortcuts import render, redirect 
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Category, Book


# Create your views here.
data = {
    "tarih" : "tarih kategorisindeki kitap listesi",
    "roman" : "roman kategorisindeki kitap listesi",
    "psikoloji" : "psikoloji kategorisindeki kitap listesi"
}
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books.html", context)

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
    category_name = category_list[category_id-1]

    redirect_url = reverse("category_name", args=[category_name])

    return redirect(redirect_url)


def getBooksByAuthor(request):
    return HttpResponse("Yazara göre kitap listesi")


def authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request,"authors.html", context)

def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories.html", context)

def bookdetail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, "book-detail.html", {"book": book})
    except:
        return HttpResponseNotFound("Kitap Bulunamadı...")

def bookdetailname(request, slug_name):
    try:
        context = {"book" : Book.objects.get(slug=slug_name)}
        return render(request, "book-detail-name.html", context )
    except Book.DoesNotExist:
        return HttpResponseNotFound("Kitap Bulunamadı....")



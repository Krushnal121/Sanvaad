from django.shortcuts import render, HttpResponse
from .models import Article, Banners

def home(request):
    items = Article.objects.all()
    images = Banners.objects.all()
    return render(request,"index.html",{"Article":items, "images":images})



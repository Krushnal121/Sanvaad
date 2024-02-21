from django.shortcuts import render, HttpResponse
from .models import Article

def home(request):
    items = Article.objects.all()
    return render(request,"index.html",{"Article":items})



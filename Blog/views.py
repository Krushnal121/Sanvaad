from django.shortcuts import render, HttpResponse
from Home.models import Article

def blog(request):
    items = Article.objects.all()
    return render(request,"blog.html", {"Article": items})

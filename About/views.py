from django.shortcuts import render, HttpResponse

def about(request):
    return render(request,"about.html")

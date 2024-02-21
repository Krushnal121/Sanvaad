from django.shortcuts import render, HttpResponse

def dblogs(request):
    return render(request,"dblogs.html")

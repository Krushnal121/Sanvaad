from django.shortcuts import render, HttpResponse

def team(request):
    return render(request,"team.html")

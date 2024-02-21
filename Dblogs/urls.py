from django.urls import path
from . import views
urlpatterns = [
    path('', views.dblogs, name="dblogs")
]
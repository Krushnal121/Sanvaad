from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Home.urls")),
    path("blogs", include("Blog.urls")),
    path("about", include("About.urls")),
    path("contact",include("Contact.urls")),
    path("team", include("Team.urls")),
    path("dblogs", include("Dblogs.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
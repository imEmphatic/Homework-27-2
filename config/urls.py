from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("materials/", include("materials.urls")),
    path("", RedirectView.as_view(url="/materials/courses/", permanent=True)),
]

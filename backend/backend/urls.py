from django.contrib import admin
from django.urls import path

from todos import views as todo_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todo_views.index),
]

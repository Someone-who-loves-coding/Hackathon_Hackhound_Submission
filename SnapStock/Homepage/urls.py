from django.contrib import admin
from django.urls import path
from Homepage import views

urlpatterns = [
    path('admin/', admin.site.urls)
]
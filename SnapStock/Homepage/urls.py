from django.contrib import admin
from django.urls import path
from Homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index),
    path('Home/',views.Home),
    path('Recipes/',views.Recipes),
    path('Signup/',views.SignUp),
    path('Login/',views.Login)
]
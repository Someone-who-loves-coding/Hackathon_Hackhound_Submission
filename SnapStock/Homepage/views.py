from django.shortcuts import render,HttpResponse

def Home(request):
    return HttpResponse("Hello World")


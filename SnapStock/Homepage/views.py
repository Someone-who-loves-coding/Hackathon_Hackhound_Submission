from django.shortcuts import render

def Index(request):
    return render(request,'Index.html')

def Home(request):
    return render(request,'Home.html')

def Recipes(request):
    context = {
        'Element': 'Value'
    }
    return render(request,'Recipes.html')

def Signup(request):
    return render(request,'Signup.html')


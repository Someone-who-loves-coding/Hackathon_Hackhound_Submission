from django.shortcuts import render
from Homepage.models import Signup

def Index(request):
    return render(request,'Index.html')

def Home(request):
    return render(request,'Home.html')

def Recipes(request):
    context = {
        'Element': 'Value'
    }
    return render(request,'Recipes.html')

def SignUp(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        signup = Signup(Username = username, Password = password)
        signup.save()
    return render(request,'Signup.html')


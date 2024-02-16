from django.shortcuts import render,redirect
from Homepage.models import Users,Ingredients
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def Index(request):
    return render(request,'Index.html')

def Login(request):
    if request.method == "POST":
        username_ = request.POST.get('Username')
        password_ = request.POST.get('Password')
        user = authenticate(username = username_, password = password_)
        if user is not None:
            redirect("/Signup")
        else :
            return render(request,'Login.html')
    return render(request,'Login.html')

def Home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Expiry_date = request.POST.get('expiry_date')
        ingredients = Ingredients(Title = title, Date=Expiry_date)
        ingredients.save()
        Tingredients = Ingredients.objects.all()
    return render(request,'Home.html', {'ingredients': Tingredients})

def Recipes(request):
    context = {
        'Element': 'Value'
    }
    return render(request,'Recipes.html')

def SignUp(request):
    if request.method == "POST":
        username_ = request.POST.get('Username')
        password_ = request.POST.get('Password')
        # signup = Users(Username = username_, Password = password_)
        user = User.objects.create_user(username = username_, password = password_)
        user.save()
        # signup.save()
    return render(request,'Signup.html')


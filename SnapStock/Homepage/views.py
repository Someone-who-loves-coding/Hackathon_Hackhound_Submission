from django.shortcuts import render
from Homepage.models import Signup,Ingredients
from django.contrib.messages import constants as messages

def Index(request):
    return render(request,'Index.html')

def Home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Expiry_date = request.POST.get('expiry_date')
        ingredients = Ingredients(Title = title, Date=Expiry_date)
        ingredients.save()
    ingredients = Ingredients.objects.all()
    ans = []
    for item in ingredients:
        ans.append({"title":item.Title, "date":item.Date})
    print("ing : ", ans)
    return render(request,'Home.html', {'ingredients': ans})

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
        messages.success(request, "Successful Signup")
    return render(request,'Signup.html')


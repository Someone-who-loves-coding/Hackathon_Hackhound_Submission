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
    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
    return render(request,'Signup.html')


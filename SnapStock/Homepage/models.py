from django.db import models

class Signup(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class Ingredients(models.Model):
    Title = models.CharField(max_length=50)
    Date = models.DateField()


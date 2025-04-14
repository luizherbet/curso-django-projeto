from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='recipes/covers/%Y/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

#class User(models.Model):

    
# Create your models here.

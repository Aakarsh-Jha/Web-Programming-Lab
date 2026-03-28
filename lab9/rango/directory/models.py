from django.db import models

# Create your models here.
from django.db import models
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=128)
    visits = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'visits', 'likes']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'title', 'url', 'views']
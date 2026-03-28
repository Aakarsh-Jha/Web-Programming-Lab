from django.urls import path
from workapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert_work, name='insert_work'),
    path('search/', views.search, name='search'),
]
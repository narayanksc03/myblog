from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('demo/',views.demoIndex, name="demo"),

]

# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo, name="demo"),
    path('register/',views.register,name="user.register"),
    path('edit/<int:id/', views.user_edit, name="user.edit"),
    path('show/<int:id>/',views.user_show,name="user.views"),
    path('login/',views.user_login,name="user.login"),

]
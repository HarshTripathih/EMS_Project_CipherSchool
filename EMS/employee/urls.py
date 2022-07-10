from django.contrib import admin
from django.urls import path, include
from employee import views
urlpatterns = [
    path("", views.index, name='home'),
    path("createdepartment", views.createdep, name='create department'),
    path("viewdepartment", views.viewdep, name='view department'),
    path("createrole", views.createrole, name='create role'),
    path("viewrole", views.viewrole, name='view role'),
    path("viewuser", views.viewuser, name='view user'),
    path("createuser", views.createuser, name='create user'),
    path("viewpermission", views.viewpermission, name='view permission'),
    path("editadmin", views.editadmin, name='edit admin'),
    path("editsupervisor", views.editsupervisor, name='edit supervisor'),
    path("createpermission", views.createpermission, name='create permission'),
    path("approveleave", views.approveleave, name='approve leave'),
    path("createleave", views.createleave, name='create leave'),
    path("showleave", views.showleave, name='show leave'),
    path("viewnotice", views.viewnotice, name='view notice'),
    path("viewnotice2", views.viewnotice2, name='view notice2'),
    path("login", views.login, name='login'),
    path("createnotice", views.createnotice, name='create notice'),
    path("mail", views.mail, name='mail'),

]

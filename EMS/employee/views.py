from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from employee.models import CreateLeaveInfo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login


# Create your views here.

def index(request):
    return render (request, 'index.html')

def createdep(request):
 return render(request, 'create-department.html')

def viewdep(request):
    return render (request, 'view-department.html')

def createrole(request):
    return render (request, 'create_role.html')

def viewrole(request):
    return render (request, 'view_role.html')

def viewuser(request):
    return render (request, 'view_user.html')

def createuser(request):
    return render (request, 'create_user.html')

def viewpermission(request):
    return render (request, 'view_permission.html')

def editadmin(request):
    return render (request, 'edit-admin.html')

def editsupervisor(request):
    return render (request, 'edit-supervisor.html')

def createpermission(request):
    return render (request, 'create_permission.html')

def approveleave(request):
    return render (request, 'approve-leave.html')

def createleave(request):

    if request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        leavefrom = request.POST.get('leave_from')
        leavetill = request.POST.get('leave_till')
        leavetype = request.POST.get('leave_type')
        leavedesc = request.POST.get('leave_desc')
        print(leavetype,leavetill,leavefrom,leavedesc)
        leavedata = CreateLeaveInfo(leavefrom=leavefrom,leavetill=leavetill,leavetype=leavetype,leavedesc=leavedesc)
        leavedata.save()
    return render (request, 'create_leave.html')


def viewnotice(request):
    return render (request, 'view-notice.html')

def viewnotice2(request):
    return render (request, 'view-notice2.html')

def createnotice(request):
    return render (request, 'create-notice.html')

def mail(request):
    return render (request, 'mail.html')

def createrole(request):
    return render (request, 'create_role.html')

def login(request):
    return render (request, 'login.html')


def showleave(request):
    return render (request, 'show_leave.html')




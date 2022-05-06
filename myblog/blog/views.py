from contextvars import Context
from django.shortcuts import render
from blog.forms import UserRegisterForm
from blog.models import AppUser
def demo(request):
    urf = UserRegisterForm
    template = 'user/create.html'
    context = {'form':urf,}
    return render(request,template,context)

def register(request):
    if request.method =="POST":
        user = AppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.contact = request.POST.get('contact')
        user.password = request.POST.get('password')
        urf = UserRegisterForm
        template = 'users/create.html'
        context = {
            'form':urf,
            'msg':'Registered Sucessfully',
            'user':user
        }
        user.save()
        return render(request,template,context)       
        
    else:
        
        urf = UserRegisterForm
        template = 'users/create.html'
        context = {'form': urf, 'msg': 'Create'}
        return render(request,template,context)
def user_show(request,id):
    return render(request)

def user_edit(request,id):
    return render(request)

def user_login(request,id):
    return render(request)
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from .forms import registerform, todoform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import Group
from .models import Todos
from . import signals


def home(request):
    signals.notification.send(sender=None,request=request,user=['kanani','kanani'])
    return HttpResponse('custom signals created')



# User authenticate area............
def register(request):
    if request.method == 'POST':
        fm = registerform(request.POST)
        if fm.is_valid():
            messages.success(request, 'account created')
            user = fm.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
    else:
        fm = registerform()
    return render(request, 'register.html', {'form': fm})


def loggin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login user  !!!!!')
                    return HttpResponseRedirect('/index/')

        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/index/')


def loggout(request):
    logout(request)
    return HttpResponseRedirect('/loggin/')


# change pwd with old passoword
def change_pwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = PasswordChangeForm(user=request.user, data=request.POST)
            if f.is_valid():
                f.save()
                update_session_auth_hash(request, f.user)
                messages.success(request, 'password change success.')
                return HttpResponseRedirect('/index/')
        else:
            f = PasswordChangeForm(user=request.user)
        return render(request, 'password.html', {'form': f})
    else:
        return HttpResponseRedirect('/loggin/')


#
# # change pwd without old pwd
# def change_pwd1(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             f = SetPasswordForm(user=request.user, data=request.POST)
#             if f.is_valid():
#                 f.save()
#                 update_session_auth_hash(request, f.user)
#                 messages.success(request, 'password change success.')
#                 return HttpResponseRedirect('/index/')
#         else:
#             f = SetPasswordForm(user=request.user)
#         return render(request, 'password1.html', {'form': f})
#     else:
#         return HttpResponseRedirect('/loggin/')
#


######### COOKIE area....................

def setcookie(request):
    response = render(request, 'setcookie.html')
    response.set_signed_cookie('name', 'raj', salt='nm', expires=datetime.utcnow() + timedelta(days=2))
    # response.set_cookie('name', 'raj', expires=datetime.utcnow()+timedelta(days=2))
    # response.set_cookie('name', 'raj', max_age=60)
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', 'guest-user')
    name = request.get_signed_cookie('name', default='unknown', salt='nm')
    return render(request, 'getcookie.html', {'name': name})


def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response


# Session area ....
def setsession(request):
    request.session['name'] = 'raj'
    request.session['lname'] = 'patel'
    request.session.set_expiry(500)
    return render(request, 'setsession.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', 'unknown')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '21')
    return render(request, 'getsession.html', {'name': name, 'lname': lname,
                                               'keys': keys, 'items': items})


def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')


def index(request):
    if request.user.is_authenticated:
        t = Todos.objects.all()
        user = request.user

        gps = user.groups.all()
        return render(request, 'index.html', {'name': request.user, 't': t, 'gps': gps})
    else:
        return HttpResponseRedirect('/loggin/')


# user details...............
def todo(request):
    if request.method == "POST":
        blog = todoform(request.POST)
        if blog.is_valid():
            print(blog)
            blog.save()
            return redirect('/todo_detail/')

    else:
        blog = todoform()
        return render(request, 'todo.html', {'blog': blog})


def todo_detail(request):
    td = Todos.objects.all()
    return render(request, 'todo_detail.html', {'td': td})


def edit(request, id):
    st = Todos.objects.get(id=id)
    return render(request, 'edit.html', {'st': st})


def update(request, id):
    st = Todos.objects.get(id=id)
    form = todoform(request.POST, instance=st)
    if form.is_valid():
        form.save()
        return redirect('/todo_detail/')
    return render(request, 'edit.html', {'st': st})


def delete(request, id):
    s = Todos.objects.get(pk=id)
    s.delete()
    return redirect('/todo_detail/')

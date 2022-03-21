from . import views
from django.urls import path

app_name = "todoapp"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('setcookie/', views.setcookie, name='setcookie'),
    path('setsession/', views.setsession, name='setsession'),
    path('getcookie/', views.getcookie, name='getcookie'),
    path('getsession/', views.getsession, name='getsession'),
    path('delcookie/', views.delcookie, name='delcookie'),
    path('delsession/', views.delsession, name='delsession'),
    path('todo/', views.todo, name='todo'),
    path('todo_detail/', views.todo_detail),
    path('edit/<int:id>/', views.edit),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('register/', views.register, name='register'),
    path('loggin/', views.loggin, name='loggin'),
    path('loggout/', views.loggout, name='loggout'),
    path('change_pwd/', views.change_pwd, name='change_pwd'),
    # path('change_pwd1/', views.change_pwd1, name='change_pwd1'),

]

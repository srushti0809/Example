from django.contrib import admin
from django.urls import path, include
from myapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('liststudent', views.liststudent, name='liststudent'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('listcourse', views.listcourse, name='listcourse'),
    path('addresult', views.addresult, name='addresult'),
    path('listresult', views.listresult, name='listresult'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
]
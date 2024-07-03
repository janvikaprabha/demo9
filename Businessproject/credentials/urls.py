from django.contrib import admin
from .import views
from django.urls import path


from businessproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form', views.form, name='form'),
    path('logout', views.logout, name='logout'),
    path('about',views.about,name='about'),



]
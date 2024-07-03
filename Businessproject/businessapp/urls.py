from django.urls import path
from .import views
app_name='businessapp'


urlpatterns = [
    path('index/', views.index, name='index'),

    path('department/',views.department, name='department'),
    path('<slug:d_slug>/', views.Departments, name='products_by_department'),
    path('<slug:d_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
    path('cse', views.cse, name='cse'),
    path('ice', views.ice, name='ice'),
    path('eee', views.eee, name='eee'),

    path('mechanical', views.mechanical, name='mechanical'),
    path('ece', views.ece, name='ece'),
    path('civil', views.civil, name='civil'),






]

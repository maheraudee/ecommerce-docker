from django.urls import path

from . import views
app_name = 'cafe'

urlpatterns = [
    # path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('special_dishes/', views.special_dishes, name='special_dishes'),
    path('team/', views.team, name='team'),
    path('menu/', views.menu, name='menu'),
    path('', views.home, name='home'),

]
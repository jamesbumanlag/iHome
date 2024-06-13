
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('reset', views.reset, name='reset'),
    path('navbar', views.navbar, name='navbar'),
    path('logout_user', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('residents', views.residents, name='residents'),
    path('add_res', views.add_res, name='add_res')

]
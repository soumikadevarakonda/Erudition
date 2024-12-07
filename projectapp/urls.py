from django.urls import path
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('registerpagelogic/', views.registerpagelogic, name='registerpagelogic'),
    path('loginpagelogic/', views.loginpagelogic, name='loginpagelogic'),
    path('registerpagecall/', views.registerpagecall, name='registerpagecall'),
    path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
    path('logout/', views.logout, name='logout'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('elibrary/', views.elibrary, name='elibrary'),
    path('authentication/', views.authentication, name='authentication'),
    path('digital/', views.digital, name='digital'),
]

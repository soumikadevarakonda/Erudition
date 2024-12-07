from django.urls import path, include
from . import views

app_name = 'userapp'

urlpatterns = [
    path('userhomepage/', views.userhomepage, name='userhomepage'),
]
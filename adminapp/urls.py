from django.urls import path, include
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('adminhomepage/', views.adminhomepage, name='adminhomepage'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('catalog_management/', views.catalog_management, name='catalog_management'),
    path('view_reports/', views.view_reports, name='view_reports'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
]
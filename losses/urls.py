"""Определяет схемы URL для losses."""
 
from django.urls import path
from . import views
 
app_name = 'losses'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # diagrams
    path('diagrams/', views.diagrams, name='diagrams'),
    # months diagram
    path('diagrams/<int:header_id>/', views.header, name='header'),
]
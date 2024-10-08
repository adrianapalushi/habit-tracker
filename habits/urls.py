from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('habit/new/', views.habit_create, name='habit_create'),
    path('habit/edit/<int:pk>/', views.habit_edit, name='habit_edit'),
    path('habit/delete/<int:pk>/', views.habit_delete, name='habit_delete'),
]

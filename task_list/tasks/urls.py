from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<task_id>/', views.edit, name="edit"),
    path('delete/<task_id>/', views.delete, name="delete"),
]
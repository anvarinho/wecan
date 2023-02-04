from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/<str:pk>', views.getTask),
    path('login/', views.loginView.as_view()),
    path('register/', views.registerView.as_view()),
]

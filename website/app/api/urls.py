from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'account', views.UserViewSet)
router.register(r'task', views.TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('categories/', views.getCategories),
    path('subcategories/', views.getSubcategories),
    path('tasks/', views.getTasks),
    path('register/', views.registerView.as_view()),
]

# urlpatterns = [
#     path('', views.getRoutes),
#     path('tasks/', views.getTasks),
#     path('tasks/<str:pk>', views.getTask),
#     path('login/', views.loginView.as_view()),
#     path('register/', views.registerView.as_view()),
# ]

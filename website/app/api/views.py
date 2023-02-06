from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.shortcuts import render
from .serializers import TaskSerializer, SubcategorySerializer, CategorySerializer
from django.http.response import JsonResponse
from app.models import Task, User, Category, Subcategory
from rest_framework import status
from django.db.models import Count
from django.db.models import Count
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer, CreateUserSerializer
import jwt
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST'])
def getCategories(request):
    if request.method == 'GET':
        regions = Category.objects.all()
        serializer = CategorySerializer(regions, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def getSubcategories(request):
    if request.method == 'GET':
        regions = Subcategory.objects.all()
        serializer = SubcategorySerializer(regions, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/tasks',
        'GET /api/tasks/:id',
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getTasks(request):
    if request.method == 'GET':
        regions = Task.objects.order_by('-created')
        serializer = TaskSerializer(regions, many=True)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     form = RegionForm(data=request.data)
    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse(form.data, status=status.HTTP_201_CREATED) 
    #     return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

class registerView(GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            key='JWT_SECRET_KEY'
            auth_token = jwt.encode ({'user':"payload"}, key, algorithm="HS256")
            serializer = UserSerializer(user)
            data={'user':serializer.data, 'token':auth_token}
            return Response(data, status=status.HTTP_200_OK)
            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

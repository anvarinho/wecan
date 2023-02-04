from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import TaskSerializer
from django.http.response import JsonResponse
from app.models import Task
from rest_framework import status
from django.db.models import Count
# Create your views here.

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

# @api_view(['GET', 'POST'])
# def image_list(request):
#     """
#     Get list of data or create new ones
#     """
#     if request.method == 'GET':
#         images = ImageModel.objects.all()
#         message = request.query_params.get('message', None)
#         if message is not None:
#             images = images.filter(message__icontains=message)
#         serializer = ImageSerializer(images, many=True)
#         return JsonResponse(serializer.data, safe=False)
 
#     elif request.method == 'POST':
#         form = ImageForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return JsonResponse(form.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def image_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         image = ImageModel.objects.get(pk=pk)
#     except ImageModel.DoesNotExist:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ImageSerializer(image)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ImageSerializer(image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         image.delete()
#         return JsonResponse(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST', 'PUT'])
# def getRoutes(request):
#     routes = [
#         'GET /api',
#         'GET /api/tasks',
#         'GET /api/tasks/:id',
#         # 'GET /api/tours',
#         # 'GET /api/tours/:id',
#     ]
#     return Response(routes)

# @api_view(['GET'])
# def getPlaces(request):
#     rooms=Place.objects.all().annotate(q_places=Count('places')).order_by('-q_places')
#     q = request.query_params.get('q', None)
#     if q is not None:
#         rooms = rooms.filter(name__icontains=q)
#     serializer = PlaceSerializer(rooms, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getPlace(request, pk):
#     room=Place.objects.get(id=pk)
#     serializer = PlaceSerializer(room, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getTours(request):
#     rooms=Tour.objects.all()
#     serializer = TourSerializer(rooms, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getTour(request, pk):
#     room=Tour.objects.get(id=pk)
#     serializer = TourSerializer(room, many=False)
#     return Response(serializer.data)
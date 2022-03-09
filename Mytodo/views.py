from crypt import methods
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class TodoList(ModelViewSet):
    queryset  = Todo.objects.all()
    serializer_class = TodoSerializer

    
    
    





# Viewset 

# from functools import partial
# from urllib import response
# from .serializers import TodoSerializer
# from .models import Todo
# from rest_framework.response import Response
# from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
# from rest_framework import status

# class TodoList(viewsets.ViewSet):
#     # get the todo list
#     def list(self,request):
#         queryset = Todo.objects.all()
#         serializer = TodoSerializer(queryset,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     # Create the todo item
#     def create(self,request):
#         serializer = TodoSerializer(data = request.data)
#         # check the validation
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response("Insertion failed !",status=status.HTTP_400_BAD_REQUEST)

#     # update the todo item
#     def update(self,request,pk=None):
#         queryset = Todo.objects.all()
#         # Will find the object correponds to pk if not found then retun error
#         data = get_object_or_404(queryset,pk=pk)
#         serializer = TodoSerializer(data,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response("Updation failed !",status=status.HTTP_400_BAD_REQUEST) 

#     # retrive the todo item
#     def retrive(self,request,pk=None):
#         queryset = Todo.objects.all()
#         data = get_object_or_404(queryset,pk=pk)
#         serializer = TodoSerializer(data)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     #delete the todo item
#     def delete(self,request,pk):
#         queryset = Todo.objects.all()
#         data = get_object_or_404(queryset,pk=pk)
#         data.delete()
#         return Response('Data Deleted successfully',status=status.HTTP_200_OK)
        


   

























# from .serializers import TodoSerializer
# from .models import Todo
# from rest_framework import generics
# from rest_framework.response import Response

# # For List the todo item and create the new todo item
# class TodoList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# # For Retrive the todo item, update and destroy todo item
# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer







# from functools import partial
# from django.http import Http404
# from .serializers import TodoSerializer
# from .models import Todo
# from rest_framework.views import APIView
# from rest_framework.response import Response



# class TodoList(APIView):

# # get the list 
#    def get(self,reqest):
#       # get the queryset
#       data = Todo.objects.all()
#       # complex datatype to python dict data type
#       serializer = TodoSerializer(data,many=True)
#       return Response(serializer.data)

# # To create the list
#    def post(self,request):
#       serializer = TodoSerializer(data=request.data)
#       # check the validation of serialization and save it
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       return Response(serializer.errors)

# class TodoDetail(APIView):
# #  To get the perticular model object from the db, if found then return, else not found
#    def get_object(self,pk):
#       try:
#          return Todo.objects.get(pk=pk)
#       except Todo.DoesNotExist:
#          return Http404

# # Retrive the Todo item
#    def get(self,request,pk):
#       try:
#          data = self.get_object(pk)
#          serializer = TodoSerializer(data)
#          return Response(serializer.data)
#       except:
#          return Response('Object not exists')
 
# #  Update the todo item
#    def put(self,request,pk):
#       data = self.get_object(pk)
#       serializer = TodoSerializer(data,data=request.data,partial=True)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data)
#       return Response(serializer.errors)

# # Delete the todo item
#    def delete(self,request,pk):
#       try:
#          data = self.get_object(pk)
#          # Delete the object
#          data.delete()
#          return Response('Data deleted successfullly !')
#       except:
#          return Response('object not found')













































































#  import json
# from django.http import HttpResponse
# from .serializers import TodoSerializer
# from .models import Todo
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import io




# @csrf_exempt
# def getTodoData(request):
#    # For listing todo list
#    if request.method == 'GET':
#       # Will fech All the data from database
#       queryset = Todo.objects.all()
      
#       # complex datatype to python data type
#       serializer = TodoSerializer(queryset,many=True)

#       # python datatype to json
#       json_data = JSONRenderer().render(serializer.data)
#       # will return http response
#       return HttpResponse(json_data,content_type='application/json')

# # for creating todo list
#    elif request.method == 'POST':
#       # convert json to python data type
#       data = JSONParser().parse(request)

#       # deserializaed data
#       serializer = TodoSerializer(data=data)

#       # check validation and saved the data in db and return json response
#       if serializer.is_valid():
#          serializer.save()
#          return JsonResponse(serializer.data, status=201)
#       return JsonResponse(serializer.errors, status=400)
      
#       # For updating Todo list
#    elif request.method == 'PUT':
#       # keep the bytes in memory buffer
#       streams = io.BytesIO(request.body)

#       # convert json to python data type
#       pydata = JSONParser().parse(streams)

#       # Get the id from the data user has sent and get model object respective to that id
#       id = pydata.get('id')
#       data = Todo.objects.get(id=id)

#       serializer = TodoSerializer(data,data=pydata,partial=True)
#       if serializer.is_valid():
#          serializer.save()
#          return JsonResponse(serializer.data, status=201)
#       return JsonResponse(serializer.errors, status=400) 

# # For deleting the Todo list
#    elif request.method == 'DELETE':
#       streams = io.BytesIO(request.body)
#       pydata = JSONParser().parse(streams)
#       id = pydata.get('id')
#       data = Todo.objects.get(id=id)

#       # Delete the data which has id
#       data.delete()
#       return HttpResponse('Data Deleted Successfully')


# @csrf_exempt
# # For Retriving
# def getTodoDetail(request):
#    if request.method == 'POST':
#       # keep the bytes in memory buffer
#       streams = io.BytesIO(request.body)

#       # convert json to python data type
#       pydata = JSONParser().parse(streams)

#       # Get the id from the data user has sent and get model object respective to that id
#       id = pydata.get('id')
#       data = Todo.objects.get(id=id)
#       serializers = TodoSerializer(data)

#       json_data = JSONRenderer().render(serializers.data)
#       print('**Data ',data)
#       return HttpResponse(json_data,content_type = 'application/json')

   



     



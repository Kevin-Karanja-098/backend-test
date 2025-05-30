# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import viewsets, permissions
# from .serializers import *
# from rest_framework.response import Response
# from .models import *


# # def home(request): 
# #     return HttpResponse("This is the homepage")
# class ProjectManagerViewset(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]
#     queryset = ProjectManager.objects.all()
#     serializer_class = ProjectManagerSerializer

#     def list(self, request):
#         queryset = ProjectManager.objects.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)
    
# class EmployeesViewset(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]
#     queryset = Employees.objects.all()
#     serializer_class = EmployeesSerializer

#     def list(self, request):
#         queryset = Employees.objects.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)


# class ProjectViewset(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     def list(self, request):
#         queryset = Project.objects.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data)
#         else: 
#             return Response(serializer.errors, status=400)

#     def retrieve(self, request, pk=None):
#         project = self.queryset.get(pk=pk)
#         serializer = self.serializer_class(project)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         project = self.queryset.get(pk=pk)
#         serializer = self.serializer_class(project,data=request.data)
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data)
#         else: 
#             return Response(serializer.errors, status=400)

#     def destroy(self, request, pk=None):
#         project = self.queryset.get(pk=pk)
#         project.delete()
#         return Response(status=204)
        
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import *
from .models import *

# Optional homepage view
# def home(request): 
#     return HttpResponse("This is the homepage")

# Project Manager List & Create View
class ProjectManagerListCreateView(generics.ListCreateAPIView):
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer
    permission_classes = [permissions.AllowAny]

# Employees List & Create View
class EmployeesListCreateView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [permissions.AllowAny]

# Project List & Create View
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

# Project Retrieve, Update, and Delete View
class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]





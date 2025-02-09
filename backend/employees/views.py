from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeListSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from .utils.filters import EmployeeFilter
from .utils.pagination import CustomPageNumberPagination

@api_view(['GET', 'PUT'])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def employee_create(request):
    try:
        data = request.POST.dict()
        data.pop('cv', None)  
        data.pop('photo', None)  
        data.pop('id_document', None)  
        
        if 'photo' in request.FILES:
            data['photo'] = request.FILES['photo']
        if 'cv' in request.FILES:
            data['cv'] = request.FILES['cv']
        if 'id_document' in request.FILES:
            data['id_document'] = request.FILES['id_document']

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Error:", str(e))  
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['first_name', 'last_name', 'email', 'department', 'job_title']
    ordering_fields = ['first_name', 'last_name', 'department', 'job_title', 'salary', 'start_date']
    ordering = ['last_name', 'first_name']

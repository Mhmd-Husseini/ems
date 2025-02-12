from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, parser_classes, action
from rest_framework.response import Response
from .models import Employee, Timesheet
from .serializers import EmployeeSerializer, EmployeeListSerializer, TimesheetSerializer, TimesheetListSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
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

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing employee information
    """
    queryset = Employee.objects.all()
    pagination_class = CustomPageNumberPagination
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['first_name', 'last_name', 'email', 'department', 'job_title']
    ordering_fields = ['first_name', 'last_name', 'department', 'job_title', 'salary', 'start_date']
    ordering = ['last_name', 'first_name']

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeListSerializer
        return EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()

            if 'photo' in data and not request.FILES.get('photo'):
                data.pop('photo')
            if 'cv' in data and not request.FILES.get('cv'):
                data.pop('cv')
            if 'id_document' in data and not request.FILES.get('id_document'):
                data.pop('id_document')

            if 'photo' in request.FILES:
                data['photo'] = request.FILES['photo']
            if 'cv' in request.FILES:
                data['cv'] = request.FILES['cv']
            if 'id_document' in request.FILES:
                data['id_document'] = request.FILES['id_document']

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED, 
                headers=headers
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            
            if 'photo' in data and not request.FILES.get('photo'):
                data.pop('photo')
            if 'cv' in data and not request.FILES.get('cv'):
                data.pop('cv')
            if 'id_document' in data and not request.FILES.get('id_document'):
                data.pop('id_document')

            if 'photo' in request.FILES:
                data['photo'] = request.FILES['photo']
            if 'cv' in request.FILES:
                data['cv'] = request.FILES['cv']
            if 'id_document' in request.FILES:
                data['id_document'] = request.FILES['id_document']

            instance = self.get_object()
            serializer = self.get_serializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'])
    def options(self, request):
        """Return employee options for dropdowns"""
        employees = self.get_queryset().values('id', 'first_name', 'last_name')
        data = [{
            'value': emp['id'],
            'label': f"{emp['first_name']} {emp['last_name']}"
        } for emp in employees]
        return Response(data)

class TimesheetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing timesheet information
    """
    queryset = Timesheet.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['employee']
    search_fields = ['employee__first_name', 'employee__last_name', 'summary']
    ordering_fields = ['start_time', 'end_time', 'employee__last_name']
    ordering = ['-start_time']

    def get_serializer_class(self):
        if self.action == 'list':
            return TimesheetListSerializer
        return TimesheetSerializer

    @action(detail=False, methods=['get'])
    def by_employee(self, request):
        """Get timesheets for a specific employee"""
        employee_id = request.query_params.get('employee_id')
        if not employee_id:
            return Response(
                {'error': 'employee_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        timesheets = self.get_queryset().filter(employee_id=employee_id)
        serializer = self.get_serializer(timesheets, many=True)
        return Response(serializer.data)

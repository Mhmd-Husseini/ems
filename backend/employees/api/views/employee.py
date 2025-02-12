from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ...models.employee import Employee
from ..serializers.employee import EmployeeSerializer, EmployeeListSerializer
from ...utils.filters import EmployeeFilter
from ...utils.pagination import CustomPageNumberPagination

class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing employee information"""
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
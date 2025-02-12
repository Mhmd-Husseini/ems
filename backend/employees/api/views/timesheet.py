from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ...models.timesheet import Timesheet
from ..serializers.timesheet import TimesheetSerializer, TimesheetListSerializer
from ...utils.pagination import CustomPageNumberPagination

class TimesheetViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing timesheet information"""
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
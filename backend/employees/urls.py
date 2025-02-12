from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views.employee import EmployeeViewSet
from .api.views.timesheet import TimesheetViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'timesheets', TimesheetViewSet)

app_name = 'employees'

urlpatterns = [
    path('', include(router.urls)),
] 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'timesheets', views.TimesheetViewSet)

app_name = 'employees'

urlpatterns = [
    path('', include(router.urls)),
] 
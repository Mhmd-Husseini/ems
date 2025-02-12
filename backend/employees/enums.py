from django.db import models

class Department(models.TextChoices):
    IT = 'IT', 'Information Technology'
    HR = 'HR', 'Human Resources'
    FINANCE = 'FINANCE', 'Finance'
    MARKETING = 'MARKETING', 'Marketing'
    SALES = 'SALES', 'Sales'
    OPERATIONS = 'OPERATIONS', 'Operations'
    LEGAL = 'LEGAL', 'Legal'

class JobPosition(models.TextChoices):
    DEVELOPER = 'DEVELOPER', 'Developer'
    MANAGER = 'MANAGER', 'Manager'
    ANALYST = 'ANALYST', 'Analyst'
    DESIGNER = 'DESIGNER', 'Designer'
    COORDINATOR = 'COORDINATOR', 'Coordinator'
    SPECIALIST = 'SPECIALIST', 'Specialist'
    DIRECTOR = 'DIRECTOR', 'Director'
    CONSULTANT = 'CONSULTANT', 'Consultant' 
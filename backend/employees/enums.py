from django.db import models

class Department(models.TextChoices):
    ENGINEERING = 'ENGINEERING', 'Engineering'
    MARKETING = 'MARKETING', 'Marketing'
    SALES = 'SALES', 'Sales'
    HR = 'HR', 'Human Resources'
    FINANCE = 'FINANCE', 'Finance'
    IT = 'IT', 'Information Technology'

class JobPosition(models.TextChoices):
    SENIOR_DEVELOPER = 'SENIOR_DEVELOPER', 'Senior Developer'
    JUNIOR_DEVELOPER = 'JUNIOR_DEVELOPER', 'Junior Developer'
    MARKETING_MANAGER = 'MARKETING_MANAGER', 'Marketing Manager'
    SALES_REPRESENTATIVE = 'SALES_REPRESENTATIVE', 'Sales Representative'
    HR_MANAGER = 'HR_MANAGER', 'HR Manager'
    FINANCE_ANALYST = 'FINANCE_ANALYST', 'Finance Analyst'
    PROJECT_MANAGER = 'PROJECT_MANAGER', 'Project Manager' 
from django_filters import rest_framework as filters
from django.db.models import Q
from typing import List, Dict, Any, Optional
from functools import reduce
import operator

class DynamicFilterSet(filters.FilterSet):
    """
    A base filter set that provides dynamic filtering capabilities.
    Supports complex queries, related fields, and custom lookups.
    """
    
    def __init__(self, *args, **kwargs):
        self.related_fields = getattr(self.Meta, 'related_fields', {})
        self.search_fields = getattr(self.Meta, 'search_fields', [])
        super().__init__(*args, **kwargs)

    @staticmethod
    def build_query(
        search_term: str, 
        fields: List[str], 
        lookup_expr: str = 'icontains'
    ) -> Q:
        """
        Builds a Q object for searching across multiple fields
        """
        return reduce(
            operator.or_,
            (Q(**{f'{field}__{lookup_expr}': search_term}) for field in fields)
        )

    def filter_search(self, queryset, name, value):
        """
        Performs a search across specified fields
        """
        if not value:
            return queryset
        
        q_objects = self.build_query(value, self.search_fields)
        return queryset.filter(q_objects)

    def filter_related(self, queryset, name, value):
        """
        Filters by related field values
        """
        if not value or name not in self.related_fields:
            return queryset
            
        field_config = self.related_fields[name]
        lookup = field_config.get('lookup', 'exact')
        relation = field_config.get('relation')
        field = field_config.get('field')
        
        if not relation or not field:
            return queryset
            
        filter_kwargs = {f'{relation}__{field}__{lookup}': value}
        return queryset.filter(**filter_kwargs)

class EmployeeFilter(DynamicFilterSet):
    """
    Filter set for Employee model with advanced filtering capabilities
    """
    search = filters.CharFilter(method='filter_search')
    name = filters.CharFilter(method='filter_name')
    department = filters.CharFilter(lookup_expr='icontains')
    job_title = filters.CharFilter(lookup_expr='icontains')
    min_salary = filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary', lookup_expr='lte')
    start_date_after = filters.DateFilter(field_name='start_date', lookup_expr='gte')
    start_date_before = filters.DateFilter(field_name='start_date', lookup_expr='lte')
    
    class Meta:
        model = None  
        fields = ['department', 'job_title']
        search_fields = [
            'first_name',
            'last_name',
            'email',
            'department',
            'job_title'
        ]

    def filter_name(self, queryset, name, value):
        """Custom filter for name searching"""
        if not value:
            return queryset
        
        parts = value.split()
        q_objects = Q()
        
        for part in parts:
            q_objects |= (
                Q(first_name__icontains=part) |
                Q(last_name__icontains=part)
            )
            
        return queryset.filter(q_objects)

# Example usage of a more specific filter
class AdvancedEmployeeFilter(DynamicFilterSet):
    """
    Example of a more complex filter implementation
    """
    department_id = filters.NumberFilter(field_name='department__id')
    salary_range = filters.CharFilter(method='filter_salary_range')
    experience = filters.NumberFilter(method='filter_experience')
    skills = filters.CharFilter(method='filter_related')

    class Meta:
        model = None  # We'll set this dynamically
        fields = ['department', 'job_title']
        search_fields = [
            'first_name',
            'last_name',
            'email',
            'department__name',
            'job_title'
        ]
        related_fields = {
            'skills': {
                'relation': 'employeeskills',
                'field': 'skill__name',
                'lookup': 'icontains'
            },
            'department': {
                'relation': 'department',
                'field': 'name',
                'lookup': 'icontains'
            }
        }

    def filter_salary_range(self, queryset, name, value):
        """
        Filter by salary range in format 'min-max'
        """
        if not value:
            return queryset
            
        try:
            min_salary, max_salary = map(float, value.split('-'))
            return queryset.filter(salary__gte=min_salary, salary__lte=max_salary)
        except (ValueError, TypeError):
            return queryset

    def filter_experience(self, queryset, name, value):
        """
        Filter by years of experience based on start_date
        """
        if not value:
            return queryset
            
        from django.utils import timezone
        from dateutil.relativedelta import relativedelta
        
        date_threshold = timezone.now().date() - relativedelta(years=int(value))
        return queryset.filter(start_date__lte=date_threshold)

def create_dynamic_filter(
    model: Any,
    search_fields: List[str],
    related_fields: Optional[Dict] = None,
    additional_filters: Optional[Dict] = None
) -> type:
    """
    Factory function to create dynamic filter sets
    
    Usage:
    MyModelFilter = create_dynamic_filter(
        model=MyModel,
        search_fields=['name', 'description'],
        related_fields={
            'category': {
                'relation': 'category',
                'field': 'name',
                'lookup': 'icontains'
            }
        },
        additional_filters={
            'status': ['exact'],
            'created_at': ['gte', 'lte']
        }
    )
    """
    meta_attrs = {
        'model': model,
        'search_fields': search_fields,
        'related_fields': related_fields or {}
    }
    
    filter_attrs = {
        'search': filters.CharFilter(method='filter_search'),
        'Meta': type('Meta', (), meta_attrs)
    }

    if additional_filters:
        for field, lookups in additional_filters.items():
            for lookup in lookups:
                filter_name = f'{field}__{lookup}' if lookup != 'exact' else field
                filter_attrs[filter_name] = filters.Filter(
                    field_name=field,
                    lookup_expr=lookup
                )

    return type(
        f'{model.__name__}Filter',
        (DynamicFilterSet,),
        filter_attrs
    ) 
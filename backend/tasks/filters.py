import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter()
    priority = django_filters.ChoiceFilter(choices=Task.PRIORITY_CHOICES)
    category = django_filters.NumberFilter(field_name='category__id')
    due_date_from = django_filters.DateTimeFilter(field_name='due_date', lookup_expr='gte')
    due_date_to = django_filters.DateTimeFilter(field_name='due_date', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['completed', 'priority', 'category', 'due_date_from', 'due_date_to']
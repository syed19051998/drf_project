import django_filters
from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name="designation", lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name="emp_name", lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')   # this is for primary key i'd but goal is to filter the E001... emp i'd
    id_min = django_filters.CharFilter(method = 'filter_by_id_range',label= 'from EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='to EMP ID')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        if name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset 
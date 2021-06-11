import django_filters
from .models import Parks
from django_filters import CharFilter
class ParkFilter(django_filters.FilterSet):
  name = CharFilter(field_name='name', lookup_expr='icontains')
  description = CharFilter(field_name='description', lookup_expr='icontains')
  class Meta:
    model = Parks
    fields = 'name','description'
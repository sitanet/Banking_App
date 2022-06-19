from cProfile import label
import django_filters
from django_filters import CharFilter
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
     name = CharFilter(label='Name:', lookup_expr='icontains')
     phone_no = CharFilter(label='Phone No:',lookup_expr='icontains')
     cust_no = CharFilter(label='Account No:',lookup_expr='icontains')

   
   

     class Meta:
        model = Customer
        fields = ['name','phone_no', 'cust_no',]
     
from django.contrib import admin
from finance_lens_app.models import coa
from company.models import Company

# Register your models here.
from .models import Customer


admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(coa)

from datetime import datetime
from logging import PlaceHolder
from msilib.schema import Control
from operator import concat
from tkinter import Widget
from turtle import numinput
from xml.dom.minidom import Attr
from django import forms

from company.models import Company

from .models import Customer
from finance_lens_app.models import coa

from django.forms import ModelChoiceField
from django.forms.widgets import NumberInput, EmailInput
from django.contrib.admin.widgets import AdminDateWidget, AdminEmailInputWidget
from django.forms.fields import DateField, EmailField



class DateInput(forms.DateInput):
    input_type = 'date'


class customers(forms.ModelForm):
    # specify the name of model to use
    
    photo = forms.ImageField()
    sign = forms.ImageField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    SEX = (
    ("M", "Male"),
    ("F", "Female"),
)
    MARITAL_STATUS = (
    ("S", "SINGLE"),
    ("M", "MARRIED"),
    ("D", "DIVOICED"),
)
    MODE_OF_IDENTIFICATION = (
    ("Voters card", "Voters card"),
    ("National identification", "National identification"),
    ("Drivers License", "Drivers License"),
)
  
 

    cust_sex = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=SEX))
    dobirth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    br_code = forms.ModelChoiceField(queryset = Company.objects.all(),initial = 0, widget=forms.Select(attrs={'class': 'form-control'}))
    acc_cat = forms.ModelChoiceField(queryset = coa.objects.all(),initial = 0, widget=forms.Select(attrs={'class': 'form-control'}))
    res_address=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Resident Address:',max_length=10)
    off_address=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Office Address:',max_length=10)
    phone_no=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'phone'}))
    mar_status = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=MARITAL_STATUS))
    mode_of_id = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=MODE_OF_IDENTIFICATION))

    RELIGION = (
    ("Christian", "Christian"),
    ("Muslim", "Muslim"),
    ("Others", "Others"),
)
    religion=forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=RELIGION))
  
  
    
  
    id_no=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    state_of_oringin=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    local_govt_origin=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    nationality=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    local_govt_res=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    state_of_res=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    email_add=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))

    
    tin_no=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    mother_mai_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    place_of_birth=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    ref_no=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    
    ocuppation=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
    landmark=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=20)
      

    
    class Meta:
        model = Customer
        fields = ('photo',
            'sign',
            'cust_sex',
            'name',
            'br_code',
            'acc_cat',
            'dobirth',
            'mar_status',
            'religion',
            'mode_of_id',
            'res_address',
            'off_address',
            'phone_no',
            'id_no',
            'ref_no',
            'place_of_birth',
            'mother_mai_name',
            'tin_no',
            'state_of_oringin',
            'local_govt_origin',
            'nationality',
            'local_govt_res',
            'state_of_res',
            'email_add',
            'ocuppation',
            'city',
            'landmark',)


    

       
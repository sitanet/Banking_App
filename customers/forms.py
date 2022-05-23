
from logging import PlaceHolder
from django import forms

from .models import Customer



class DateInput(forms.DateInput):
    input_type = 'date'


class customers(forms.ModelForm):
    # specify the name of model to use
    
    
  
    dobirth=forms.DateField(label='Date of Birth', widget=DateInput)
    
    city=forms.CharField(label='City:',max_length=10)
    
  
    landmark=forms.CharField(label='Nearest Bus-Stop:',max_length=20)
    
 

    
    class Meta:
        model = Customer
        fields = "__all__"

        labels = {
            "photo": "Passport:",
            "sign": "Signature:",
            "name": "Full Name:",
            "br_code": "Branch Code:",
            "acc_cat": "Type of Account:",
            "cust_sex": "Gender:",
            "mar_status": "Marital Status:",
            "religion": "Religion:",
            "mode_of_id": "Mode of Identification:",
            "res_address": "Residential Address:",
            "off_address": "Office Address:",
            "phone_no": "Phone No:",
            "id_no": "Identification No:",
            "ref_no": "Reference No:",
            "place_of_birth": "Place of Birth:",
            "mother_mai_name": "Mother Maiden Name:",
            "tin_no": "TIN No:",
            "state_of_oringin": "State of Origin:",
            "local_govt_origin": "Local Government Origin:",
            "local_govt_res": "Local Government Resident:",
            "state_of_res": "State of Resident:",
            "email_add": "Email Address:",
            "ocuppation": "Occupation:",
            
        }
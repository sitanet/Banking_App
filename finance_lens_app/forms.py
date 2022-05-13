from aifc import Aifc_read
from cProfile import label
import imp
from django import forms
from .models import Acct_type, acct_head, coa


class Acct_type_form(forms.ModelForm):
    acct_type_name=forms.CharField(required=True,widget=forms.widgets.Input(attrs={"placeholder":"Enter Account Type","class": "",}),
            label=""
    )
    
    
    class Meta:
        model= Acct_type
        fields =('acct_type_name','Aid')

class Acct_head_form(forms.ModelForm):
    head_name=forms.CharField(required=True,widget=forms.widgets.Input(attrs={"placeholder":"Enter Account Type","class": "",}),
            label=""
    )
    class Meta:
        model= acct_head
        fields =('head_name','gl_no','Aid',)



class coa_form_cat(forms.ModelForm):
    ac_name=forms.CharField(required=True,widget=forms.widgets.Input(attrs={"placeholder":"Enter Account Type","class": "",}),
            label=""
    )
    
    class Meta:
        model= coa
        fields =('gl_no',)










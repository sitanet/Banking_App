from statistics import mode
from django.db import models



class Acct_type(models.Model):
    Aid=models.AutoField(primary_key=True)
    acct_type_name=models.CharField(max_length=200, unique=True)
    class Meta:
        
        db_table="Acct_Type"
        


class acct_head(models.Model):
    id=models.AutoField(primary_key=True)
    Aid=models.IntegerField()
    head_name=models.CharField(max_length=200, unique=True)
    gl_no=models.IntegerField(unique=True)
    
    class Meta:
        
        db_table="acct_head"


class coa(models.Model):
    id=models.AutoField(primary_key=True)
    gl_no=models.IntegerField(unique=True)
    ac_name=models.CharField(max_length=200, unique=True)
    ac_type=models.IntegerField()
    ac_head=models.CharField(max_length=200)
    currcy=models.CharField(max_length=200)
    
    class Meta:
        
        db_table="coa"

    def __str__(self): 
        return str(self.ac_name)
   
        




  


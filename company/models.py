from django.db import models


# Create your models here.

BR_CODE = (
    ("1", "YBA"),
    
)



class Company(models.Model):
    id=models.AutoField(primary_key=True)
    br_code=models.CharField(choices = BR_CODE,  max_length=50)
    br_name=models.CharField(max_length=150,)
    br_address=models.CharField(max_length=100)
    reg_no=models.IntegerField()
    br_ses_date=models.DateField()
    reg_date=models.DateField()
    admin_name=models.CharField(max_length=50)
    
    def __str__(self): 
        return self.br_name
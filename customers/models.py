from django.db import models
from company.models import Company
from finance_lens_app.models import coa






MARITAL_STATUS = (
    ("S", "Single"),
    ("M", "Married"),
    ("D", "Divoice"),
)


MODE_OF_IDENTIFICATION = (
    ("Voters card", "Voters card"),
    ("National identification", "National identification"),
    ("Drivers License", "Drivers License"),
)
RELIGION = (
    ("Christian", "Christian"),
    ("Muslim", "Muslim"),
    ("Others", "Others"),
)

RELIGION = (
    ("Christian", "Christian"),
    ("Muslim", "Muslim"),
    ("Others", "Others"),
)

# Create your models here.
class Customer(models.Model):
    photo=models.ImageField(upload_to='photos/')
    sign=models.ImageField(upload_to='signs/')
    br_code=models.ForeignKey(Company, on_delete=models.CASCADE)
    acc_cat=models.ForeignKey(coa, on_delete=models.CASCADE, max_length=10)
    cust_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, unique=True)
    dobirth=models.DateField()
    cust_sex=models.CharField(default = 'Male', max_length=5)
    res_address=models.TextField(max_length=200)
    phone_no=models.CharField(max_length=16)
    mar_status=models.CharField(choices = MARITAL_STATUS, default = 'Single',  max_length=10)
    mode_of_id=models.CharField(choices = MODE_OF_IDENTIFICATION,  max_length=50)
    id_no=models.CharField(max_length=100)
    ref_no=models.IntegerField()
    place_of_birth=models.CharField(max_length=100)
    mother_mai_name=models.CharField(max_length=100)
    religion=models.CharField(choices=RELIGION, default='Christian',  max_length=10)
    tin_no=models.CharField(max_length=50)
    state_of_oringin=models.CharField(max_length=20)
    local_govt_origin=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20)
    off_address=models.TextField(max_length=200)
    city=models.CharField(max_length=10)
    local_govt_res=models.CharField(max_length=20)
    state_of_res=models.CharField(max_length=20)
    landmark=models.CharField(max_length=20)
    email_add=models.EmailField(max_length=30)
    ocuppation=models.CharField(max_length=20)





    def __str__(self): 
        return self.name
    




    



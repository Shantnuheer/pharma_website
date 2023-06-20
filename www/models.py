from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class fromula(models.Model):
    Product_name=models.CharField(max_length=25)
    CAT_NO= models.CharField(max_length=40)
    Chemical_name= models.CharField(max_length=100)
    Molecular_Formula= models.CharField(max_length=40)
    Molecular_Weight= models.IntegerField()
    CAS_Number= models.CharField(max_length=40)
    Solubility= models.CharField(max_length=40)
    Storage= models.CharField(max_length=40)
    Keywords= models.CharField(max_length=40)
    Purity_by_HPLC= models.CharField(max_length=40)
    Inventory_status= models.CharField(max_length=40)
    image= CloudinaryField('image')


    # Contact form

class contact(models.Model):
    Name= models.CharField(max_length=20)
    Email= models.EmailField()
    Phone= models.IntegerField()
    Message= models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.Name

weight= (
    ('MG','MG'),
    ('G','G'),
    ('KG','KG'),
)
class request_for_quote(models.Model):
    product=models.CharField(max_length=50)
    name= models.CharField(max_length=25)
    email= models.EmailField()
    company=models.CharField(max_length=50)
    contact=models.IntegerField()
    package=models.CharField(max_length=70)
    weight= models.CharField(max_length=100,choices=weight,default='MG')


class cart(models.Model):
    Product_name= models.CharField(max_length=500)
    quantity= models.IntegerField()
    user= models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.Product_name
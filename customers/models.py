from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone
from django.core.validators import MinValueValidator
# Create your models here.

BUSINESS_CATEGORIES = (
    ('FinTech','FinTech'),
    ('Learning Institute','Learning Institute'),
    ('Transportation', 'Transportation'),
    ('Service','Service'),
    ('Banking','Banking'),
    ("other","other"),
) 

class Customers(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return  f"{self.name} "
    



class Business(models.Model):
    business_name = models.CharField(max_length=100)
    registration_date = models.DateField()
    location = models.CharField(max_length=50, null=True)
    location_sub_county = models.CharField(max_length=100,null=True)
    location_ward = models.CharField(max_length=100,null=True)
    location_building_name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=50, choices=BUSINESS_CATEGORIES)
    age = models.IntegerField(null =True,validators=[MinValueValidator(0)]) # type: ignore
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def calculate_business_age(self):
        today = datetime.now().date()  # Get the current date
        age = today.year - self.registration_date.year
        return age

    def save(self):
        if self.registration_date and not self.age:
            self.age = self.calculate_business_age()
        super().save()

    """
     @property
    def business_age(self):
        self.age = self.calculate_business_age()
        super().save(force_insert=True)
    
        
    def calculate_business_age(self):
        today = datetime.date.now()
        age = today - self.registration_date
        return age.days // 365  # Calculate years of operation
    """
   
    
    
    

    def __str__(self):
        return f"{self.business_name} | {self.owner}"

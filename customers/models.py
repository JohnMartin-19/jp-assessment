from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone
# Create your models here.

BUSINESS_CATEGORIES = (
    ('FinTech','FinTech'),
    ('Learning Institute','Learning Institute'),
    ('Transportation', 'Transportation'),
    ('Service','Service'),
    ('Banking','Banking'),
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
    category = models.CharField(max_length=50, choices=BUSINESS_CATEGORIES)
    age = models.IntegerField(null =True) # type: ignore
    owner = models.ForeignKey(Customers, on_delete=models.CASCADE)
    
    def business_age(self):
        today = datetime.now().date()
        age = today.year - self.registration_date.year - ((today.month, today.day) < (self.registration_date.month, self.registration_date.day))
        return age

    @property
    def save(self):
        self.age = self.business_age()
        super().save()


    def __str__(self):
        return f"{self.business_name} | {self.owner}"

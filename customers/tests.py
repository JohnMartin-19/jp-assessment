from django.test import TestCase
from .models import Customers,Business
from datetime import datetime
# Create your tests here.

class  CustomerTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customers.objects.create( email='john@gmail.com')
        cls.customer = Customers.objects.get(id=1)

    def test_Customer_creation(self):
        """Testing the creation of a customer"""

        customer=Customers.objects.get(id=1 )
        expected_object_name = f'{customer.email}'
        self.assertEqual(expected_object_name, 'john@gmail.com')




class BusinessTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Run only once per class initialization.
         Business.objects.create( business_name='Tours and Travels')
         cls.business = Business.objects.get(id=1)

    def test_Business_creation(self):
        

        biz=Business.objects.get(id=1 )
        expected_object_name = f'{biz.business_name}'
        self.assertEqual(expected_object_name, 'Tours and Travels')

    
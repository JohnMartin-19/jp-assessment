from django.shortcuts import render
from rest_framework import viewsets,generics
from  .models import Business,Customers
from .serializers import BusinessSerializer,CustomerSerializer,getBusinessSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomerList(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class  GetBusiness(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = getBusinessSerializer
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
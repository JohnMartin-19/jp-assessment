from rest_framework import serializers

from .models import Customers,Business
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields=('id','name','date_of_birth','email', 'phone','nationality')

class  BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registration_date', 'owner','location','category','owner')

class getBusinessSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer()
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registration_date','location','category', 'owner')
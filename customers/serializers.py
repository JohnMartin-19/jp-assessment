from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Customers,Business
from accounts.models import  CustomUser
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields=('id','name','date_of_birth','email', 'phone','nationality')

class  BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registration_date','age', 'owner','location','location_building_name','category','owner')

class getBusinessSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer()
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registration_date','location','category','owner')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, CustomUser):
        token = super().get_token(CustomUser)
        token['username'] = CustomUser.username

        return token
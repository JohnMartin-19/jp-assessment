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
        fields = ('id', 'business_name','registration_date', 'age','location','location_building_name','category','customer')

    def create(self, validated_data):
        business = Business(**validated_data)
        business.save()
        return business
class getBusinessSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registration_date','location','category','customer',"age")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, CustomUser):
        token = super().get_token(CustomUser)
        token['username'] = CustomUser.username

        return token
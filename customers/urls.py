from  django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomerList,CustomerDetail,BusinessList,BusinessDetail,GetBusiness,MyTokenObtainPairView
urlpatterns = [
    path('customers/<int:pk>/', CustomerDetail.as_view(),name = 'customer_detail'),
    path('customers/', CustomerList.as_view(), name ='customer_list'),
    path('business/<int:pk>/', BusinessDetail.as_view(),name = 'business_detail'),
    path('business/', BusinessList.as_view(),name ='business_list'),
    #api endpoint for getting jwt token
    path('token/',MyTokenObtainPairView.as_view(),name="TokenObtainPair"),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh'),

    #api endpoint to retreive all the business details(nested)
    #'GET' method allowed only
    path('all_business/', GetBusiness.as_view(), name = 'Nested Business Details'), #for getting all businesses in the system

]
from  django.urls import path
from .views import CustomerList,CustomerDetail,BusinessList,BusinessDetail

urlpatterns = [
    path('<int:pk>/', CustomerDetail.as_view(),name = 'customer_detail'),
    path('', CustomerList.as_view( name ='customer_list')),
    path('<int:pk>/', BusinessDetail.as_view(),name = 'business_detail'),
    path('', BusinessList.as_view( name ='business_list')),

]
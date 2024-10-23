from django.urls import path
from . import views

urlpatterns = [
    path('property/', views.property_list, name='property_list'),
    path('tenant/<int:pk>/', views.tenant_detail, name='tenant_detail'),
]

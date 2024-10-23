from django.urls import path
from .views import (
    PropertyListView, PropertyCreateView, PropertyUpdateView, PropertyDeleteView,
    TenantListView, TenantCreateView, TenantUpdateView, TenantDeleteView,
    ContractListView, ContractCreateView, ContractUpdateView, ContractDeleteView,
    PaymentListView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView
)

urlpatterns = [
    path('properties/', PropertyListView.as_view(), name='property_list'),
    path('properties/add/', PropertyCreateView.as_view(), name='property_add'),
    path('properties/<int:pk>/edit/', PropertyUpdateView.as_view(), name='property_edit'),
    path('properties/<int:pk>/delete/', PropertyDeleteView.as_view(), name='property_delete'),

    path('tenants/', TenantListView.as_view(), name='tenant_list'),
    path('tenants/add/', TenantCreateView.as_view(), name='tenant_add'),
    path('tenants/<int:pk>/edit/', TenantUpdateView.as_view(), name='tenant_edit'),
    path('tenants/<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),

    path('contracts/', ContractListView.as_view(), name='contract_list'),
    path('contracts/add/', ContractCreateView.as_view(), name='contract_add'),
    path('contracts/<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),

    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/add/', PaymentCreateView.as_view(), name='payment_add'),
    path('payments/<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment_edit'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),
]
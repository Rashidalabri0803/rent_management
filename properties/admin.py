from django.contrib import admin
from .models import Property, Tenant, Contract, Payment
# Register your models here.
admin.site.site_header = "لوحة إدارة الأيجارات"
admin.site.site_title = "نظام إدارة الإيجارات"
admin.site.index_title = "مرحبا بك في لوحة الإدارة"
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display =('name', 'address', 'created_at', 'update_at')
    search_fields = ('name', 'address')
    list_filter =('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields':('name', 'address', 'description')
        }),
        ('تواريخ', {
        'fields':('created_at', 'update_at'),
        'classes':('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'update_at')
@admin.register(Tenant)    
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_filter =('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields':('first_name', 'last_name', 'phone', 'email')
        }),
        ('تواريخ', {
        'fields':('created_at',),
        'classes':('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
    
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'start_date', 'end_date', 'monthly_rent')
    search_fields = ('property__name', 'tenant__first_name', 'tenant__last_name')
    list_filter =('start_date', 'end_date')
    ordering = ('-start_date',)
    fieldsets = (
        (None, {
            'fields':('property', 'tenant', 'start_date', 'end_date', 'monthly_rent')
        }),
        ('تواريخ', {
        'fields':('created_at',),
        'classes':('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
    
    def is_expired(self, obj):
        return obj.is_expired()
    is_expired.boolean = True
    is_expired.short_description = 'منتهي'

@admin.register(Payment)        
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('contract', 'payment_date', 'amount', 'is_late')
    search_fields = ('contract__property_name', 'contract__tenant__first_name', 'contract__tenant__last_name')
    list_filter =('payment_date', 'is_late')
    ordering = ('-payment_date',)
    fieldsets = (
        (None, {
            'fields':('contract', 'payment_date', 'amount', 'is_late')
        }),
        ('تواريخ', {
        'fields':('created_at',),
        'classes':('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
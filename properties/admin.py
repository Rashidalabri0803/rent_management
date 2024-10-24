from django.contrib import admin
from .models import Property, Tenant, Contract, Payment, PropertyAttachment, MaintenanceEvent

admin.site.site_header = "لوحة إدارة الأيجارات"
admin.site.site_title = "نظام إدارة الإيجارات"
admin.site.index_title = "مرحبا بك في لوحة الإدارة"

class PropertyAttahcmentInline(admin.TabularInline):
    model = PropertyAttachment
    extra = 1
    verbose_name = "مرفق"
    verbose_name_plural = "مرفقات العقار"

class MainteanceEventInline(admin.TabularInline):
    model = MaintenanceEvent
    extra = 1
    verbose_name = "صيانة"
    verbose_name_plural = "صيانات العقار"
    
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display =('name', 'property_type', 'address', 'available', 'created_at')
    list_filter =('property_type', 'available')
    search_fields = ('name', 'address')
    inlines = [PropertyAttahcmentInline, MainteanceEventInline]
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields':('name', 'property_type', 'num_rooms', 'available', 'description')
        }),
        ('معلومات إضافية', {
        'fields':('created_at',),
        'classes':('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
    
@admin.register(Tenant)    
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'id_number')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'id_number')
    
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'start_date', 'end_date', 'monthly_rent', 'is_active')
    list_filter =('is_active', 'start_date', 'end_date')
    search_fields = ('property__name', 'tenant__first_name', 'tenant__last_name')
    fieldsets = (
        (None, {
            'fields':('property', 'tenant', 'start_date', 'end_date', 'monthly_rent', 'deposit', 'is_active')
        }),
        ('ملاحظات العقد', {
        'fields':('notes',),
        'classes':('collapse',),
        }),
    )

@admin.register(Payment)        
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('contract', 'payment_date', 'amount', 'is_late')
    list_filter =('payment_date', 'is_late')
    search_fields = ('contract__property_name', 'contract__tenant__first_name', 'contract__tenant__last_name')
    ordering = ('-payment_date',)
    fieldsets = (
        (None, {
            'fields':('contract', 'payment_date', 'amount', 'is_late')
        }),
        ('ملاحظات الدفع', {
        'fields':('notes',),
        'classes':('collapse',),
        }),
    )

@admin.register(PropertyAttachment)
class PropertyAttachmentAdmin(admin.ModelAdmin):
    list_display = ('property', 'file', 'description')
    search_fields = ('property__name',)

@admin.register(MaintenanceEvent)
class MaintenanceEventAdmin(admin.ModelAdmin):
    list_display = ('property', 'event_date', 'cost', 'resolved')
    list_filter =('event_date', 'resolved')
    search_fields = ('property__name', 'description')
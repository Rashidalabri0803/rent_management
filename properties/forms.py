from django import forms
from .models import Property, Tenant, Contract, Payment, PropertyAttachment, MaintenanceEvent
from django.utils.translation import gettext_lazy as _
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'address', 'property_type', 'num_rooms', 'available', 'description')
        labels = {
            'name': _('اسم العقار'),
            'address': _('عنوان العقار'),
            'property_type': _('نوع العقار'),
            'num_rooms': _('عدد الغرف'),
            'available': _('متاح'),
            'description': _('وصف العقار'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'أدخل وصف العقار'}),
        }
        
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('first_name', 'last_name', 'phone', 'email', 'address', 'id_number')
        labels = {
            'first_name': _('الاسم الاول'),
            'last_name': _('الاسم الاخير'),
            'phone': _('رقم الهاتف'),
            'email': _('البريد الالكتروني'),
            'address': _('عنوان المستأجر'),
            'id_number': _('رقم الهوية'),
        }
        widgets = {
            'address': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'أدخل عنوان المستأجر'}),
        }
        
class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('property', 'tenant', 'start_date', 'end_date', 'monthly_rent', 'deposit', 'notes', 'is_active')
        labels = {
            'property': _('العقار'),
            'tenant': _('المستأجر'),
            'start_date': _('تاريخ البدء'),
            'end_date': _('تاريخ النهاية'),
            'monthly_rent': _('الإيجار الشهري'),
            'deposit': _('التأمين'),
            'notes': _('ملاحظات العقد'),
            'is_active': _('العقد نشط'),
        }
        widgets = {
            'notes': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'أدخل ملاحظات العقد'}),
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date': forms.DateInput(attrs={'type':'date'}),
        }
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model= Payment
        fields = ('contract', 'payment_date', 'amount', 'is_late', 'notes')
        labels = {
            'contract': _('العقد'),
            'payment_date': _('تاريخ الدفع'),
            'amount': _('المبلغ'),
            'is_late': _('هل تأخرت الدفعة؟'),
            'notes': _('ملاحظات الدفع'),
        }
        widgets = {
            'payment_date': forms.DateInput(attrs={'type':'date'}),
            'notes': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'أدخل ملاحظات الدفع'}),
        }

class MantenanceEventForm(forms.ModelForm):
    class Meta:
        model = MaintenanceEvent
        fields = ['property', 'description', 'event_date', 'cost', 'resolved']
        labels = {
            'property': _('العقار'),
            'description': _('وصف الصيانة'),
            'event_date': _('تاريخ الصيانة')
            'cost': _('التكلفة الصيانة'),
            'resolved': _('تم المعالجة'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'أدخل وصف الصيانة'}),
            'event_date': forms.DateInput(attrs={'type':'date'}),
        }
class PropertySearchForm(forms.Form):
    name = forms.CharField(label=_('اسم العقار'), required=False, widget=forms.TextInput(attrs={'placeholder':'ابحث عن العقار'}))
    address = forms.CharField(label=_('عنوان العقار'), required=False)
    property_type = forms.Choices(choices=[('', 'أختر نوع العقار')] + Property.PROPERTY_TYPES, required=False, label='نوع العقار')
    available = forms.BooleanField(label=_('متاح'), required=False)

class TenantSearchForm(forms.Form):
    first_name = forms.CharField(label=_('الاسم الاول'), required=False, widget=forms.TextInput(attrs={'placeholder':'ابحث عن المستأجر'}))
    last_name = forms.CharField(label=_('الاسم الاخير'), required=False, widget=forms.TextInput(attrs={'placeholder':'ابحث عن المستأجر'}))
    phone = forms.CharField(label=_('رقم الهاتف'), required=False, widget=forms.TextInput(attrs={'placeholder':'ابحث عن المستأجر'}))
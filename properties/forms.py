from django import forms
from .models import Property, Tenant, Contract, Payment
from django.utils.translation import gettext_lazy as _
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'description']
        labels = {
            'name':_('اسم العقار'),
            'address':_('العنوان'),
            'description':_('الوصف'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'أدخل اسم العقار'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'أدخل العنوان'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'أدخل وصفاً'}),
        }
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['first_name', 'last_name', 'phone', 'email']
        labels = {
            'first_name':_('الاسم الأول'),
            'last_name':_('الاسم الأخير'),
            'phone':_('رقم الهاتف'),
            'email':_('البريد الإلكتروني'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الاسم الأول'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'الاسم الأخير'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'أدخل رقم الهاتف'}),
            'email': forms.EmailField(attrs={'class':'form-control', 'placeholder':'أدخل البريد الإلكتروني'}),
        }
        
class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['property', 'tenant', 'start_date', 'end_date', 'monthly_rent']
        labels = {
            'property': _('العقار'),
            'tenant':_('المستأجر'),
            'start_date':_('تاريخ البدء'),
            'end_date':_('تاريخ الانتهاء'),
            'monthly_rent':_('الإيجار الشهري')
        }
        widgets = {
            'property': forms.Select(attrs={'class':'form-control'}),
            'tenant': forms.Select(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'monthly_rent'L forms.NumberInput(attrs={'class':'form-control', 'placeholder':'أدخل مبلغ الإيجار'}),
        }
class PaymentForm(forms.ModelForm):
    class Meta:
        model= Payment
        fields = ['contract', 'payment_date', 'amount', 'is_late']
        labels = {
            'contract':_('العقد'),
            'payment_date':_('تاريخ الدفع'),
            'amount':_('المبلغ'),
            'is_late':_('متأخر'),
        }
        widgets = {
            'contract': forms.Select(attrs={'class':'form-control'}),
            'payment_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'amount': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'أدخل المبلغ'}),
            'is_late': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
        
class PropertySearchForm(forms.Form):
    query = forms.CharField(
        label=_('بحث عن عقار'), 
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'أدخل اسم العقار للبحث'}))
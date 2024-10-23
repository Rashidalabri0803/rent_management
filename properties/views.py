from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Property, Tenant, Contract, Payment
from .forms import PropertyForm, TenantForm, ContractForm, PaymentForm, PropertySearchForm
from django.contrib import messages
# Create your views here.

class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Property.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PropertySearchForm(self.request.GET or None)
        return context

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        messages.success(self.request, 'تم إضافة العقار بنجاح')
        return super().form_valid(form)

class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم تحديث العقار بنجاح')
        return super().form_valid(form)

class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'property_confirm_delete.html'
    success_url = reverse_lazy('property_list')

    def delete(self, request, *args, **kwargs):
        messages.sucess(self.request, 'تم حذف العقار بنجاح')
        return super().delete(request, *args, **kwargs)

class TenantListView(ListView):
    model = Tenant
    template_name = 'tenant_list.html'
    context_object_name = 'tenants'
    paginate_by = 10

class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant_form.html'
    success_url = reverse_lazy('tenant_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم إضافة المستأجر بنجاح')
        return super().form_valid(form)

class TenantUpdateView(UpdateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant_form.html'
    success_url = reverse_lazy('tenant_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم تحديث المستأجر بنجاح')
        return super().form_valid(form)

class TenantDeleteView(DeleteView):
    model = Tenant
    template_name = 'tenant_confirm_delete.html'
    success_url = reverse_lazy('tenant_list')

    def delete(self, request, *args, **kwargs):
        messages.sucess(self.request, 'تم حذف المستأجر بنجاح')
        return super().delete(request, *args, **kwargs)

class ContractListView(ListView):
    model = Contract
    template_name = 'contract_list.html'
    context_object_name = 'contracts'
    paginate_by = 10

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract_form.html'
    success_url = reverse_lazy('contract_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم إضافة العقد بنجاح')
        return super().form_valid(form)

class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract_form.html'
    success_url = reverse_lazy('contract_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم تحديث العقد بنجاح')
        return super().form_valid(form)

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contract_confirm_delete.html'
    success_url = reverse_lazy('contract_list')

    def delete(self, request, *args, **kwargs):
        messages.sucess(self.request, 'تم حذف العقد بنجاح')
        return super().delete(request, *args, **kwargs)

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'
    context_object_name = 'payments'
    paginate_by = 10

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم إضافة الدفعة بنجاح')
        return super().form_valid(form)

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

    def form_valid(self, form):
        messages.sucess(self.request, 'تم تحديث الدفعة بنجاح')
        return super().form_valid(form)

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')
    def delete(self, request, *args, **kwargs):
        messages.sucess(self.request, 'تم حذف الدفعة بنجاح')
        return super().delete(request, *args, **kwargs)
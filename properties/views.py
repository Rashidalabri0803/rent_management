from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Property, Tenant, Contract, Payment, MaintenanceEvent
from .forms import PropertyForm, TenantForm, ContractForm, PaymentForm, MantenanceEventForm, PropertySearchForm, TenantSearchForm
# Create your views here.

class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Property.objects.all()
        name = self.request.GET.get('name', '')
        property_type = self.request.GET.get('property_type', '')
        available = self.request.GET.get('available', '')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if property_type:
            queryset = queryset.filter(property_type=property_type)
        if available:
            queryset = queryset.filter(available=True)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PropertySearchForm(self.request.GET)
        return context

class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        messages.success(self.request, "تم إضافة العقار بنجاح!")
        return super().form_valid(form)

class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث العقار بنجاح")
        return super().form_valid(form)

class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'property_confirm_delete.html'
    success_url = reverse_lazy('property_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "تم حذف العقار بنجاح")
        return super().delete(request, *args, **kwargs)

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

class TenantListView(ListView):
    model = Tenant
    template_name = 'tenant_list.html'
    context_object_name = 'tenants'
    paginate_by = 10

    def get_queryset(self):
        queryset = Tenant.objects.all()
        first_name = self.request.GET.get('first_name', '')
        last_name = self.request.GET.get('last_name', '')
        phone = self.request.GET.get('phone', '')

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        if phone:
            queryset = queryset.filter(phone__icontains=phone)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TenantSearchForm(self.request.GET)
        return context

class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant_form.html'
    success_url = reverse_lazy('tenant_list')

    def form_valid(self, form):
        messages.success(self.request, "تم إضافة المستأجر بنجاح")
        return super().form_valid(form)

class TenantUpdateView(UpdateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant_form.html'
    success_url = reverse_lazy('tenant_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث المستأجر بنجاح")
        return super().form_valid(form)

class TenantDeleteView(DeleteView):
    model = Tenant
    template_name = 'tenant_confirm_delete.html'
    success_url = reverse_lazy('tenant_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "تم حذف المستأجر بنجاح")
        return super().delete(request, *args, **kwargs)

class TenantDetailView(DetailView):
    model = Tenant
    template_name = 'tenant_detail.html'
    context_object_name = 'tenant'

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
        messages.success(self.request, "تم إضافة العقد بنجاح")
        return super().form_valid(form)

class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract_form.html'
    success_url = reverse_lazy('contract_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث العقد بنجاح")
        return super().form_valid(form)

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contract_confirm_delete.html'
    success_url = reverse_lazy('contract_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "تم حذف العقد بنجاح")
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
        messages.success(self.request, "تم إضافة الدفعة بنجاح")
        return super().form_valid(form)

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث الدفعة بنجاح")
        return super().form_valid(form)

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "تم حذف الدفعة بنجاح")
        return super().delete(request, *args, **kwargs)

class MaintenanceEventListView(ListView):
    model = MaintenanceEvent
    template_name = 'maintenance_event_list.html'
    context_object_name = 'maintenance_events'
    paginate_by = 10

class MaintenanceEventCreateView(CreateView):
    model = MaintenanceEvent
    form_class = MantenanceEventForm
    template_name = 'maintenance_event_form.html'
    success_url = reverse_lazy('maintenance_event_list')

    def form_valid(self, form):
        messages.success(self.request, "تم إضافة حدث الصيانة بنجاح")
        return super().form_valid(form)

class MaintenanceEventUpdateView(UpdateView):
    model = MaintenanceEvent
    form_class = MantenanceEventForm
    template_name = 'maintenance_event_form.html'
    success_url = reverse_lazy('maintenance_event_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث حدث الصيانة بنجاح")
        return super().form_valid(form)

class MaintenanceEventDeleteView(DeleteView):
    model = MaintenanceEvent
    template_name = 'maintenance_event_confirm_delete.html'
    success_url = reverse_lazy('maintenance_event_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "تم حذف حدث الصيانة بنجاح")
        return super().delete(request, *args, **kwargs)
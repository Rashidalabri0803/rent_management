from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.ggeneric import ListView, CreateView, UpdateView, DeleteView
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
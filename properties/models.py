from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField("اسم العقار", max_length=100)
    address = models.CharField("العنوان", max_length=255)
    description = models.TextField("الوصف", blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)
    update_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    
    def __str__(self):
        return self.name
        
class Tenant(models.Model):
    first_name = models.CharField("الاسم الأول", max_length=50)
    last_name = models.CharField("الاسم الأخير", max_length=50)
    phone = models.CharField("رقم الهاتف", max_length=15)
    email = models.EmailField("البريد الإلكتروني", unique=True)
    created_at = models.DateTimeField("تاريخ التسجيل", auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Contract(models.Model):
    property = models.ForeignKey(Property, verbose_name="العقار", on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, verbose_name="المستأجر", on_delete=models.CASCADE)
    start_date = models.DateField("تاريخ البدء")
    end_date = models.DateField("تاريخ الانتهاء")
    monthly_rent = models.DecimalField("الإيجار الشهري", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("تاريخ العقد", auto_now_add=True)
    
    def __str__(self):
        return f"{self.property.name} - {self.tenant.first_name}"
    
class Payment(models.Model):
    contract = models.ForeignKey(Contract, verbose_name="العقد", on_delete=models.CASCADE)
    payment_date = models.DateField("تاريخ الدفع")
    amount = models.DecimalField("المبلغ", max_digits=10, decimal_places=2)
    is_late = models.BooleanField("متأخر", default=False)
    created_at = models.DateTimeField("تاريخ التسجيل", auto_now_add=True)
    
    def __str__(self):
        return f"{self.contract} - {self.payment_date}"
        
    class Meta:
        ordering = ['-payment_date']
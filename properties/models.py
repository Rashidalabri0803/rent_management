from django.db import models
from django.utils import timezone

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'شقة'),
        ('officestation', 'مكتب'),
        ('store', 'متجر'),
    ]
    name = models.CharField(verbose_name="اسم العقار", max_length=100)
    address = models.TextField(verbose_name="العنوان")
    property_type = models.CharField(verbose_name="نوع العقار", max_length=20, choices=PROPERTY_TYPES)
    num_rooms = models.IntegerField(verbose_name="عدد الغرف")
    available = models.BooleanField(verbose_name="متاح", default=True)
    description = models.TextField(verbose_name="الوصف", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="تاريخ الإضافة", auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class Tenant(models.Model):
    first_name = models.CharField(verbose_name="الاسم الأول", max_length=50)
    last_name = models.CharField(verbose_name="الاسم الأخير", max_length=50)
    phone = models.CharField(verbose_name="رقم الهاتف", max_length=15)
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    address = models.TextField(verbose_name="العنوان المستأجر")
    id_number = models.CharField(verbose_name="رقم الهوية", max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Contract(models.Model):
    property = models.ForeignKey(Property, verbose_name="العقار", on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, verbose_name="المستأجر", on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="تاريخ البدء")
    end_date = models.DateField(verbose_name="تاريخ الانتهاء")
    monthly_rent = models.DecimalField(verbose_name="الإيجار الشهري", max_digits=10, decimal_places=2)
    deposit = models.DecimalField(verbose_name="التأمين", max_digits=10, decimal_places=2)
    notes = models.TextField(verbose_name="ملاحظات العقد", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="العقد نشط", default=True, null=True)
    
    def __str__(self):
        return f"عقد {self.property.name} - {self.tenant.first_name} {self.tenant.last_name}"
    
class Payment(models.Model):
    contract = models.ForeignKey(Contract, verbose_name="العقد", on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name="تاريخ الدفع")
    amount = models.DecimalField(verbose_name="المبلغ", max_digits=10, decimal_places=2)
    is_late = models.BooleanField(verbose_name="هل تأخرت الدفعة؟", default=False)
    notes = models.TextField(verbose_name="ملاحظات الدفعة", blank=True, null=True)
    
    def __str__(self):
        return f"دفعة {self.amount} __| {self.contract.tenant.first_name} {self.contract.tenant.last_name}"

class PropertyAttachment(models.Model):
    property = models.ForeignKey(Property, verbose_name="العقار", on_delete=models.CASCADE)
    file = models.FileField(verbose_name="الملف المرفق", upload_to='property_attachments/')
    description = models.TextField(verbose_name="وصف الملف", blank=True, null=True)

    def __str__(self):
        return f"مرفق __| {self.property.name}"

class MaintenanceEvent(models.Model):
    property = models.ForeignKey(Property, verbose_name="العقار", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="وصف الصيانة")
    event_date = models.DateField(verbose_name="تاريخ الصيانة", default=timezone.now)
    cost = models.DecimalField(verbose_name="التكلفة", max_digits=10, decimal_places=2)
    resolved = models.BooleanField(verbose_name="تمت المعالجة", default=False)

    def __str__(self):
        return f"صيانة {self.property.name} - {self.event_date}"
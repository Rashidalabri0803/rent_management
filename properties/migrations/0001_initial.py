# Generated by Django 5.0.3 on 2024-10-24 13:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(verbose_name='تاريخ الانتهاء')),
                ('monthly_rent', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='الإيجار الشهري')),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='التأمين')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='ملاحظات العقد')),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='العقد نشط')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم العقار')),
                ('address', models.TextField(verbose_name='العنوان')),
                ('property_type', models.CharField(choices=[('apartment', 'شقة'), ('officestation', 'مكتب'), ('store', 'متجر')], max_length=20, verbose_name='نوع العقار')),
                ('num_rooms', models.IntegerField(verbose_name='عدد الغرف')),
                ('available', models.BooleanField(default=True, verbose_name='متاح')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='الاسم الأول')),
                ('last_name', models.CharField(max_length=50, verbose_name='الاسم الأخير')),
                ('phone', models.CharField(max_length=15, verbose_name='رقم الهاتف')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الإلكتروني')),
                ('address', models.TextField(verbose_name='العنوان المستأجر')),
                ('id_number', models.CharField(max_length=20, unique=True, verbose_name='رقم الهوية')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='تاريخ الدفع')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المبلغ')),
                ('is_late', models.BooleanField(default=False, verbose_name='هل تأخرت الدفعة؟')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='ملاحظات الدفعة')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.contract', verbose_name='العقد')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='وصف الصيانة')),
                ('event_date', models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الصيانة')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='التكلفة')),
                ('resolved', models.BooleanField(default=False, verbose_name='تمت المعالجة')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property', verbose_name='العقار')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property', verbose_name='العقار'),
        ),
        migrations.CreateModel(
            name='PropertyAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='property_attachments/', verbose_name='الملف المرفق')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف الملف')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property', verbose_name='العقار')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.tenant', verbose_name='المستأجر'),
        ),
    ]

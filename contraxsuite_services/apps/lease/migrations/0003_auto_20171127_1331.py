# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0002_auto_20171127_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leasedocument',
            name='address',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='alternatives_allowed',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('YWL', 'Yes With Limitations / Restrictions')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='arbitration_forum',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='arbitration / forum'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='area_size_sq_ft',
            field=models.FloatField(blank=True, null=True, verbose_name='square ft.'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='assignment_subletting_permitted',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('YWR', 'Yes With Notice or Restrictions')], max_length=5, null=True, verbose_name='Assignment / Subletting Permitted'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='construction_allowance_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='construction_allowance_type',
            field=models.CharField(blank=True, choices=[('C', 'Cash'), ('RR', 'Rent Reduction')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='insurance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='late_fee_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='late_fee_interest_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='late fee interest rate (percent)'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='late_fee_trigger_days',
            field=models.IntegerField(blank=True, null=True, verbose_name='late fee trigger (n days)'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='late_fee_type',
            field=models.CharField(blank=True, choices=[('A', 'Amount'), ('I', 'Interest')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='lease_type',
            field=models.CharField(blank=True, choices=[('G', 'Gross'), ('N', 'Net'), ('TN', 'Triple Net')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='lessee',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='lessor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='mean_rent_per_month',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='mean_rent_per_quarter',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='mean_rent_per_year',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='period_late_fee_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='period_late_fee_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='period_rent_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='period_rent_due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='permitted_uses',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='prohibited_uses',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='property_type',
            field=models.CharField(blank=True, choices=[('O', 'Office'), ('R', 'Retail'), ('S', 'Storage')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='renew_non_renew_notice_date',
            field=models.DateField(blank=True, null=True, verbose_name='renew / non-renew notice date'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='rent_due_frequency',
            field=models.CharField(blank=True, choices=[('M', 'Monthly')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='sale_of_property_behaviour',
            field=models.TextField(blank=True, null=True, verbose_name='sale of property / do rights and obligations survive sale'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='security_deposit',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='term_duration',
            field=models.DateField(blank=True, null=True, verbose_name='term / duration'),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='termination',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leasedocument',
            name='total_rent_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-08 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0001_initial'),
        ('Transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='Buyer.customer'),
        ),
        migrations.AlterField(
            model_name='sucessfull_transaction',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Sucessful_transaction', to='Buyer.customer'),
        ),
    ]

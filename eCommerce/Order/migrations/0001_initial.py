# Generated by Django 3.2.7 on 2021-10-02 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('address_second', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.CharField(max_length=6)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('ordered_date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('placed', 'Placed'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='created', max_length=120)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.customer')),
                ('product', models.ManyToManyField(to='Order.ProductCart')),
            ],
            options={
                'ordering': ['-ordered_date'],
            },
        ),
    ]
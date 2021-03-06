# Generated by Django 3.2.7 on 2021-11-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_dimension',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]

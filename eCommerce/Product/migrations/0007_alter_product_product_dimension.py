# Generated by Django 3.2.7 on 2021-11-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_dimension',
            field=models.JSONField(blank=True, default=None),
        ),
    ]

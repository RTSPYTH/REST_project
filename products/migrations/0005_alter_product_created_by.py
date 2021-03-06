# Generated by Django 4.0 on 2021-12-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0005_alter_user_user_type'),
        ('products', '0004_alter_product_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to='authentications.user'),
        ),
    ]

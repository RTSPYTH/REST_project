# Generated by Django 4.0 on 2021-12-23 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0004_alter_user_is_active_alter_user_is_staff'),
        ('products', '0002_product_created_by_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_by', to='authentications.user'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-24 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentications', '0007_alter_profile_age_alter_profile_first_name_and_more'),
        ('products', '0005_alter_product_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('total_price', models.IntegerField()),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_by', to='authentications.user')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='products.product')),
            ],
        ),
    ]

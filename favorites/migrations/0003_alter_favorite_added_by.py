# Generated by Django 4.0 on 2021-12-24 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0006_profile'),
        ('favorites', '0002_alter_favorite_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to='authentications.user'),
        ),
    ]
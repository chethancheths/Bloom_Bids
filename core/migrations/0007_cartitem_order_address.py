# Generated by Django 4.0 on 2022-01-18 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.useraddress'),
        ),
    ]

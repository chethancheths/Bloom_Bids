# Generated by Django 4.0 on 2022-01-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_order_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='Card_no',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='Name_on_card',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='cvv',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='exp_date',
            field=models.DateField(null=True),
        ),
    ]

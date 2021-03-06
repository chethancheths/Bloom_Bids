# Generated by Django 4.0 on 2021-12-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='CartItem',
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': 'CartItems'},
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('Bs', 'BestSeller')], default='', max_length=2),
        ),
    ]

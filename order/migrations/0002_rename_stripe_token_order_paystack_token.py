# Generated by Django 4.0.3 on 2022-04-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stripe_token',
            new_name='paystack_token',
        ),
    ]

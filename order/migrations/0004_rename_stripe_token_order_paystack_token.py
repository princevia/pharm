# Generated by Django 4.0.3 on 2022-04-07 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_paystack_token_order_stripe_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stripe_token',
            new_name='paystack_token',
        ),
    ]
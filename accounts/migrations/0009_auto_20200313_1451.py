# Generated by Django 3.0.1 on 2020-03-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

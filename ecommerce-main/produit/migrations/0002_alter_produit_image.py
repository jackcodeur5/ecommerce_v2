# Generated by Django 4.0 on 2021-12-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

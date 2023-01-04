# Generated by Django 4.0 on 2022-01-07 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0004_remove_commande_livraison'),
        ('livraison', '0002_alter_livraison_prix_livraison'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraison',
            name='commande',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='commande.commande'),
            preserve_default=False,
        ),
    ]
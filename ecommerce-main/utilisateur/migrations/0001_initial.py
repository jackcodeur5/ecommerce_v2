# Generated by Django 4.0 on 2021-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.IntegerField(null=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('pass_word', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

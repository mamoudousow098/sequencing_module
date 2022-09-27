# Generated by Django 4.1.1 on 2022-09-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing_module_api', '0002_ordinateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='DossierZip',
            fields=[
                ('id_zip', models.AutoField(primary_key=True, serialize=False)),
                ('nom_dossier', models.CharField(max_length=255)),
                ('date_creation', models.DateField()),
            ],
            options={
                'db_table': 'dossierzip',
            },
        ),
        migrations.CreateModel(
            name='Echantillon',
            fields=[
                ('id_echantillon', models.AutoField(primary_key=True, serialize=False)),
                ('date_echantillon', models.DateField()),
                ('pays_origine', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'echantillon',
            },
        ),
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id_fichier', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('destinataire', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'fichier',
            },
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id_run', models.AutoField(primary_key=True, serialize=False)),
                ('date_run', models.DateField()),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'run',
            },
        ),
        migrations.AlterModelTable(
            name='ordinateur',
            table='ordinateur',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]

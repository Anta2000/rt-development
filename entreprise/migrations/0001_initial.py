# Generated by Django 4.2.1 on 2023-06-05 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('responsable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entreprise.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type_machine', models.CharField(choices=[('PC', 'PC'), ('Desktop', 'Desktop'), ('Switch', 'Switch'), ('Serveur', 'Serveur')], max_length=100)),
                ('statut', models.CharField(choices=[('Défaillant', 'Défaillant'), ('Bon état', 'Bon état'), ('En maintenance', 'En maintenance')], max_length=100)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='machine_images/')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entreprise.employe')),
            ],
        ),
        migrations.CreateModel(
            name='MiseAJour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_mise_a_jour', models.DateField(auto_now_add=True)),
                ('effectue_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.employe')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_maintenance', models.DateField()),
                ('effectuee_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.employe')),
                ('infrastructure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entreprise.infrastructure')),
            ],
        ),
    ]

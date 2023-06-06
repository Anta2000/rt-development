# Generated by Django 4.2.1 on 2023-06-05 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entreprise', '0003_remove_maintenance_infrastructure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='date_maintenance',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entreprise.machine'),
        ),
    ]
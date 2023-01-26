# Generated by Django 4.1.5 on 2023-01-25 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('praksaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='representativeId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='praksaApp.person', unique=True),
        ),
    ]
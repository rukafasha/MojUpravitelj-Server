# Generated by Django 4.1.5 on 2023-01-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praksaApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appartmentperson',
            old_name='active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='reportstatus',
            old_name='active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='active',
            new_name='isAactive',
        ),
        migrations.AddField(
            model_name='appartment',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='building',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='company',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='country',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='county',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='report',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='role',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='roleperson',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]

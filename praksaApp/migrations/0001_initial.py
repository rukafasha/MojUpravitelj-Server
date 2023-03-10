# Generated by Django 4.1.5 on 2023-01-19 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyId', models.IntegerField(primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('countryId', models.IntegerField(primary_key=True, serialize=False)),
                ('countryName', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('personId', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('dateOfBirth', models.DateField()),
                ('companyId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='praksaApp.company')),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='ReportStatus',
            fields=[
                ('reportStatusId', models.IntegerField(primary_key=True, serialize=False)),
                ('statusDescription', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'ReportStatus',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('roleId', models.IntegerField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=100)),
                ('roleDescription', models.TextField()),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('userAccountId', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'UserAccount',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.person')),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.role')),
            ],
            options={
                'db_table': 'Report',
                'unique_together': {('personId', 'roleId')},
            },
        ),
        migrations.AddField(
            model_name='person',
            name='userAccountId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.useraccount'),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('countyId', models.IntegerField(primary_key=True, serialize=False)),
                ('countyName', models.CharField(max_length=100)),
                ('countryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.country')),
            ],
            options={
                'db_table': 'County',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('personId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.person')),
                ('reportId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.report')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('buildingId', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('numberOfAppartment', models.IntegerField()),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.company')),
                ('countyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.county')),
                ('representativeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='praksaApp.person', unique=True)),
            ],
            options={
                'db_table': 'Building',
            },
        ),
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('appartmentId', models.IntegerField(primary_key=True, serialize=False)),
                ('appartmentNumber', models.IntegerField()),
                ('numberOfPeople', models.IntegerField()),
                ('buildingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.building')),
            ],
            options={
                'db_table': 'Appartment',
            },
        ),
        migrations.CreateModel(
            name='RolePerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('personId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.person')),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.role')),
            ],
            options={
                'db_table': 'RolePerson',
                'unique_together': {('personId', 'roleId')},
                'index_together': {('personId', 'roleId')},
            },
        ),
        migrations.CreateModel(
            name='AppartmentPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('appartmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.appartment')),
                ('personId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praksaApp.person')),
            ],
            options={
                'db_table': 'AppartmentPerson',
                'unique_together': {('personId', 'appartmentId')},
                'index_together': {('personId', 'appartmentId')},
            },
        ),
    ]

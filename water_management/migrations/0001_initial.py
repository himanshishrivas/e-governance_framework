# Generated by Django 2.2.6 on 2019-10-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='water_management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='larryxu', max_length=20)),
                ('first_name', models.CharField(default='Jane', max_length=20)),
                ('last_name', models.CharField(default='Doe', max_length=20)),
                ('initial', models.CharField(default='x', max_length=20)),
                ('relationToPatient', models.CharField(default='parent to children', max_length=20)),
                ('dob', models.CharField(default='now', max_length=30)),
                ('socSec', models.IntegerField(default=0)),
                ('address', models.CharField(default='main st', max_length=50)),
                ('city', models.CharField(default='columbus', max_length=20)),
                ('state', models.CharField(default='OH', max_length=20)),
                ('zip', models.CharField(default='43201', max_length=20)),
                ('homephone', models.CharField(default='6144445566', max_length=20)),
                ('cellphone', models.CharField(default='6144445566', max_length=20)),
                ('email', models.CharField(default='example@emamil.com', max_length=20)),
                ('employerName', models.CharField(default='John', max_length=20)),
                ('employerOccupation', models.CharField(default='manager', max_length=20)),
                ('employerBusAddr', models.CharField(default='main st', max_length=20)),
                ('employerBusPhone', models.CharField(default='6144445566', max_length=20)),
                ('employerBusEmail', models.CharField(default='example@email.com', max_length=20)),
                ('insurComp', models.CharField(default='franklin', max_length=20)),
                ('insurCompPhone', models.CharField(default='6144445566', max_length=20)),
                ('insurContNum', models.CharField(default='6144445566', max_length=20)),
                ('insurGroupNum', models.CharField(default='6144445566', max_length=20)),
                ('insurSubscNum', models.CharField(default='6144445566', max_length=20)),
                ('dependentName', models.CharField(default='Jane Doe', max_length=20)),
            ],
        ),
    ]

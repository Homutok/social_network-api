# Generated by Django 4.0.4 on 2022-04-30 11:30

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(db_index=True, max_length=100)),
                ('person_photo', models.ImageField(blank=True, null=True, upload_to='article')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('summary', models.CharField(db_index=True, max_length=1000, null=True)),
                ('person_gender', models.CharField(blank=True, choices=[('male', 'Мужчина'), ('female', 'Женщина'), ('other', 'Другие')], default='study', help_text='Половая принадлежность', max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ['person_name'],
            },
        ),
    ]
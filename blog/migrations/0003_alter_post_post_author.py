# Generated by Django 4.0.4 on 2022-04-30 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile'),
        ('blog', '0002_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_for_user', to='profiles.profile'),
        ),
    ]

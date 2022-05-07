# Generated by Django 4.0.4 on 2022-05-04 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_post_author_post_author_and_more'),
        ('post_comments', '0002_alter_comment_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commented_post', to='blog.post'),
        ),
    ]

# Generated by Django 3.2.16 on 2023-05-19 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blog_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='message',
        ),
    ]

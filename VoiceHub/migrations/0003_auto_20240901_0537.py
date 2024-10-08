# Generated by Django 5.1 on 2024-09-01 05:37

from django.db import migrations, models

def set_default_author(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('VoiceHub', 'Post')
    default_user = User.objects.first()  # Or use a specific user
    if default_user:
        Post.objects.filter(author__isnull=True).update(author=default_user)

class Migration(migrations.Migration):

    dependencies = [
        ('VoiceHub', '0002_post_author'),  
    ]

    operations = [
        migrations.RunPython(set_default_author),
    ]


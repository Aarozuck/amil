# Generated by Django 4.1.7 on 2024-05-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_userprofile_saved_services_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_products',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_rents',
        ),
    ]

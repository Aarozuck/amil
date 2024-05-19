# Generated by Django 4.1.7 on 2024-05-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_service_userprofile_saved_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_services',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='saved_products',
            field=models.ManyToManyField(related_name='saved_products', to='home.product'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='saved_rents',
            field=models.ManyToManyField(related_name='saved_rents', to='home.rent'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
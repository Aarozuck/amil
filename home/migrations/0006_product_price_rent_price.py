# Generated by Django 4.1.7 on 2024-05-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_subject_tutoring_tutoringcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfile', '0002_remove_fileupload_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='uploadedFile',
            field=models.FileField(upload_to='Uploaded_Files/'),
        ),
    ]

# Generated by Django 3.0 on 2019-12-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recon', '0002_auto_20191224_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='edgenode',
            name='S3_Address',
            field=models.CharField(default=222, help_text='Enter an S3 address of storage for the Edge node', max_length=2000),
            preserve_default=False,
        ),
    ]

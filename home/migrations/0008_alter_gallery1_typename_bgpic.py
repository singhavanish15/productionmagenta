# Generated by Django 4.1.1 on 2022-10-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_gallery1_typename_bgpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery1',
            name='typename_bgpic',
            field=models.ImageField(height_field=500, upload_to='', width_field=800),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muallif',
            name='tugilgan_yil',
            field=models.DateField(),
        ),
    ]

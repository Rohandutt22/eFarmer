# Generated by Django 2.1.7 on 2019-04-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eFarmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phoneNo',
            field=models.IntegerField(default=9876543210, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='typeOfUser',
            field=models.CharField(choices=[('PROFFESSOR', 'PROFFESSOR'), ('MANDI_VENDOR', 'MANDI_VENDOR'), ('FARMER', 'FARMER'), ('SHOPKEEPER', 'SHOPKEEPER')], default=3, max_length=20),
            preserve_default=False,
        ),
    ]

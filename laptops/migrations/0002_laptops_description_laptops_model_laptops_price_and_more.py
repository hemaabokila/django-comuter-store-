# Generated by Django 5.1.1 on 2024-09-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptops',
            name='description',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptops',
            name='model',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptops',
            name='price',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laptops',
            name='type',
            field=models.CharField(choices=[('deel', 'dell'), ('hp', 'hp'), ('aseer', 'aseer'), ('mack', 'mack')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
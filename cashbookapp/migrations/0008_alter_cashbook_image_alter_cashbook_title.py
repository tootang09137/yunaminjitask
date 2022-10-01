# Generated by Django 4.0.4 on 2022-09-25 10:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0007_alter_cashbook_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='cashbook',
            name='title',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1, '제목을 작성해주세요!')]),
        ),
    ]
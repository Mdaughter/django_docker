# Generated by Django 3.0.7 on 2020-06-30 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191022_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodssku',
            name='desc',
            field=models.CharField(blank=True, max_length=256, verbose_name='商品简介'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-02-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='province',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='region_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='region_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='variety',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='winery',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
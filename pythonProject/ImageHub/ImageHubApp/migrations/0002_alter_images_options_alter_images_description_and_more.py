# Generated by Django 5.0.6 on 2024-05-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageHubApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]

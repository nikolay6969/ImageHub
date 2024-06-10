# Generated by Django 5.0.6 on 2024-05-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageHubApp', '0002_alter_images_options_alter_images_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинку'},
        ),
        migrations.AddField(
            model_name='images',
            name='counLike',
            field=models.IntegerField(default=0, verbose_name='Like'),
        ),
    ]

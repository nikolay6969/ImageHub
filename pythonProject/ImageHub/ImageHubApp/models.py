from django.db import models


# Create your models here.
class Images(models.Model):
    image = models.ImageField(verbose_name="Картинка", null=True, upload_to='static/img/')
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=100)
    counLike = models.IntegerField(verbose_name='Like', default=0)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинку'


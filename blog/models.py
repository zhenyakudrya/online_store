from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    tittle = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_publication = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='счетчик публикаций')

    def __str__(self):
        return f'{self.tittle} {self.date_created}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
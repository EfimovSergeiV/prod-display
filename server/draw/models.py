from django.db import models
from django_resized import ResizedImageField



class DrawingModel(models.Model):
    """   """
    DRAWNING_STATUS = (
        ('queue', 'В очереди'),
        ('progress', 'Выполняется'),
        ('completed', 'Выполнен'),
    )

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=15, default='queue', choices=DRAWNING_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    link = models.URLField(blank=True, null=True)
    pdf = models.FileField(upload_to='pdf/', blank=True, null=True)
    webp = models.ImageField(upload_to='webp/', blank=True, null=True)    
    prw = ResizedImageField(
        size = [420, None],
        upload_to='prw/',
        quality=80,
        null=True,
        blank=True,
        force_format='WEBP',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чертеж в производстве'
        verbose_name_plural = 'Чертежи в производстве'



class FileModel(models.Model):
    """ Список файлов в хранилище """

    name = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
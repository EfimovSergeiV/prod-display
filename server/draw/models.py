from django.db import models


class DrawingModel(models.Model):
    """   """

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=15, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    
    webp = models.ImageField(upload_to='webp/', blank=True, null=True)
    pdf = models.FileField(upload_to='pdf/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чертеж'
        verbose_name_plural = 'Чертежи'
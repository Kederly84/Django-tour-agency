from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class BasModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.deleted = True
        self.save()


class ListOfCountries(BasModel):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', '-created']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Regions(BasModel):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE, **NULLABLE)
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', '-created']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Accommodation(BasModel):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE, **NULLABLE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, **NULLABLE)
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='accommodation_img', blank=True)
    short_desc = models.CharField(max_length=128, verbose_name='краткое описание', blank=True)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    availability = models.PositiveIntegerField(verbose_name='количество свободных номеров')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    room_desc = models.CharField(max_length=128, verbose_name='краткое описание комнаты', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        ordering = ['name', 'availability']
        verbose_name = 'Размещение'
        verbose_name_plural = 'Размещения'

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by('country', 'region', 'name')

    def __str__(self):
        return f'{self.name} ({self.country.name})'

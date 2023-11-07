from django.conf import settings
from django.db import models

from mainapp.models import Accommodation


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    nights = models.PositiveIntegerField(default=0, verbose_name='количество ночей')
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def accommodation_cost(self):
        return self.accommodation.price * self.nights

    @property
    def total_nights(self):
        _accommodation = Basket.objects.filter(user=self.user)
        _total_nights = sum(list(map(lambda x: x.nights, _accommodation)))
        return _total_nights

    @property
    def total_cost(self):
        _accommodation = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.accommodation_cost, _accommodation)))
        return _total_cost

    @staticmethod
    def get_item(user):
        return user.basket.select_related().order_by('accommodation__country')

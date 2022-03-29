from django.contrib.auth.models import User
from django.db import models


class NailMaster(models.Model):
    name = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Appointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nail_master = models.ForeignKey(NailMaster, on_delete=models.CASCADE)
    date = models.DateField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nail_master = models.ForeignKey(NailMaster, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.nail_master}, {self.user}'

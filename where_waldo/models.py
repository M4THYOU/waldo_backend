from django.db import models


class WaldoGame(models.Model):
    img = models.ImageField(upload_to='images/')

from django.db import models

# Create your models here.
class Color(models.Model):
    car_color = models.CharField(max_length=100, verbose_name="Цвет машины")

    def __str__(self):
        return self.car_color
    
class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя владельца')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кузов машины')

    def __str__(self):
        return self.kuzov

class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Марка машины')
    price = models.IntegerField(blank=True, null=True, verbose_name='Цена машины')
    car_date = models.DateField(blank=True, null=True, verbose_name='Дата выпуска машины')
    colors = models.ManyToManyField(
        Color,
        related_name='cars',
        verbose_name='colors'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cars',
        verbose_name='Кузов машины'
    )
    
    owner = models.ForeignKey(
        Owner,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="cars",
        verbose_name='Имя владельцов'
    )

    def __str__(self):
        return self.brand
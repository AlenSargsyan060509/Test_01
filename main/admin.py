from django.contrib import admin
from .models import Car, Color, Owner, Category

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', "brand", 'price', 'car_date']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Category)
class OwnerKuzov(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["id", 'car_color']
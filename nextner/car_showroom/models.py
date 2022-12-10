"""Модуль со схематическими моделями таблиц для автосалона"""
from django.db import models


class CarShowRoomModel(models.Model):
    """Модель автосалона"""
    name = models.CharField(max_length=250, verbose_name='Название')
    address = models.TextField(verbose_name='Адрес')
    email = models.EmailField(verbose_name='Email')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car_showrooms'
        verbose_name = 'Авто салон'
        verbose_name_plural = 'Авто салоны'


class CarModel(models.Model):
    """Модель автомобиля"""
    name = models.CharField(max_length=250, verbose_name='Название')
    car_showroom = models.ForeignKey(
        CarShowRoomModel,
        related_name='car',
        verbose_name='Авто салон',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cars'
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class CarSpecificationModel(models.Model):
    """Модель характеристик"""
    name = models.CharField(
        max_length=150, verbose_name='Название')
    amount = models.IntegerField(verbose_name='Количество')
    weight = models.IntegerField(verbose_name='Вес')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    car = models.ForeignKey(
        CarModel,
        related_name='specifications',
        verbose_name='Характеристики',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.car.name

    class Meta:
        db_table = 'car_specification'
        verbose_name = 'Характеристика Автомобиля'
        verbose_name_plural = 'Характеристики Автомобилей'

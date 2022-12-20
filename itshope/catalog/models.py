from django.db import models


# Create your models here.

class Product(models.Model):
    objects = None
    image = models.ImageField()
    name = models.CharField('Название', max_length=50)
    manufacturer = models.CharField('Производитель', max_length=30)
    price = models.IntegerField('Цена', null=True)
    description = models.CharField('Описание', max_length=1000)
    available = models.BooleanField('Наличие', default=True)
    product_type = models.CharField('Тип продукта', max_length=20, db_index=True)

    def __str__(self):
        return self.name


class Videocard(models.Model):
    objects = None
    product = models.OneToOneField(Product,
                                   related_name='videocards',
                                   on_delete=models.CASCADE)

    memory_amount = models.CharField('Кол-во памяти', max_length=15)
    memory_type = models.CharField('Тип памяти', max_length=15)
    memory_frequency = models.CharField('Частота памяти', max_length=15)
    bus_width = models.CharField('Разрядность шины', max_length=15)


class CPU(models.Model):
    product = models.OneToOneField(Product,
                                   related_name='cpus',
                                   on_delete=models.CASCADE)

    clock_speed = models.CharField('Частота процессора', max_length=15)
    number_of_cores = models.IntegerField('Количество ядер', null=True)
    soket = models.CharField('Сокет', max_length=15)
    family = models.CharField('Семейство процессора', max_length=15)
    generation = models.CharField('Поколение процессора', max_length=15)


class Display(models.Model):
    product = models.OneToOneField(Product,
                                   related_name='displays',
                                   on_delete=models.CASCADE)

    diagonal = models.CharField('Диагональ', max_length=15)
    resolution = models.CharField('Разрешение экрана', max_length=15)
    matrix_type = models.CharField('Тип матрицы', max_length=15)
    features = models.CharField('Особенности', max_length=100)

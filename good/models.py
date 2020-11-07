from django.db import models
from customer.models import Customer
from datetime import datetime, timedelta
# Create your models here.

class Order(models.Model):
    '''
    Модель "Заказы"
    customer - покупатель
    name - наименование
    '''
    CHOICES = {
    ('Да', 'Да'),
    ('Нет', 'Нет')
    }
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name="Клиент"
                                 )
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False,
                                   verbose_name="Дата создания"
                                   )
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True,
                                   verbose_name="Обновлено"
                                   )
    payment = models.CharField(default=2,
                               max_length=10,
                               choices=CHOICES,
                               verbose_name="Оплачено"
                               )
    file = models.FileField(upload_to = 'files/',
                            null=True,
                            blank=True,
                            verbose_name="Файл"
                            )

    def __str__(self):
         return "%s" % (self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Good(models.Model):
    '''
    Модель "Товары"
    profile - Профиль
    fittings - Фурнитура
    type_of_product - тип продукта
    filling - Заполнение
    seaf_color - Цвет уплотнения
    micro_ventilation - Микровентиляция
    decor_color - Цвет декора
    handle_color - Цвет ручки
    toning - Тонировка
    product_color - Цвет изделия
    description - описание
    number_of - Количество
    square - Площадь
    price_per_item - Цена за 1 шт.
    sale - Скидка
    price_with_sale - Цена со скидкой
    total_price - Финальная цена
    time_of_production - Время производства
    created - Дата заказа
    updated - Фиксирует время изменения
    completed - Дата изготовления
    '''
    PRODUCT={
    ('СПК 58мм', 'СПК 58мм'),
    ('СПК 47мм', 'СПК 47мм'),
    ('КПС 90мм', 'КПС 90мм'),
    ('СКП 82мм', 'СКП 82мм'),
    }

    order=models.ForeignKey(Order,
                            blank = True,
                            null = True,
                            default = None,
                            on_delete=models.CASCADE,
                            verbose_name="Заказ"
                            )
    profile = models.CharField(max_length=128,
                               default=1,
                               choices=PRODUCT,
                               verbose_name="Профиль"
                               )
    fittings = models.CharField(max_length=128,
                                default=0,
                                verbose_name="Фурнитура"
                                )
    type_of_product = models.CharField(max_length=128,
                                       default=0,
                                       verbose_name="Тип изделия"
                                       )
    filling = models.CharField(max_length=128,
                               default=0,
                               verbose_name="Заполнение"
                               )
    CHOICES= {
            ('Зеленый', 'Зеленый'),
            ('Красный', 'Красный'),
            ('Синий', 'Синий'),
            ('Черный', 'Черный')}
    CHOICES1 = {
        ('Имеется','Имеется'),
        ('Не имеется', 'Не имеется')
    }
    image = models.ImageField(upload_to = 'good_img/',
                              blank=True,
                              null=True,
                              verbose_name="Изображение"
                              )
    seal_color = models.CharField(max_length=10,
                                  default=0,
                                  choices=CHOICES,
                                  verbose_name="Цвет уплотнения"
                                  )
    micro_ventilation = models.CharField(max_length=10,
                                         default=0,
                                         choices=CHOICES1,
                                         verbose_name="Микропроветривание"
                                         )
    decor_color = models.CharField(max_length=10,
                                   default=0,
                                   choices=CHOICES,
                                   verbose_name="Цвет декорации"
                                   )
    handle_color = models.CharField(max_length=10,
                                    default=0,
                                    choices=CHOICES,
                                    verbose_name="Цвет ручки"
                                    )
    toning = models.CharField(max_length=10,
                              default=0,
                              choices=CHOICES,
                              verbose_name="Тонировка"
                              )
    product_color = models.CharField(max_length=10,
                                     default=0,
                                     choices=CHOICES,
                                     verbose_name="Цвет изделия"
                                     )
    time_of_production = models.IntegerField(default=0,
                                             verbose_name="Время изготовления"
                                             )
    number_of = models.IntegerField(default = 1,
                                    verbose_name="Количество"
                                    )
    square = models.CharField(max_length=128,
                              default=0,
                              verbose_name="Площадь"
                              )
    price_per_item = models.DecimalField(max_digits = 10,
                                         decimal_places = 2,
                                         default = 0,
                                         verbose_name="Цена за 1 штуку"
                                         )
    sale = models.IntegerField(default=0,
                               verbose_name="Скидка"
                               )
    price_with_sale = models.CharField(blank=True,
                                       null=True,
                                       max_length=128,
                                       default=0,
                                       verbose_name="Цена со скидкой за 1 шт."
                                       )
    total_price = models.DecimalField(max_digits = 10,
                                      decimal_places = 2,
                                      default = 0,
                                      verbose_name="Итоговая цена"
                                      )
    created = models.DateTimeField(default = datetime.now(),
                                   blank=True,
                                   null=True,
                                   verbose_name="Дата начала производства"
                                   )
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True,
                                   verbose_name="Обновлено"
                                   )
    completed = models.DateTimeField(blank=True,
                                     null=True,
                                     verbose_name="Дата изготовления"
                                     )

    CHOICES_STATUS = {
        ('1','Ожидает материал'),
        ('2', 'В производстве'),
        ('3', 'Готов')
    }

    status = models.CharField(max_length=1,default=1,choices=CHOICES_STATUS)

    def save(self, *args, **kwargs):
       self.completed = self.created + timedelta(hours=self.time_of_production)
       self.total_price = int(self.price_per_item*self.number_of*(100-self.sale))/100
       self.price_with_sale=int(self.price_per_item*(100-self.sale))/100
       super().save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.profile,self.total_price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class GoodImage(models.Model):
    '''
    Модель фотографий для товаров
    '''
    good = models.ForeignKey(Good,
                             blank = True,
                             null = True,
                             default = None,
                             on_delete=models.CASCADE,
                             verbose_name="Товар"
                             )
    image = models.ImageField(upload_to = 'good_img/',
                              verbose_name="Изображение"
                              )
    is_main = models.BooleanField(default = False,
                                  verbose_name="Основная"
                                  )
    is_active = models.BooleanField(default = True,
                                    verbose_name="Активная"
                                    )
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False,
                                   verbose_name="Дата создания"
                                   )
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True,
                                   verbose_name="Обновлено"
                                   )

    def __str__(self):
         return "Товар: %s" % self.id

    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товаров'

from django.db import models
from django.db.models import Sum
from django.forms import ModelForm
from good.models import Order
from customer.models import Customer
from datetime import datetime, timedelta

# Create your models here.

class Provider(models.Model):
    '''
    Модель "Поставщик услуг"
    '''
    GENDER = {
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
    ('Не определен', 'Не определен')
    }
    first_name = models.CharField(max_length=30,
                                  verbose_name="Имя"
                                  )
    last_name = models.CharField(max_length=30,
                                 verbose_name="Фамилия"
                                 )
    patronymic = models.CharField(max_length=30,
                                  verbose_name="Отчество"
                                  )
    gender = models.CharField(default=3,
                              max_length=30,
                              choices=GENDER,
                              verbose_name="Пол"
                              )
    organization = models.CharField(max_length=30,
                                    verbose_name="Организация"
                                    )
    director = models.CharField(max_length=20,
                                verbose_name="Директор"
                                )

    class Meta:
        verbose_name = "Поставщик услуг"
        verbose_name_plural = "Поставщики услуг"

    def __str__(self):
        return '%s %s %s %s' % (self.last_name,self.first_name,self.patronymic,self.organization)


class Transaction(models.Model):
    date_transaction = models.DateField(blank=True,
                                        null=True,
                                        verbose_name="Дата поступления платежа"
                                        )
    contract = models.ForeignKey('Contract',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                verbose_name="Контракт"
                                )
    sum = models.DecimalField(max_digits = 10,
                              decimal_places = 2,
                              default = 0,
                              verbose_name="Сумма оплаты"
                            )
    comment = models.CharField(max_length=128,
                               verbose_name="Комментарий к оплате"
                               )
    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return '%s %s %s' % (self.date_transaction, self.sum, self.comment)


class Contract(models.Model):
    '''
    "Модель "Договор"
    order - заказ
    customer - клиент
    provider - заказчик
    type - тип договора(0-обычный договор) ?нужно подумать о других видах
    data_provider - дата создания договора
    information - дополнительная информация
    '''
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              verbose_name="Заказ"
                              )
    contract_number = models.IntegerField(default=0,
                                          verbose_name="Номер контракта"
                                          )
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name="Клиент"
                                 )
    provider = models.ForeignKey(Provider,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name="Поставщик"
                                 )
    avance = models.IntegerField(default=50,
                                 verbose_name="Аванс"
                                 )
    garanty = models.IntegerField(default=1,
                                  verbose_name="Гарантия"
                                  )
    time_of_production = models.IntegerField(default=45,
                                             verbose_name="Срок поставки"
                                             )
    #Словарь типов договоров
    CHOICES= {
            ('Тип 1', 'Тип 1'),
            ('Тип 2', 'Тип 2'),
            ('Тип 3', 'Тип 3'),
            ('Тип 4', 'Тип 4')}
    type = models.CharField(max_length=128,
                            choices=CHOICES,
                            verbose_name="Тип договора"
                            )
    total_price = models.DecimalField(max_digits = 10,
                                     decimal_places = 2,
                                     default = 0,
                                     verbose_name="Полная стоимость"
                                     )
    date_provider = models.DateField(blank=True,
                                     null=True,
                                     verbose_name="Дата подписания договора поставщиков"
                                     )
    created = models.DateTimeField(default = datetime.now(),
                                   verbose_name="Дата создания"
                                   )
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True,
                                   verbose_name="Обновлено"
                                   )
    # def get_total_price(self):
    #     return self.order.good_set.all().aggregate(Sum('total_price'))['total_price__sum']

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"
        ordering = ["id"]


    def __str__(self):
        return '%s %s %s' % (self.id,self.customer, self.provider)

    def save(self, *args, **kwargs):
        self.customer = self.order.customer
        self.date_provider = self.created.date()
        super().save(*args, **kwargs)


    def get_total_transaction(self):
        if Transaction.objects.filter(contract=self.id).aggregate(Sum('sum'))['sum__sum'] is None:
            return 0
        else:
            return Transaction.objects.filter(contract=self.id).aggregate(Sum('sum'))['sum__sum']

    def get_debt(self):
        if Transaction.objects.filter(contract=self.id).aggregate(Sum('sum'))['sum__sum'] is None:
            return self.total_price
        else:
            return self.total_price - Transaction.objects.filter(contract=self.id).aggregate(Sum('sum'))['sum__sum']

from django.db import models
from django.forms import ModelForm


class Customer(models.Model):
    '''
    Модель "Покупатель"
    first_name - имя
    last_name - фамилия
    patronymic - отчество
    number - телефон
    city - город
    bank_account - банковский счет
    mail_index - почтовый индекс
    email - почта
    '''
    GENDER = {
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
    ('Неопределен', 'Неопределен')
    }
    first_name = models.CharField(max_length=30,
                                  blank=True,
                                  verbose_name="Имя"
                                  )
    last_name = models.CharField(max_length=30,
                                 blank=True,
                                 verbose_name="Фамилия"
                                 )
    patronymic = models.CharField(max_length=30,
                                  blank=True,
                                  verbose_name="Отчество"
                                  )
    gender = models.CharField(default=3,
                              max_length=30,
                              choices = GENDER,
                              verbose_name="Пол"
                              )
    number = models.CharField(max_length=15,
                              verbose_name="Номер телефона"
                              )
    bank_account = models.CharField(max_length=30,
                                    verbose_name="Банковские данные"
                                    )
    mail_index = models.CharField(max_length=6,
                                  verbose_name="Индекс"
                                  )
    city = models.CharField(max_length=20,
                            verbose_name="Город"
                            )
    email = models.EmailField(blank=True,
                              verbose_name="Email"
                              )

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return '%s %s %s %s' % (self.last_name,self.first_name, self.patronymic, self.number)

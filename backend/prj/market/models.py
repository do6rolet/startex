# Модели (типы полей выбрать из представляемых фреймворком):
# - Учетные записи пользователей: ФИО, адрес доставки, email (он же логин), пароль, роль.
# - Роли пользователей: клиент, менеджер.
# - Товары: артикул (текст), наименование, цена закуп, цена розница.
# - Корзина: клиент, товар, количество, цена, сумма по строке.

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.utils.text import slugify





class Product(models.Model):
    articule = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    price_in = models.DecimalField(max_digits=12, decimal_places=2)
    price_out = models.DecimalField(max_digits=12, decimal_places=2)
    slug = models.SlugField(max_length=200, db_index=True, default='', editable=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name



    def save(self, *args, **kwargs):
        value = self.name + self.articule

        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)








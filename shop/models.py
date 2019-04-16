from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone
from django.shortcuts  import redirect

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])
#model posta
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, verbose_name="Изображение поста")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#Модель темы
class Themes(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='themes/%Y/%m/%d/', blank=True, verbose_name="Изображение темы")
    class Meta:
        ordering = ['name']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ThemeListByTheme', args=[self.slug])
class Filt(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    longname = models.CharField(max_length=100)
    class Meta:
        ordering = ['name']
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])            

# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    themes = models.ForeignKey(Themes,related_name='products',verbose_name='Тема')
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    promo = models.BooleanField(verbose_name='Акция')
    new = models.BooleanField(verbose_name='Новые')
    hit = models.BooleanField(verbose_name='Хит продаж')
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large')
    ]
    name = models.CharField(max_length=3, choices=SIZES, unique=True)

    class Meta:
        verbose_name = "Розмір"
        verbose_name_plural = "Розміри"

    def __str__(self):
        return self.name



class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(
        max_length=7, 
        validators=[
            RegexValidator(
                regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
                message='Введіть коректний HEX-код кольору'
            )
        ]
    )

    class Meta:
        verbose_name = "Колір"
        verbose_name_plural = "Кольори"

    def __str__(self):
        return f"{self.name} ({self.hex_code})"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва')
    description = models.TextField(verbose_name='Описання')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    newPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0,  verbose_name='Новаціна по Акцій')
    newPrice_Yes_No = models.BooleanField(default=False, verbose_name='Показати Акцію')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категорія')
    stock = models.PositiveIntegerField(verbose_name='Штук в Наявності')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Назва')
    sizes = models.ManyToManyField(Size, related_name='products', verbose_name='Розмір')
    colors = models.ManyToManyField(Color, related_name='products', verbose_name='Колір')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def __str__(self):
        return self.name
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='Вибери продукт')
    image = models.ImageField(upload_to='product_images/')
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинкі"

    def __str__(self):
        return f"Image for {self.product.name}"
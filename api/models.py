from django.db import models

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
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Extra Extra Extra Large')
    ]
    name = models.CharField(max_length=4, choices=SIZES, unique=True)

    class Meta:
        verbose_name = "Розмір"
        verbose_name_plural = "Розміри"

    def __str__(self):
        return self.name


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
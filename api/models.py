from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
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
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    sizes = models.ManyToManyField(Size, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def __str__(self):
        return self.name
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинкі"

    def __str__(self):
        return f"Image for {self.product.name}"
from rest_framework import serializers
from .models import Category, Product, Size, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products']
        





class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name']


class ProductImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_primary']

class ProductSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)


    available_sizes = serializers.ListField(
        child=serializers.CharField(), 
        write_only=True
    )
    available_colors = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        ), 
        write_only=True
    )
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), 
        write_only=True, 
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'newPrice', 'newPrice_Yes_No', 'category', 
            'stock', 'created_at', 'images', 'uploaded_images', 
            'sizes', 'available_sizes', 'available_colors'
        ]


    def create(self, validated_data):
        sizes_data = validated_data.pop('available_sizes', [])
        images_data = validated_data.pop('uploaded_images', [])


        # Create product
        product = Product.objects.create(**validated_data)
        
        # Add sizes
        for size_name in sizes_data:
            size, _ = Size.objects.get_or_create(name=size_name)
            product.sizes.add(size)

        
        # Add images
        for index, image_data in enumerate(images_data):
            is_primary = index == 0  # First image is primary


            
            ProductImage.objects.create(
                product=product, 
                image=image_data, 
                is_primary=is_primary,
            )
        
        return product

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    """
    Проверка названия отсутствует, так как это проверяется из-за null=False в модели
    """
    def validate_price(self, value):
        if value is not None:
            if value < 0:
                raise serializers.ValidationError("Цена должна быть больше нуля")
        return value

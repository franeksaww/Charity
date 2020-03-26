from rest_framework import serializers

from main_apk.models import CategoryModel, InstitutionModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'name')


class InstitutionSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = InstitutionModel
        fields = ('id', 'name', 'description', 'type', 'categories')
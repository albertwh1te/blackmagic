# coding:utf-8
from rest_framework import serializers
from houses.models import House, Collection


class HouseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        depth = 2


class CollectionSerializer(serializers.ModelSerializer):
    house_id = serializers.IntegerField()

    def create(self, data):
        house_id = data['house_id']
        house = House.objects.filter(id=house_id).first()
        if house:
            user = self.context['request'].user
            collection = Collection(
                house=house,
                user=user
            )
            collection.save()
            return collection

    class Meta:
        model = Collection
        depth = 2

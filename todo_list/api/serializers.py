from dataclasses import field
from typing_extensions import Required
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from base.models import Item, List

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'date', 'list']

    # def create(self, validated_data):
    #     # Create and return a new Item instance, given the validated data.
    #     return Item.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # Updates and returns an existing Item instance,
    #     # given the validated data.
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.completed = validated_data.get('completed', instance.completed)
        
    #     instance.save()
    #     return instance
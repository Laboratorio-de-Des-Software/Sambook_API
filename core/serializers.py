from rest_framework import serializers
from core.models import Example

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Example
        fields=(
            'ID',
            'Nome',
            'Idade',
            'data_criacao'
            )

# from django.contrib.auth.models import User,Group
# from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

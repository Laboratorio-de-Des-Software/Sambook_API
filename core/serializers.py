from rest_framework import serializers
from .models import Escola, Enredo, LivroAbreAlas, Usuario


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['idEscola', 'nome']

class EnredoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enredo
        fields = ['idEnredo', 'enredo', 'carnavalesco']

class LivroAbreAlasSerializer(serializers.ModelSerializer):
    escola = EscolaSerializer()

    class Meta:
        model = LivroAbreAlas
        fields = ['idLivro', 'escola', 'data_cadastro', 'enredo']

class UsuarioSerializer(serializers.ModelSerializer):
    escola = EscolaSerializer()

    class Meta:
        model = Usuario
        fields = ['idUsr', 'nomeUsr', 'escola']



# old3
# class ExampleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Example
#         fields=(
#             'ID',
#             'Nome',
#             'Idade',
#             'data_criacao'
#             )

# old2
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


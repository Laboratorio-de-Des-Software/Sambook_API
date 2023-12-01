from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import views,status

from .models import Escola, Enredo, LivroAbreAlas, Usuario
from .serializers import EnredoSerializer, EscolaSerializer, LivroAbreAlasSerializer, UsuarioSerializer


@csrf_exempt
def crud_api(request, model_name, id=None):
    """
    View para operações CRUD em diferentes modelos.
    """
    model_mapping = {
        'escola': Escola,
        'enredo': Enredo,
        'livroabrealas': LivroAbreAlas,
        'usuario': Usuario,
    }

    model = model_mapping.get(model_name.lower())
    
    if not model:
        return JsonResponse({"message": "Modelo não encontrado"}, safe=False, status=404)

    if request.method == 'GET':
        objects = model.objects.all()
        serializer = get_serializer(model_name)(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = get_serializer(model_name)(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Inserido com sucesso"}, safe=False)
        return JsonResponse({"message": "Falha ao inserir", "errors": serializer.errors}, safe=False, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        instance = model.objects.get(pk=data['id'])
        serializer = get_serializer(model_name)(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Dados atualizados!"}, safe=False)
        return JsonResponse({"message": "Falha ao atualizar", "errors": serializer.errors}, safe=False, status=400)

    elif request.method == 'DELETE':
        instance = model.objects.get(pk=id)
        instance.delete()
        return JsonResponse({"message": "Deletado com sucesso!"}, safe=False)

    return JsonResponse({"message": "Método não permitido"}, safe=False, status=405)


def get_serializer(model_name):
    """
    Retorna o serializer correspondente ao modelo.
    """
    serializer_mapping = {
        'escola': EscolaSerializer,
        'enredo': EnredoSerializer,
        'livroabrealas': LivroAbreAlasSerializer,
        'usuario': UsuarioSerializer,
    }
    return serializer_mapping.get(model_name.lower())


# Old2
# from django.contrib.auth.models import User,Group
# from rest_framework import viewsets
# from rest_framework import permissions
# from core.serializers import UserSerializer,GroupSerializer

# class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all().order_by('-date_joined')
#   serializer_class = UserSerializer
#   permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]



# old3
# class ExampleAPIView(views.APIView):

  # serializer_class = ExampleSerializer

  # def get_serializer_context(self):
  #   return {
  #     'request': self.request,
  #     'view': self,
  #   }

  # def get_serializer(self, *args, **kwargs):
  #   kwargs['context'] = self.get_serializer_context()
  #   return self.serializer_class(*args, **kwargs)




#old1
# class ExampleAPIView(views.APIView):
#   def exampleApi(request,id=None):
#     if request.method == 'GET':
#       examplesGetObjs = Example.objects.all()
#       examples_serializer = ExampleSerializer(examplesGetObjs,many=True)
#       return JsonResponse(examples_serializer.data,safe=False)
#     elif request.method == 'POST':
#       example_data = JSONParser().parse(request)
#       example_serializer = ExampleSerializer(data=example_data)
#       if example_serializer.is_valid():
#         example_serializer.save()
#         return JsonResponse("Inserido com Sucesso",safe=False)
#       return JsonResponse("Falha ao inserir",safe=False)
#     elif request.method == 'PUT':
#       example_data = JSONParser().parse(request)
#       example = Example.objects.get(ExampleID = example_data['ID'])
#       Example_serializer = ExampleSerializer(Example,data=example_data)
#       if Example_serializer.is_valid():
#         Example_serializer.save()
#         return JsonResponse("Dados atualizados!",safe=False)
#       return JsonResponse("Falha ao atualizar!")
#     elif request.method == 'DELETE':
#       example = Example.objects.get(ExmpleId=id)
#       example.delete()
#       return JsonResponse("Deletado com sucesso!",safe=False)

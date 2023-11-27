from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import views,status

from .models import Example
from .serializers import ExampleSerializer

# Old
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

class ExampleAPIView(views.APIView):

  serializer_class = ExampleSerializer

  def get_serializer_context(self):
    return {
      'request': self.request,
      'view': self,
    }

  def get_serializer(self, *args, **kwargs):
    kwargs['context'] = self.get_serializer_context()
    return self.serializer_class(*args, **kwargs)

  def exampleApi(request,id=None):
    if request.method == 'GET':
      examplesGetObjs = Example.objects.all()
      examples_serializer = ExampleSerializer(examplesGetObjs,many=True)
      return JsonResponse(examples_serializer.data,safe=False)
    elif request.method == 'POST':
      example_data = JSONParser().parse(request)
      example_serializer = ExampleSerializer(data=example_data)
      if example_serializer.is_valid():
        example_serializer.save()
        return JsonResponse("Inserido com Sucesso",safe=False)
      return JsonResponse("Falha ao inserir",safe=False)
    elif request.method == 'PUT':
      example_data = JSONParser().parse(request)
      example = Example.objects.get(ExampleID = example_data['ID'])
      Example_serializer = ExampleSerializer(Example,data=example_data)
      if Example_serializer.is_valid():
        Example_serializer.save()
        return JsonResponse("Dados atualizados!",safe=False)
      return JsonResponse("Falha ao atualizar!")
    elif request.method == 'DELETE':
      example = Example.objects.get(ExmpleId=id)
      example.delete()
      return JsonResponse("Deletado com sucesso!",safe=False)

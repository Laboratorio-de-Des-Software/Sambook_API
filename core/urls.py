from django.urls import include, path
from rest_framework import routers
from core import views


urlpatterns = [
    # Exemplo para o modelo Escola
    path('escola/', crud_api, {'model_name': 'escola'}, name='escola_crud_api'),
    path('escola/<int:id>/', crud_api, {'model_name': 'escola'}, name='escola_crud_api'),

    # Exemplo para o modelo Enredo
    path('enredo/', crud_api, {'model_name': 'enredo'}, name='enredo_crud_api'),
    path('enredo/<int:id>/', crud_api, {'model_name': 'enredo'}, name='enredo_crud_api'),

    # Exemplo para o modelo LivroAbreAlas
    path('livroabrealas/', crud_api, {'model_name': 'livroabrealas'}, name='livroabrealas_crud_api'),
    path('livroabrealas/<int:id>/', crud_api, {'model_name': 'livroabrealas'}, name='livroabrealas_crud_api'),

    # Exemplo para o modelo Usuario
    path('usuario/', crud_api, {'model_name': 'usuario'}, name='usuario_crud_api'),
    path('usuario/<int:id>/', crud_api, {'model_name': 'usuario'}, name='usuario_crud_api'),
]




# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)




# urlpatterns = [
#      # path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#     path('example',views.exampleApi),
#     path('example/<int:id>',views.exampleApi)
# ]
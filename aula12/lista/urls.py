from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views
from .models import Post, Comentario

# Serializers da API
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'autor', 'conteudo', 'data_postagem']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'autor', 'conteudo', 'data_comentario']

# ViewSets da API
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

# Router DRF
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comentarios', ComentarioViewSet)

# URLs do site + API
urlpatterns = [
    path('comentario/', views.comentario, name='comentario'),
    path('comentario/remove/<int:id>/', views.remove_comentario, name='remove_comentario'),
    path('ola/', views.ola, name='ola'),
    path('index/', views.index, name='index'),
    path('index/remove/<int:id>/', views.remove_post, name='remove_post'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('comentario/editar/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('index/editar/<int:id>/', views.editar_post, name='editar_post'),
    
    path('api/', include(router.urls)),
]

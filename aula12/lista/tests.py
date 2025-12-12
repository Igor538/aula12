from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comentario

class TestPosts(TestCase):
    def setUp(self):
        # Criar um usuário genérico
        self.user = User.objects.create_user(username='usuario1', password='senha123')
        # Criar um post associado ao usuário
        self.post = Post.objects.create(autor=self.user, conteudo='Conteúdo do post')

    def test_criar_post(self):
        post = Post.objects.get(autor=self.user)
        self.assertEqual(post.conteudo, 'Conteúdo do post')

    def test_representacao_post(self):
        post = Post.objects.get(autor=self.user)
        # O __str__ do model retorna: f'{self.conteudo} ({self.id})'
        self.assertEqual(str(post), f'{post.conteudo} ({post.id})')


class TestComentario(TestCase):
    def setUp(self):
        # Criar um usuário genérico
        self.user = User.objects.create_user(username='usuario2', password='senha123')
        # Criar um comentário associado ao usuário
        self.comentario = Comentario.objects.create(
            autor=self.user,
            conteudo='Conteúdo do comentário'
        )

    def test_comentario_criado(self):
        comentario = Comentario.objects.get(autor=self.user)
        self.assertEqual(comentario.conteudo, 'Conteúdo do comentário')
        self.assertEqual(comentario.autor.username, 'usuario2')

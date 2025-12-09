from django.test import TestCase
from .models import Post, Comentario

class TestPosts(TestCase):
    def setUp(self):
        Post.objects.create(id=100, autor='Miguel', conteudo='Post 1')

    def test_criar_post(self):
        post = Post.objects.get(autor='Miguel')
        self.assertEqual(post.conteudo, 'Post 1')

    def test_representacao_post(self):
        post = Post.objects.get(autor='Miguel')
        self.assertEqual(str(post), 'Miguel (100)')

class TestComentario(TestCase):
    def setUp(self):
        Comentario.objects.create(autor='Miguel', data_comentario='2025-11-18 11:52:00', conteudo="Comentario 1")

    def test_comentario_criado(self):
        comentario = Comentario.objects.get(autor='Miguel')
        self.assertEqual(comentario.conteudo, 'Comentario 1')
        self.assertEqual(comentario.autor, 'Miguel')

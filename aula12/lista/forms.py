from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Post, Comentario


# Formulário de Registro
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Endereço de e-mail',
        error_messages={'required': 'O e-mail é obrigatório.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nome de usuário',
            'password1': 'Senha',
            'password2': 'Confirme a senha'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email


# Formulário de Login
class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _('Por favor, insira um nome de usuário e senha corretos.'),
        'inactive': _('Esta conta está inativa.'),
    }


# Formulário de criação de tarefa (Post)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.TextInput(
                attrs={
                    'placeholder': 'Digite sua tarefa...',
                    'class': 'editar'
                }
            )
        }


# Formulário de comentário
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu comentário...',
                    'class': 'editar'
                }
            )
        }

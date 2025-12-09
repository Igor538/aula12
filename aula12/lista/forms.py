from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Post, Comentario

# Formulário de Registro
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
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
        help_texts = {
            'username': _('Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.'),
            'password1': _('Sua senha deve conter pelo menos 8 caracteres e não ser muito comum ou apenas numérica.'),
        }

    error_messages = {
        'password_mismatch': _('As senhas não coincidem.'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].error_messages.update({
            'password_too_short': _('A senha é muito curta. Deve conter pelo menos 8 caracteres.'),
            'password_too_common': _('Esta senha é muito comum. Escolha outra.'),
            'password_entirely_numeric': _('A senha não pode conter apenas números.'),
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

# Formulário de Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput,
    )

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
            'conteudo': forms.TextInput(attrs={'placeholder': 'Digite sua tarefa...', 'class': 'editar'})
        }

# Formulário de comentário
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.TextInput(attrs={'placeholder': 'Digite seu comentário...', 'class': 'editar'})
        }

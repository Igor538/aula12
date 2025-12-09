from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def ola(request):
    return render(request, 'ola.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ola')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('ola')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha incorretos.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    posts = Post.objects.filter(autor=request.user)
    editar_id = request.GET.get('editar')
    post_edit = None
    if editar_id:
        post_edit = get_object_or_404(Post, id=editar_id, autor=request.user)

    if request.method == 'POST':
        if 'editar_post' in request.POST:
            post_id = request.POST.get('post_id')
            post_to_edit = get_object_or_404(Post, id=post_id, autor=request.user)
            form = PostForm(request.POST, instance=post_to_edit)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('index')
    else:
        form = PostForm(instance=post_edit)

    return render(request, 'index.html', {'posts': posts, 'form': form, 'editar_id': editar_id})

@login_required
def remove_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.autor == request.user:
        post.delete()
    return redirect('index')

@login_required
def comentario(request):
    comentarios = Comentario.objects.filter(autor=request.user)
    editar_id = request.GET.get('editar')
    comentario_edit = None
    if editar_id:
        comentario_edit = get_object_or_404(Comentario, id=editar_id, autor=request.user)

    if request.method == 'POST':
        if 'editar_comentario' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            comentario_to_edit = get_object_or_404(Comentario, id=comentario_id, autor=request.user)
            form = ComentarioForm(request.POST, instance=comentario_to_edit)
            if form.is_valid():
                form.save()
                return redirect('comentario')
        else:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.autor = request.user
                comment.save()
                return redirect('comentario')
    else:
        form = ComentarioForm(instance=comentario_edit)

    return render(request, 'comentarios.html', {'comentarios': comentarios, 'form': form, 'editar_id': editar_id})

@login_required
def remove_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    if comentario.autor == request.user:
        comentario.delete()
    return redirect('comentario')

@login_required
def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id, autor=request.user)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentario')
    else:
        form = ComentarioForm(instance=comentario)
    comentarios = Comentario.objects.filter(autor=request.user)
    return render(request, 'comentarios.html', {'comentarios': comentarios, 'form_editar': form, 'editar_id': id})

@login_required
def editar_post(request, id):
    post = get_object_or_404(Post, id=id, autor=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    posts = Post.objects.filter(autor=request.user)
    return render(request, 'index.html', {'posts': posts, 'form_editar': form, 'editar_id': id})
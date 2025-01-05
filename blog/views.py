from django.shortcuts import render, get_object_or_404, redirect
from .models import AcercaDe, Blog 
from .forms import RegistroUsuarioForm, PostForm, EditProfileForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db import models 
from .models import Post, Entrevista, Noticia, Analisis, Mensaje
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Mensaje
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from mensajes.models import Mensaje
from django.views.decorators.csrf import csrf_protect


def vista_acerca_de(request):
    acerca_de = AcercaDe.objects.first()  # Suponiendo que solo hay un objeto
    return render(request, 'acerca_de.html', {'acerca_de': acerca_de})

def vista_pags(request):
    blogs = Blog.objects.all()
    return render(request, 'paginas.html', {'blogs': blogs})

def detalle_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'detalle_blog.html', {'blog': blog})


def lobby(request):
    return render(request, 'lobby.html')

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_lobby')  # Redirigir al lobby o página principal
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


from django.shortcuts import render
from .models import Post

def home_lobby(request):
    if request.user.is_authenticated:
        # Últimos posts, ordenados por fecha de publicación, obtenemos los últimos 5
        ultimos_posts = Post.objects.all().order_by('-fecha_publicacion')[:5]

        # Posts destacados, filtramos por el campo 'destacado' (suponiendo que existe)
        posts_destacados = Post.objects.filter(destacado=True)

    else:
        ultimos_posts = []
        posts_destacados = []

    return render(request, 'home_lobby.html', {
        'posts_destacados': posts_destacados,
        'ultimos_posts': ultimos_posts,
    })






# Vista para el perfil del usuario
@login_required
def perfil(request):
    return render(request, 'perfil.html')  # Asegúrate de tener un template para el perfil

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})



# Vista para la página principal
def pagina_principal(request):
    # Recuperamos los posts para mostrarlos en la página principal
    posts = Post.objects.all()  # O puedes agregar filtros según lo que quieras mostrar (ej. destacados)
    return render(request, 'pagina_principal.html', {'posts': posts})

# Vista para la página "Acerca de mí"
def acerca_de(request):
    return render(request, 'acerca_de.html')

# Vista para el detalle de un post
def detalle_post(request, post_id):  # Asegúrate de que el parámetro se llama post_id
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detalle_entrevista.html', {'post': post})

# Vista para el perfil (si el usuario está autenticado)
def perfil(request):
    return render(request, 'perfil.html')

def categoria_analisis(request):
    analisis_list = Analisis.objects.all()
    return render(request, 'categoria_analisis.html', {'analisis': analisis_list})

def detalle_analisis(request, id):
    analisis = get_object_or_404(Analisis, id=id)
    return render(request, 'detalle_analisis.html', {'analisis': analisis})



def categoria_entrevistas(request):
    entrevistas = Entrevista.objects.all()  # Asegúrate de que esto devuelva todas las entrevistas
    paginator = Paginator(entrevistas, 6)  # Paginación de 6 entrevistas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Página actual

    return render(request, 'categoria_entrevistas.html', {'posts': page_obj})

def categoria_rugby_noticias(request):
    # Filtramos los posts por la categoría "Noticias"
    posts = Post.objects.filter(categoria="Noticias")

    # Asegúrate de que hay posts para mostrar
    print(posts)  # Esto es solo para depurar

    return render(request, 'categoria_rugby_noticias.html', {'posts': posts})

def detalle_noticia(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detalle_noticia.html', {'post': post})

def noticias_list(request):
    noticias = Noticia.objects.all()
    paginator = Paginator(noticias, 9)  # 9 noticias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'noticias.html', {'posts': page_obj})

def detalle_entrevista(request, pk):
    # Filtrar solo las entrevistas
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detalle_entrevista.html', {'post': post})


def index(request):
    # Obtener todos los posts o las publicaciones que desees mostrar
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detalle_post.html', {'post': post})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm  # Si tienes un formulario para editar el perfil

@login_required
def editar_perfil(request):
    # Obtener el usuario actual
    usuario = request.user
    
    # Si el método de la solicitud es POST, se procesan los datos del formulario
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('perfil')  # Redirigir a la vista del perfil
    else:
        form = EditProfileForm(instance=usuario)
    
    return render(request, 'editar_perfil.html', {'form': form})


def custom_logout(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página principal o a la página que prefieras

from django.shortcuts import render

@login_required
def inbox(request):
    # Filtra los mensajes donde el usuario logueado es el receptor
    messages = Mensaje.objects.filter(receiver=request.user).order_by('-timestamp')  # Solo los mensajes recibidos
    
    context = {
        'messages': messages,
    }
    
    return render(request, 'mensajes/inbox.html', context)


@csrf_protect
@login_required
def send_message(request, user_id=None):
    users = User.objects.exclude(id=request.user.id)  # Excluye al usuario logueado
    if request.method == "POST":
        recipient_id = request.POST.get('recipient')
        content = request.POST.get('content')
        
        if recipient_id and content:
            recipient = get_object_or_404(User, id=recipient_id)
            mensaje = Mensaje(sender=request.user, receiver=recipient, content=content)
            mensaje.save()
            return redirect('mensajes:inbox')
    
    return render(request, 'mensajes/send_message.html', {'users': users})

@login_required
def message_detail(request, message_id):
    # Ver detalles de un mensaje
    message = Mensaje.objects.get(id=message_id)
    if message.receiver != request.user:
        raise Http404("No tienes permiso para ver este mensaje")
    
    # Marcar el mensaje como leído
    message.is_read = True
    message.save()
    
    return render(request, 'mensajes/message_detail.html', {'message': message})






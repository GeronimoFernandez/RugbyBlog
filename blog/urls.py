from django.urls import path
from . import views
from .views import lobby
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_lobby, name='home_lobby'),  # Ruta principal para home_lobby
    path('acerca-de/', views.vista_acerca_de, name='acerca_de'),
    path('paginas/', views.vista_pags, name='paginas'),
    path('paginas/<int:blog_id>/', views.detalle_blog, name='detalle_blog'),
    #registro de usuarios
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),    
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('', views.lobby, name='lobby'),
    path('', views.pagina_principal, name='pagina_principal'),
    path('noticias/', views.categoria_rugby_noticias, name='categoria_rugby_noticias'),
    path('analisis/', views.categoria_analisis, name='categoria_analisis'),
    path('entrevistas/', views.categoria_entrevistas, name='categoria_entrevistas'),
    path('detalle/<int:id>/', views.detalle_noticia, name='detalle_noticia'),  # Vista de detalle de una noticia
    path('', views.index, name='index'), 
    path('detalle/<int:id>/', views.detalle_entrevista, name='detalle_entrevista'),   
    path('post/<int:id>/', views.detalle_post, name='detalle_post'),
    path('analisis/', views.categoria_analisis, name='analisis'),
    path('analisis/<int:id>/', views.detalle_analisis, name='detalle_analisis'),
    path('lobby/', views.home_lobby, name='lobby'),
    path('home/', views.home_lobby, name='home_lobby'),
    path('inbox/', views.inbox, name='inbox'),
    path('send-message/<int:user_id>/', views.send_message, name='send_message'),
]




    # Otras rutas


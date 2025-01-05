# messages/urls.py

from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviar/<int:user_id>/', views.send_message, name='send_message'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
]

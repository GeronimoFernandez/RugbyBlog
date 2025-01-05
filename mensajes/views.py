# messages/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from .forms import MessageForm
from mensajes.models import Mensaje
from django.views.decorators.csrf import csrf_protect

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


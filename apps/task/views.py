from .forms import TaskForm
from .models import Task

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import TaskSerializer

from .tasks import send_notification_email


class TaskListView(ListView):
    """Lista todas las tareas creadas."""
    model = Task
    template_name = 'list.html'
    context_object_name = 'tasks'
    

class TaskView(CreateView):
    """Crea una nueva tarea."""
    model = Task
    template_name = 'create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task:list_task')


    def form_valid(self, form):
        """
        Envía un correo electrónico de forma asíncrona
        al usuario que se le asignó la tarea 
        usando el metodo send_notification_email
        """
        form.instance.created_by = self.request.user
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('description')
        title = form.cleaned_data.get('title')
        form.save()
        send_notification_email(email, title, message, 'Se te asignó una nueva tarea')
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    """Actualiza una tarea."""
    model = Task
    form_class = TaskForm
    template_name = 'update.html'
    success_url = reverse_lazy('task:list_task')

    def form_valid(self, form):
        """
        Envía un correo electrónico de forma asíncrona
        al usuario que se tiene asiganda la tarea al momento de actualizarla
        usando el metodo send_notification_email
        """
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('description')
        title = form.cleaned_data.get('title')
        form.save()
        send_notification_email(email, title, message, 'Una de tus tareas ha sido actualizada.')
        return super().form_valid(form)
    

class TaskDeleteView(DeleteView):
    """Elimina una tarea."""
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('task:list_task')


class TaskViewSet(viewsets.ModelViewSet):
    """API para listar, crear, actualizar y eliminar tareas."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Envía un correo electrónico de forma asíncrona
        al usuario que se le asignó la tarea 
        usando el metodo send_notification_email
        """
        response = super().create(request, *args, **kwargs)
        email = request.data.get('email', None)
        title = request.data.get('title', None)
        message = request.data.get('description', None)

        send_notification_email(email, title, message, 'Se te asignó una nueva tarea')

        return response
    
    def update(self, request, *args, **kwargs):
        """
        Envía un correo electrónico de forma asíncrona
        al usuario que se tiene asiganda la tarea al momento de actualizarla
        usando el metodo send_notification_email
        """
        response = super().update(request, *args, **kwargs)
        email = request.data.get('email', None)
        title = request.data.get('title', None)
        message = request.data.get('description', None)

        send_notification_email(email, title, message, 'Una de tus tareas ha sido actualizada.')
        
        return response
    
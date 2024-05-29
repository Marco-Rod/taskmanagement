from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """Modelo de tareas."""
    #TODO: Utilizar el campo created_by en un futuro,
    #agregar fechas de vencimiento para las tareas
    
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
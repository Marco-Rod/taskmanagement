from celery import shared_task
from django.core.mail import send_mail

from config.settings.base import EMAIL_HOST_USER


@shared_task(bind=True)
def send_notification_email(self, target_mail, title, message, mail_subject):
    """
    Envía un correo electrónico de manera asincrona al usuario que se le asignó la tarea
    haciendo uso de Celery.
    """
    full_message = format_full_message(title, message)
    send_mail(
        subject=mail_subject,
        message=full_message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return 'Email sent successfully'


def format_full_message(title, message):
    return "Titulo: " + title + '\n' + "Descripcion: " + message

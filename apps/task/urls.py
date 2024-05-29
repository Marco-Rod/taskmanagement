from django.urls import path
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from .views import TaskView, TaskUpdateView, TaskDeleteView, TaskListView, TaskViewSet

app_name = 'task'

router = DefaultRouter()
router.register('api/tasks', TaskViewSet, basename='tasks')
urlpatterns = [
    path('create/', TaskView.as_view(), name='create_task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('list/', TaskListView.as_view(), name='list_task'),

   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls

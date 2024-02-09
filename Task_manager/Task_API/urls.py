from django.urls import path
from Task_API.views import TaskListAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task-list-api'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail-api'),
]

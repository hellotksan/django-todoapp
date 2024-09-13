from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate,  TaskUpdate, TaskDelete
from .views import TaskListLogin, RegisterTodoApp
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', TaskUpdate.as_view(), name='edit-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    path('login/', TaskListLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='tasks'), name='logout'),
    path('register/', RegisterTodoApp.as_view(), name='register'),
]

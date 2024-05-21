from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),

    path('register/', views.register, name='register'),

    path('my-login/', views.my_login, name='my_login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('create-task/', views.createTask, name='create_task'),

    path('upadte-task/<str:pk>', views.updateTask, name='update_task'),

    path('delete-task/<str:pk>', views.deleteTask, name='delete_task'),

    path('view-tasks/', views.viewTasks, name='view_tasks'),

    path('profile/', views.profile, name='profile'),

    path('delete-account/', views.deleteAccount, name='delete_account'),

    path('logout/', views.logout, name='logout'),

]
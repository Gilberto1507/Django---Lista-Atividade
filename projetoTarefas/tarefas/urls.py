from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.nova_tarefa, name='nova_tarefa'),
    path('<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:pk>/alternar/', views.alternar_status, name='alternar_status'),
]
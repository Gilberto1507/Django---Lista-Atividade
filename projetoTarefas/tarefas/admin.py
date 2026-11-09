from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ["titulo", "prioridade", "concluida", "criada_em"]
    
    # Filtros laterais
    list_filter = ["prioridade", "concluida"]
    
    # Barra de pesquisa
    search_fields = ["titulo"]
    
    # Quantidade de itens por página
    list_per_page = 20
    
    # Campo que não pode ser editado
    readonly_fields = ["criada_em"]
    
    # Organização do formulário em secções
    fieldsets = [
        ("Informações da tarefa", {"fields": ["titulo", "descricao", "prioridade"]}),
        ("Status", {"fields": ["concluida", "criada_em"]}),
    ]
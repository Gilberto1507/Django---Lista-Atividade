from django.db import models

class Tarefa(models.Model):
    # Opções que vão aparecer para a prioridade
    OPCOES_PRIORIDADE = [
        ("Baixa", "Baixa"),
        ("Media", "Média"),
        ("Alta", "Alta"),
    ]

    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True, null=True)
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
from django.db import models

class Agendamento(models.Model):
    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length=150)
    email_cliente = models.CharField(max_length=150)
    telefone_cliente = models.CharField(max_length=20)

    
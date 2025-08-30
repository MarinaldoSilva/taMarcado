from .models import Agendamento
from rest_framework import serializers 

class AgendamentoSerializer(serializers.ModelSerializer):
    model : Agendamento
    fields = [
        'data_horario',
        'nome_cliente',
        'email_cliente',
        'telefone_cliente',
    ]
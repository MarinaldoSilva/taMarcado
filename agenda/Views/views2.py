from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Agendamento
from ..serializers import AgendamentoSerializer
from rest_framework.decorators import api_view

@api_view(http_method_names=['GET'])
def agendamentoDetail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    serializer_class = AgendamentoSerializer(obj)
    return JsonResponse(serializer_class.data)

@api_view(http_method_names=['GET'])
def agendamentoList(request):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data)#safe=False
    #jsonResponse por padrão só aceita retornar objs do tipo dicionario, e no serializer.data retorna uma lista
    #com dicionarios, por isso temos que adicionar o o safe=False para permiir que seja retornar uma lista


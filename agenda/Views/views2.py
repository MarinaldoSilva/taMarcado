from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Agendamento
from ..serializers import AgendamentoSerializer
from rest_framework.request import Request
from rest_framework.decorators import api_view

"""com esse decorator, minha função recebe somente pedidos via GET"""
@api_view(http_method_names=['GET'])
def agendamentoDetail(request : Request, id):
    obj = get_object_or_404(Agendamento, id=id)
    serializer_class = AgendamentoSerializer(obj)
    return JsonResponse(serializer_class.data)

@api_view(http_method_names=['GET','POST'])
def agendamentoList(request: Request):
    queryset = Agendamento.objects.all()

    if request.method == "GET":
        serializer_class = AgendamentoSerializer(queryset, many=True) #many diz que vai receber uma coleção de dados
        return JsonResponse(serializer_class.data)#safe=False
        #jsonResponse por padrão só aceita retornar objs do tipo dicionario, e no serializer.data retorna uma lista
        #com dicionarios, por isso temos que adicionar o o safe=False para permiir que seja retornar uma lista
    
    if request.method == "POST":
        dados = request.data
        serializer = AgendamentoSerializer(data=dados)
        if serializer.is_valid():
            dados_validos = serializer.validated_data
            "se is_valid() é chamado e retorna como válido, a função validated_data fica disponivel para uso no meu serializer, e ele serve para confirmar que ambos os dados de chave são o mesmo popula os dados, caso retorne false, a função erros vai ser liberada para usar, o mesmo que usamos no else"
            created_agendamento = Agendamento.objects.create(
                data_horario = dados_validos['data_horario'],
                nome_cliente = dados_validos['nome_cliente'],
                email_cliente = dados_validos['email_cliente'],
                telefone_cliente = dados_validos['telefone_cliente']
            )
            return JsonResponse(serializer.data, status = 201)

        else:
            return JsonResponse(serializer.errors, status = 400)
"""salvei os dados em uma variavel chamada dados, essa variavel tem os dados do meu request, na variavel serializer = Agendam...(data =dados) o data(parametro) é um atributo especial que vai receber os dados e como esses dados estão sendo passado para o meu serializer(ao inves de passar um obj do tip, estamos comparando se os dados que estão no meu serializer são os mesmos que já foram predefindos no meu AgendamentoSerializer, caso seja vai ser possível criar um novo agendamento com os dados do meu request.data salvos na variavel dados.)"""
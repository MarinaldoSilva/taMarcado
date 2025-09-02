from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from ..models import Agendamento
from ..serializers import AgendamentoSerializer
from rest_framework.request import Request
from rest_framework.decorators import api_view

"""com esse decorator, minha função recebe somente pedidos via GET""" #partial=partial_update
@api_view(http_method_names=['GET', 'PUT', 'PATCH'])
def agendamentoDetail(request : Request, pk):
    
    agenda = get_object_or_404(Agendamento, pk=pk)

    if request.method == "GET":    
        serializer = AgendamentoSerializer(agenda)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = AgendamentoSerializer(instance=agenda, data = request.data)
        """instance diz que vai ser uma atualização, sem isso vira o create. Os dados originais estão no instance, os novos estão no request.data"""
        if serializer.is_valid():
            """compara os campos(meu fields do serializer, se faltar algum, não é PUT e PATCH) e faz a validação campo por campo e vê se esta de acordo com o nosso models, limpa os campos e converte os dados para o tipo python, e caso tudo esteja ok, ele cria e popula o ##serializer.validated_data## e nesse dicionario de dados esta os dados já verificados"""
            agenda.save() 
            """para cada chave ##par:valor## no dic(validated_data) é feita a atualização no meu instance que recebeu agenda e atualiza todos so campos e após isso o save() é executado chamando o update() para persistir no banco"""
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "PATCH":
        serializer = AgendamentoSerializer(instance=agenda, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=400)
    

@api_view(http_method_names=['GET','POST'])
def agendamentoList(request: Request):
    queryset = Agendamento.objects.all()

    if request.method == "GET":
        serializer_class = AgendamentoSerializer(queryset, many=True) #many diz que vai receber uma coleção de dados
        return Response(serializer_class.data)#safe=False
        #jsonResponse por padrão só aceita retornar objs do tipo dicionario, e no serializer.data retorna uma lista
        #com dicionarios, por isso temos que adicionar o o safe=False para permiir que seja retornar uma lista
    
    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            dados_validos = serializer.validated_data
            "se is_valid() é chamado e retorna como válido, a função validated_data fica disponivel para uso no meu serializer, e ele serve para confirmar que ambos os dados de chave são o mesmo popula os dados, caso retorne false, a função erros vai ser liberada para usar, o mesmo que usamos no else"
            created_agendamento = Agendamento.objects.create(
                data_horario = dados_validos['data_horario'],
                nome_cliente = dados_validos['nome_cliente'],
                email_cliente = dados_validos['email_cliente'],
                telefone_cliente = dados_validos['telefone_cliente']
            )
            return Response(serializer.data, status = 201)

        else:
            return Response(serializer.errors, status = 400)
"""salvei os dados em uma variavel chamada dados, essa variavel tem os dados do meu request, na variavel serializer = Agendam...(data =dados) o data(parametro) é um atributo especial que vai receber os dados e como esses dados estão sendo passado para o meu serializer(ao inves de passar um obj do tip, estamos comparando se os dados que estão no meu serializer são os mesmos que já foram predefindos no meu AgendamentoSerializer, caso seja vai ser possível criar um novo agendamento com os dados do meu request.data salvos na variavel dados.)"""
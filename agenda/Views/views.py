from ..serializers import AgendamentoSerializer
from ..models import Agendamento
from rest_framework import generics


"""com o ListCreate, além reronar todos os meus objs e os serializa um por um
também cria um obj, e faz isso dependendo o verdo que esta na requisição"""
class AgendametoListCreateView(generics.ListCreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer


"""utilizando as generics, ao invés de fazer manualmente, a própira generics faz por mim
a RetriveUpdateDestroy já sabe o que fazer de acordo com o verbo recebido na requisiçao
GET, PUT, PATCH, DELETE. Não é mais preciso fazer tudo manualmente"""
class AgendamentoRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer



        
    


    

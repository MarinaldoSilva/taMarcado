from .serializers import AgendamentoSerializer
from .models import Agendamento
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class AgendamentoDetailView(APIView):

    def agendamento_detail(request : HttpRequest, id_param):
        try:
            agendamento = Agendamento.objects.get(id=id_param)
            serializer = AgendamentoSerializer(agendamento)

            return Response(
                {'agendamento': serializer.data},
                status=status.HTTP_200_OK
            )
        
        except ObjectDoesNotExist as e:
            return Response(
                {"detail": "Agendamento não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    


    

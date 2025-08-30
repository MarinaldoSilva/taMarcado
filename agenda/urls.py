from django.urls import include, path
from views import agendamento_detail

urlpatterns = [
    path("agendamentos/<int: id>", agendamento_detail)#trocar por as_view() do pacote APIView
]
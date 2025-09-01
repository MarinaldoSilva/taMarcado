from django.urls import path
from agenda.Views.views2 import agendamentoDetail, agendamentoList
from agenda.Views.views import AgendametoListCreateView, AgendamentoRetriveUpdateDestroyView

urlpatterns = [
    path("agendamentos/", AgendametoListCreateView.as_view(), name= "agendamento-list"),
    path("agendamentos/<int:pk>", AgendamentoRetriveUpdateDestroyView.as_view(), name="agendamento-detail"),

    path("agendamentos_n/<int:pk>/", agendamentoDetail, name="agendamento-detail"),
    path("agendamentos_n/", agendamentoList, name="agendamento_list")
]


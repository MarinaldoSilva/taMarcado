from django.urls import path
from agenda.Views.views import AgendametoListCreateView, AgendamentoRetriveUpdateDestroyView

urlpatterns = [
    path("agendamentos/", AgendametoListCreateView.as_view(), name= "agendamento-list"),
    path("agendamentos/<int:id>", AgendamentoRetriveUpdateDestroyView.as_view(), name="agendamento-detail")
    
]
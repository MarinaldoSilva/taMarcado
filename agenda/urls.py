from django.urls import include, path
from views import AgendamentoDetailView

urlpatterns = [
    path("agendamentos/<int: id>", AgendamentoDetailView.as_view(), name="agendamento-detail")
]
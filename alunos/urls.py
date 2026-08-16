from django.urls import path
from .views import dashboard, detalhe_aluno


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("alunos/<int:id>/", detalhe_aluno, name="detalhe_aluno"),
]





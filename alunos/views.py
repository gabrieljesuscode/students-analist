from django.shortcuts import render, get_object_or_404
from .models import Aluno

# Create your views here.


def dashboard(request):
	alunos = Aluno.objects.all()
	
	for aluno in alunos:
		if aluno.esta_em_risco():
			aluno.status = "ATENÇÃO"
		else:
			aluno.status = "OK"

	return render(request, "dashboard.html", {
		"alunos": alunos
	})



def detalhe_aluno(request, id):

	aluno = get_object_or_404(Aluno, id=id)

	return render(request, "detalhe_aluno.html", {
		"aluno": aluno
	})
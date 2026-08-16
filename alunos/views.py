from django.shortcuts import render
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



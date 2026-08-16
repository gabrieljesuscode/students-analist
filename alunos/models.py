from django.db import models

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(max_length=150)
	matricula = models.CharField(max_length=50, unique=True)
	turma = models.CharField(max_length=50)
	frequencia = models.FloatField()

	def esta_em_risco(self):
		if self.frequencia < 75:
			return True

		for nota in self.notas.all():
			if nota.media() < 7:
				return True

		return False

	

	def motivos_risco(self):
		motivos = []

		if self.frequencia < 75:
			motivos.append(
				"Frequência abaixo de 75%"
				)

		for nota in self.notas.all():
			if nota.media() < 7:
				motivos.append(
					f"Média baixa em {nota.disciplina}"
					)

		return motivos

	

	def __str__(self):
		return self.nome




class Nota(models.Model):
	aluno = models.ForeignKey(
		Aluno,
		on_delete=models.CASCADE,
		related_name="notas",
	)
	
	disciplina = models.CharField(max_length=100)
	nota1 = models.FloatField()
	nota2 = models.FloatField()

	def media(self):
		return (self.nota1 + self.nota2) / 2

	def __str__(self):
		return f"{self.aluno.nome} - {self.disciplina}"


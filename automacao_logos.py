dados_alunos = [
    {"nome": "Gabriel Jesus", "nota1": 8.5, "nota2": 9.0, "frequencia": 95},
    {"nome": "João Silva", "nota1": 4.0, "nota2": 5.5, "frequencia": 70},
    {"nome": "Maria Souza", "nota1": 7.0, "nota2": 8.0, "frequencia": 88},
]

print("--- PROCESSANDO DADOS ACADÊMICOS ---\n")

for aluno in dados_alunos:
	media = (aluno["nota1"] + aluno["nota2"]) / 2
	
	if media < 7 or aluno["frequencia"] < 75:
		status = "EM RISCO"
	else:
		status = "OK"


	print(
	f"Aluno: {aluno['nome']} | "
	f"Média: {media:.1f} | "
	f"Frequência: {aluno['frequencia']}% | "
	f"Status: {status}"
	)

print("--- PROCESSAMENTO CONCLUÍDO ---")

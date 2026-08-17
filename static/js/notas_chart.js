document.addEventListener('DOMContentLoaded', function () {

    // 1. Pega os dois elementos que o HTML preparou pra gente:
    //    o <canvas> onde o gráfico será desenhado
    //    e a tag <script> que guarda os dados em JSON
    var canvas = document.getElementById('notasChart');
    var dataEl = document.getElementById('disciplinas-data');

    // Se a página não tiver esses elementos, não faz nada
    if (!canvas || !dataEl) {
        return;
    }

    // 2. Transforma o texto JSON em um array de objetos JavaScript
    // Exemplo do resultado: [{ nome: "Matemática", nota1: 8, nota2: 7 }, ...]
    var disciplinas = JSON.parse(dataEl.textContent);

    // 3. Uma cor fixa para cada matéria 
    var cores = ['#3b82f6', '#facc15', '#22c55e', '#f97316', '#ef4444', '#8b5cf6', '#06b6d4', '#ec4899', '#14b8a6'];

    // 4. Monta uma "linha" do gráfico para cada matéria
    var datasets = [];

    for (var i = 0; i < disciplinas.length; i++) {
        var materia = disciplinas[i];

        datasets.push({
            label: materia.nome,
            data: [materia.nota1, materia.nota2],
            borderColor: cores[i]
        });
    }

    // 5. Cria o gráfico de linhas
    new Chart(canvas, {
        type: 'line',
        data: {
            labels: ['1º Bimestre', '2º Bimestre'],
            datasets: datasets
        }
    });

});
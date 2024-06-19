let dados;
let doenca = null;
let perguntasRestantes;
let perguntasFeitas = [];

document.addEventListener('DOMContentLoaded', () => {
    fetch('perguntas.csv')
        .then(response => response.text())
        .then(csvText => {
            dados = Papa.parse(csvText, { header: true }).data;
            perguntasRestantes = Object.keys(dados[0]).slice(1);
            mostrarProximaPergunta();
        })
        .catch(error => console.error('Erro ao carregar o CSV:', error));
});

function mostrarProximaPergunta() {
    if (dados.length === 1) {
        doenca = dados[0]['Doenca'];
        mostrarResultado();
        return;
    }

    if (dados.length === 0 || perguntasRestantes.length === 0) {
        doenca = 'Desconhecida';
        mostrarResultado();
        return;
    }

    let respostas = perguntasRestantes.map(pergunta => {
        return dados.reduce((acc, curr) => acc + Number(curr[pergunta]), 0);
    });

    let perguntaRodada = perguntasRestantes[respostas.indexOf(Math.max(...respostas))];
    perguntasFeitas.push(perguntaRodada);

    document.getElementById('question').textContent = `${perguntaRodada}?`;
    document.getElementById('question-container').classList.remove('hidden');
}

function handleResponse(resposta) {
    let perguntaRodada = perguntasFeitas[perguntasFeitas.length - 1];

    if (resposta === 'S') {
        dados = dados.filter(row => Number(row[perguntaRodada]) === 1);
    } else if (resposta === 'N') {
        dados = dados.filter(row => Number(row[perguntaRodada]) === 0);
    }

    perguntasRestantes = perguntasRestantes.filter(pergunta => pergunta !== perguntaRodada);

    mostrarProximaPergunta();
}

function mostrarResultado() {
    document.getElementById('question-container').classList.add('hidden');
    document.getElementById('result').textContent = `A resposta é ${doenca}`;
    document.getElementById('result-container').classList.remove('hidden');
}
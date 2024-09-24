// window.document.getElementById('title');
// window.document.getElementById('title').remove();


function remover() {
    window.document.getElementById('title').remove();
}

function adicionar() {
    // Cria um novo elemento h1
    const novoTitulo = document.createElement('h1');

    // Adiciona o texto ao novo elemento
    novoTitulo.textContent = 'Título da Página';
    
    // Define o id como 'title'
    novoTitulo.id = 'title';
    
    // Adiciona o elemento de volta ao corpo da página
    document.body.appendChild(novoTitulo);
}
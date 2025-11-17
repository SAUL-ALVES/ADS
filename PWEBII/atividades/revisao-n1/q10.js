//Complete as lacunas com os métodos corretos e escreva um código mínimo que: cria um <li>, adiciona texto e insere no final de uma <ul id="lista">:

// Criar: document._________('li'). R: document.createElement('li')

//Inserir dentro de um elemento já selecionado: element._________(child) R: element.appendChild(child)

//Remover um nó filho: parent._________(child). R: parent.removeChild(child)

const ul = document.getElementById('lista');

const li = document.createElement('li')
li.textContent = "Novo item";
ul.append(li);
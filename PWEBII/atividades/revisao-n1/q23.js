let filmes = [];

function addDelegatedEventListener(parent, type, selector, handler){
    parent.addEventListener(type, function (event){
        if (event.target.matches(selector)){
            handler(event);
        }
    });
}

const filmeInput = document.getElementById("filmeIn");
const addBtn = document.getElementById("addBtn");
const filtroIn = document.getElementById("filtroIn");
const listaFilmes = document.getElementById("listaFilmes");

addBtn.addEventListener('click', () => {
    const nome = filmeInput.value.trim();
    if (!nome) return;
    
    filmes.push(nome);

    const li = document.createElement("li");
    li.innerHTML = `
      ${nome}
      <button class="remover">remover</button>
    `;
    listaFilmes.appendChild(li);

    filmeInput.value = "";
});

addDelegatedEventListener(listaFilmes, 'click', ".remover", (event) => {
    const li = event.target.closest("li");
    const nome = li.firstChild.textContent.trim();

    filmes = filmes.filter(f => f !== nome);

    li.remove();

    
});

filtroIn.addEventListener("input", () => {
    const texto = filtroIn.value.toLowerCase();

    const filtrados = filmes.filter(f => f.toLowerCase().includes(texto));

    Array.from(listaFilmes.children).forEach(li => {
        const nome = li.firstChild.textContent.trim().toLowerCase();
        li.style.display = filtrados.includes(nome) ? "list-tem" : "none"
    });

});
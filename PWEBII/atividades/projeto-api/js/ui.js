export function mostrarLoading(msg) {
    document.getElementById("status").textContent = msg;
  }
  
  export function renderizarLista(pokemons) {
    const lista = document.getElementById("lista");
    lista.innerHTML = "";
  
    pokemons.forEach(pokemon => {
      const li = document.createElement("li");
      li.textContent = pokemon.name;
      lista.appendChild(li);
    });
  }
  
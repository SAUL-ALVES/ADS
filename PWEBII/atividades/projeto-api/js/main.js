import { buscarPokemons } from "./api.js";
import { mostrarLoading, renderizarLista } from "./ui.js";

const btn = document.getElementById("btnBuscar");

btn.addEventListener("click", async () => {
  try {
    mostrarLoading("Carregando...");

    const dados = await buscarPokemons();
    renderizarLista(dados.results);

    mostrarLoading("Dados carregados com sucesso!");
  } catch (erro) {
    mostrarLoading("Erro ao buscar dados da API");
  }
});

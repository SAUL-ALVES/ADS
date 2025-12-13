export async function buscarPokemons() {
    const response = await fetch("https://pokeapi.co/api/v2/pokemon?limit=10");
  
    if (!response.ok) {
      throw new Error("Erro na requisição");
    }
  
    return response.json(); 
  }
  
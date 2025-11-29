import { calcularMedia, VALOR_PI } from "./utils/calculadora.js";
import buscarDados from "./services/dados.js";

async function main(){
    const dados = await buscarDados();

    const media = calcularMedia(dados);

    console.log("Dados:", dados);
    console.log("Média:", media);
    console.log("Valor de PI", VALOR_PI);

}

main();
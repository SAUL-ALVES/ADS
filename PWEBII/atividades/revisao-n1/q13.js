//“Funções puras podem ler e alterar variáveis globais desde que retornem sempre o mesmo valor.” Avalie e justifique com um contraexemplo.

//R: Esta afirmação está incorreta, pois uma função pura não pode ter nenhum tipo de efeito colateral externo. Ela deve sempre retornar o mesmo resultado para os mesmos argumentos (determinismo).


//Contraexemplo:
let multiplicador = 2;

function multiplica(num){
    return num * multiplicador;
}

console.log(multiplica(3)); //6
multiplicador = 4;
console.log(multiplica(3)); //12


//Torna-se impura, pois começa a depender de uma variável externa que pode ser redefinida.



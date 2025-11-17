function aplicarTaxa(taxa) {
    return function (valor) {
      return valor + valor * taxa;
    };
  }

const aplicarICMS = aplicarTaxa(0.18); 
const aplicarIPI  = aplicarTaxa(0.10); 

console.log(aplicarICMS(100)); 
console.log(aplicarIPI(100));  

//Closure:

//É quando uma função lembra do ambiente onde foi criada, mesmo depois desse ambiente ter sido executado.
//Neste caso, a função retornada lembra da taxa.


//Currying:

//É a técnica de transformar uma função que recebe múltiplos parâmetros
//f(a, b)
//em uma cadeia de funções
//g(a)(b).
//Explique o conceito de lazy evaluation e comente sobre como essa técnica é empregada, bem como qual a sua vantagem, com base no trecho de código a seguir:

function lazyMap(arr, fn){
    return { get: i => fn(arr[i]), size: () => arr.length };
  }
  
  
  const values = [129.9, 99.5, 24.69, 54.65];
  
  const valuesWithDiscount = lazyMap(values, (value) => value * (1 - 0.1));
  
  console.log(valuesWithDiscount.get(0));

  //R: Lazy evaluation significa adiar o cálculo até o momento exato em que ele é necessário. O valor não é pré-computado; ele só é gerado quando você realmente pede. Em vez de: transformar todo o array na hora (map tradicional), você transforma somente o elemento que foi acessado.


//A função não cria um novo array transformado. Ela retorna um objeto com métodos que permitem acessar os valores sob demanda:

//get(i) → só aplica a função fn ao elemento do índice i na hora que você chama
//size() → só retorna o comprimento original

//A verdadeira vantagem está em não pagar o custo de uma transformação completa quando você só precisa de parte dela.

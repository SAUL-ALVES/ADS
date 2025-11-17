//a)Explique composition (da direita para a esquerda) e pipe (da esquerda para a direita).
//R: 
// Compose:
//A composição tradicional aplica funções da direita para a esquerda.
//Ou seja, compose(f, g)(x) significa f(g(x)).

//Pipe:
//O pipe faz o oposto: aplica funções da esquerda para a direita.
//pipe(f, g)(x) significa g(f(x)).

const somar1 = x => x + 1;
const dup = x => x * 2;


const compose = (...fns) => x =>
  fns.reduceRight((acc, fn) => fn(acc), x);


const resultadoCompose = compose(dup, somar1)(5);
console.log(resultadoCompose); // 12


const pipe = (...fns) => x =>
  fns.reduce((acc, fn) => fn(acc), x);


const resultadoPipe = pipe(somar1, dup)(5);
console.log(resultadoPipe); // 12


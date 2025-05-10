/*1. If-Else
A estrutura if-else é usada para executar blocos de código com base em condições. Se a condição for verdadeira, o bloco if é executado; caso contrário, o bloco else é executado.*/

const idade = 18;

if (idade >= 18) {
    console.log('Você é maior de idade.');
} else {
    console.log('Você é menor de idade.');
}

/*2. Tipos Primitivos
Os tipos primitivos em JavaScript incluem:

String: Cadeia de caracteres.
*/
const nome = "Alice";
/*Number: Números, incluindo inteiros e floats.*/


const idade1 = 25; // inteiro
const altura = 1.75; // float
//Boolean: Valores verdadeiros ou falsos.


const isAdult = true;

//Undefined: Variável que não foi atribuída a um valor.


let x;
console.log(x); // Saída: undefined

//Null: Valor intencionalmente vazio ou nulo.


const y = null;


/*3. Laços de Repetição
Os laços de repetição permitem executar um bloco de código várias vezes.

For Loop:

*/

for (let i = 0; i < 5; i++) {
    console.log(`Número: ${i}`);
}
//While Loop:

let j = 0;
while (j < 5) {
    console.log(`Número: ${j}`);
    j++;
}

/*4. Operadores Aritméticos
Os operadores aritméticos são usados para realizar cálculos.

Adição (+):*/


const soma = 5 + 3; // 8

//Subtração (-):


const subtracao = 10 - 4; // 6

//Multiplicação (*):


const multiplicacao = 7 * 2; // 14

//Divisão (/):


const divisao = 20 / 4; // 5


/*5. Operadores Booleanos
Os operadores booleanos são usados para realizar operações lógicas.

E (&&):
*/

const a = true;
const b = false;
console.log(a && b); // Saída: false

//OU (||):


console.log(a || b); // Saída: true

//NÃO (!):


console.log(!a); // Saída: false
/*6. Vetores
Os vetores (ou arrays) são usados para armazenar listas de valores.

Exemplo de declaração de vetores:*/


const frutas = ['maçã', 'banana', 'laranja'];
console.log(frutas[1]); // Saída: banana

/*7. Funções
Funções são blocos de código que podem ser chamados para executar uma tarefa específica. Elas podem receber parâmetros e retornar valores.

Exemplo de função:*/


function soma(a, b) {
    return a + b;
}

const resultado = soma(5, 3);
console.log(resultado); // Saída: 8
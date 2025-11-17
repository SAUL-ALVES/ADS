//const não pode "congelar" um array/objeto, pois ele não impede que a estrutura interna seja modificada,
// mas sim o ponteiro da variável que estamos atribuindo tal objeto/array. Em resumo, só congelamos a variável

//Ex:

const array = ["Jonas", "Lucas", "Cesar"]

const array2 = [...array, "Paulo"];

console.log(array); //[ 'Jonas', 'Lucas', 'Cesar' ]
console.log(array2); //[ 'Jonas', 'Lucas', 'Cesar', 'Paulo' ]
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Digite um valor em reais: R$ ", (real) => {
    rl.question("Digite a cotação do dolar atual: ", (cotacao) => {
    const dolar = real / cotacao;
    console.log(`O valor de R$ ${real} reais, em dólar é U$D ${dolar.toFixed(2)} dólares`);
    rl.close();    
    });
});
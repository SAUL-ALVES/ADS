const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Digite o valor do raio da circunferência: ", (raio) => {
    const pi = 3.14;
    const P = 2 * pi * raio;
    console.log(`O valor do perímetro desta cirfunferência é: ${P}`);
    rl.close;
});
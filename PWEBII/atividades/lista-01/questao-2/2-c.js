const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.question("Digite sua nota na etapa N1: ", (N1) => {
    rl.question("Digite sua nota na etapa N2: ", (N2) => {
        
    const NotaFinal = ((N1 * 2) + (N2 * 3)) / 5.0

    if (NotaFinal >= 7.0) {
        console.log(`Sua nota foi: ${NotaFinal}, então APROVADO!`);
    } 
    else {
        console.log(`Sua nota foi: ${NotaFinal}, então REPROVADO!`);
    } 

    rl.close();  

    });
});
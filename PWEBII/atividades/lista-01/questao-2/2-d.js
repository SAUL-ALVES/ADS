const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let soma = 0;
let contador = 0;
let total = 0;
let numeros = [];


rl.question("Quantos números você quer digitar? ", (n) => {
  total = parseInt(n);

  
  function lerNumero() {
    if (contador < total) {
      rl.question(`Digite o ${contador + 1}º número: `, (num) => {
        num = parseInt(num);

        
        let primo = true;
        if (num < 2) {
          primo = false;
        } else {
          for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
              primo = false;
              break;
            }
          }
        }

        
        if (primo) {
          soma += num;
        }

        contador++;
        lerNumero(); 
      });
    } else {
      console.log(`A soma dos números primos é: ${soma}`);
      rl.close();
    }
  }

  lerNumero(); 
});

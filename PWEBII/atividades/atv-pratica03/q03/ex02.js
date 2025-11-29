class ContaBancaria {
    #saldo

    constructor(saldo){
        this.#saldo = 0;
    }

    depositar(valor){
        return this.#saldo += valor;
    }

    sacar(valor){

        if (valor <= this.#saldo){
            return this.#saldo -= valor;
        }else{
            "Saldo insuficiente!"
        }
        
    }

    consultarSaldo(){
        return console.log(this.#saldo);
    }
}

const conta = new ContaBancaria();
//conta.#saldo = 100; //Erro: Private field '#saldo' must be declared in an enclosing class

//OU seja, o atributo saldo só pode ser acessado dentro da classe, pois é privado. Isso garante a proteção dos dados com o encapsulamente, impossibilitando que em subclasses ou até mesmo fora da classe, este atributo seja acessado.

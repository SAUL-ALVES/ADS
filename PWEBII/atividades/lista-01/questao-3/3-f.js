const contaBancaria = { 
    saldo: 1000,
    numeroConta: 12345,

    depositar(valor) {
        if (valor <= 0) {
            return "Insira um valor válido para depósito!";
        }
        this.saldo += valor;
        return `Depósito de R$${valor} realizado. Novo saldo: R$${this.saldo}`;
    },

    sacar(valor) {
        if (valor <= 0) {
            return "Valor inválido para saque!";
        }
        if (valor > this.saldo) {
            return "Saldo insuficiente!";
        }
        this.saldo -= valor;
        return `Saque de R$${valor} realizado. Novo saldo: R$${this.saldo}`;
    },

    informarSaldo() {
        return `Seu saldo atual é de R$${this.saldo}`;
    }
};



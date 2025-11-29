class Usuario {
    constructor(nome, email){
        this.nome = nome;
        this.email = email;
    }

    exibirInfo() {
        return console.log(`Bem vindo ${this.nome}, seu email é ${this.email}`);        
    }
}

class Administrador extends Usuario{
    constructor(nome, email, nivelAcesso){
        super(nome, email);
        this.nivelAcesso = nivelAcesso;
    }

    exibirInfo(){
        super.exibirInfo();
        console.log(`Nível de acesso: ${this.nivelAcesso}`);
    }

}

const usuario = new Usuario("Saul", "saul@gmail");
const adm = new Administrador("Saul", "saul@gmail", "super-adm");


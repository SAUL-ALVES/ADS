//Seleção: Nesta etapa selecionamos um elemento para podermos manipulá-lo, caso contrário seria um tiro no escuro.
//Binding: Aqui, registramos um listener para um tipo de evento. É aqui que diz: quando X acontecer, execute Y".
//Callback: Aqui é a parte de implementação da função quando escutamos um evento. É onde está a lógica real: impedir ações padrão, validar dados, alterar classes etc.

const form = document.getElementById('formLogin');
const email = document.getElementById('emailInput');
const msg = document.getElementById('msgErro');

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const vazio = email.value.trim() === "";

    if (vazio) {
        msg.classList.add('error');
        msg.textContent = "Preencha o e-mail.";
    } else {
        msg.classList.remove('error');
        msg.textContent = "";
    }
});

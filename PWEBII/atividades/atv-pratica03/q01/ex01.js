
const respostaApi = { 
    id: 101,
    username: "user_a",
    email: "a@ex.com",
    status: "ativo"
 }

//Destructuring de Objeto 
const {username, email} = respostaApi; 

//Rest Operator em Objeto
const {id, ...dadosComplementares} = respostaApi;

//Spread Operator
const configPadrao = {
    tema: 'dark',
    notificacoes: true
};

const configUsuario = {
    tema: 'light',
    notificacoes: false
  };

const configFinal = {
    ...configPadrao,
    ...configUsuario
};


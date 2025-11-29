const configuracoes = {
    cache: null
};

const expiracaoSegura = configuracoes.cache?.tempoExpiracao;


const tempoExpiracaoAPI = configuracoes.cache?.tempoExpiracao;
const tempoFinal = tempoExpiracaoAPI ?? 600;

console.log("Expiração segura:", expiracaoSegura);
console.log("Expiração final:", tempoFinal);

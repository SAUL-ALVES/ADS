const props = {
    id: "btn-submit",
    className: "btn-primary",
    onClick: () => {},
    "data-acao": "enviar",
    disabled: true,
    title: "Enviar formulário"
}

function prepararPropsBotao(props){
    const {id, className, onClick, ...atributosNativos} = props;

    const configuracaoPadrao = {
        id: 'default-id',
        type: 'button',
        disabled: false
    };

    const propsFinais = {
        ...configuracaoPadrao,
        ...atributosNativos,
        disabled: false
    };

    return propsFinais;

}

const resultado = prepararPropsBotao(props);
console.log(resultado);


//O Rest (...atributosNativos) pegou todas as propriedades que não foram desestruturadas (id, className, onClick) e as agrupou em um novo objeto.
//Assim, separou automaticamente o que pertence à lógica interna do botão do que deve ser repassado ao elemento HTML <button>.

//Ao montar propsFinais, a ordem é quem decide quem vence então o último valor sobrescreve os anteriores
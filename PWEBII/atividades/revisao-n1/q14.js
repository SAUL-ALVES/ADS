//Se você usa push, você muta o array original, ou seja, altera algo que está fora da função. Isso cria efeito colateral porque outro código que usa esse mesmo array passa a receber um valor diferente sem ter solicitado a mudança.

//Array imutável com spread operator:
function adicionarItem(arr, item){
    return [...arr, item];
}





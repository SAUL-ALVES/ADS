function compra(valorProduto, qtd, desconto = 0){
    const totalSemDesconto = valorProduto * qtd;
    const totalComDesconto = totalSemDesconto * (1 - desconto);

    return totalComDesconto;
}


function produtorio(...numeros){
    let resultado = 1;

    for (let n of numeros){
        resultado *= n;
    }

    return resultado;
}

console.log(produtorio(1, 9, 3));
function impares(...numeros){
    let impares = []
    for (let n of numeros){
        if (n % 2 == 1){
            impares.push(n);
        }
    }

    return impares;

}


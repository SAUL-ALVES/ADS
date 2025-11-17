function calculaImposto(valor, taxa = 0.1) {
    return valor * taxa;
  }
  console.log(calculaImposto(100, undefined));
  console.log(calculaImposto(100, null));

  // As saídas diferem pois, "undefined" é tratado como algo não definido ou declarado, mas continua não vazio.
  //Assim o default é acionado, chegando no valor que foi definido no parâmetro da função. Já "null", sempre é tratado como
  //um valor intencionalmente vazio, em caso de operações númericas ele torna-se zero. 
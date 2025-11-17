const pedidos = [
    { cliente: "A", total: 100 },
    { cliente: "B", total: 200 },
    { cliente: "A", total: 50  },
    { cliente: "C", total: 350 }
  ];


//map
const totais = pedidos.map(pedido => pedido.total);

console.log(totais);

//filter
const maiorQueDuz = pedidos.filter(pedido => pedido.total >= 200);

console.log(maiorQueDuz);

//reduce 
const soma = pedidos.reduce((acc, item) => acc + item.total, 0);

console.log(soma);
const vendas = [
    { produto: "Notebook", preco: 3500, quantidade: 1, status: "pago" },
    { produto: "Mouse", preco: 50, quantidade: 3, status: "pendente" },
    { produto: "Teclado", preco: 150, quantidade: 2, status: "pago" },
    { produto: "Monitor", preco: 1200, quantidade: 1, status: "pago" },
    { produto: "Webcam", preco: 80, quantidade: 5, status: "pendente" },
];


const listaVendasEl = document.getElementById("listaVendas");
listaVendasEl.innerHTML = vendas
    .map(v => `<li>${v.produto} - R$ ${v.preco} x ${v.quantidade} (${v.status})</li>`)
    .join("");


const compose = (...fns) => x =>
    fns.reduceRight((acc, fn) => fn(acc), x);


const filterVendasPagas = vendas =>
    vendas.filter(v => v.status === "pago");

const mapTotalItem = vendasPagas =>
    vendasPagas.map(v => v.preco * v.quantidade);

const reduceTotalGeral = totais =>
    totais.reduce((acc, t) => acc + t, 0);

const exibirTotal = totalGeral => {
    document.getElementById("totalGeral").textContent =
        `R$ ${totalGeral.toFixed(2)}`;
};


const calcularReceita = compose(
    reduceTotalGeral,
    mapTotalItem,
    filterVendasPagas
);


document.getElementById("calcularReceitaTotal")
    .addEventListener("click", () => {
        const total = calcularReceita(vendas);
        exibirTotal(total);
    });

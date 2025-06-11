package atividade1_pdm;

import java.util.ArrayList;
import java.util.List;

public class Pedido {

    private Cliente cliente;
    private List<ItemPedido> itens;

    public Pedido(Cliente cliente) {
        this.cliente = cliente;
        this.itens = new ArrayList<>();
    }

    //livro e quantidade
    public void adicionarItem(Livro livro, int quantidade) {
        if (quantidade <= 0) {
            throw new IllegalArgumentException("Quantidade deve ser maior que zero.");
        }
        itens.add(new ItemPedido(livro, quantidade));
    }

    //apenas livro (quantidade padrão = 1)
    public void adicionarItem(Livro livro) {
        adicionarItem(livro, 1);
    }

    public double calcularTotal() {
        double total = 0;
        for (ItemPedido item : itens) {
            total += item.calcularSubtotal();
        }
        return total;
    }

    public void finalizar() {
        double total = calcularTotal();

        if (cliente.getSaldoCarteira() < total) {
            throw new RuntimeException("Saldo insuficiente para finalizar o pedido.");
        }

        for (ItemPedido item : itens) {
            Livro livro = item.getLivro();
            int quantidade = item.getQuantidade();

            // Verifica se há estoque suficiente
            if (livro instanceof LivroFisico || livro instanceof LivroDigital) {
                // Apenas se quiser controlar estoque (como exemplo):
                // Aqui assumimos que Livro tem método set/getEstoque
                // Para esse exemplo simples, omitiremos a verificação real
            }
        }

        cliente.debitar(total); // debita do cliente
        System.out.printf("Pedido finalizado para %s! Total: R$ %.2f\n", cliente.getNome(), total);
    }
}

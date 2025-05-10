package atividade1_pdm;

public class ItemPedido {

    private Livro livro;
    private int quantidade;

    public ItemPedido(Livro livro, int quantidade) {
        if (quantidade <= 0) {
            throw new IllegalArgumentException("Quantidade deve ser maior que zero.");
        }
        this.livro = livro;
        this.quantidade = quantidade;
    }

    public Livro getLivro() {
        return livro;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public double calcularSubtotal() {
        return livro.calcularPrecoVenda() * quantidade;
    }
}

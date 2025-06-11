package atividade1_pdm;

public class Livro {

    private String titulo;
    private String autor;
    private int anoPublicacao;
    private double precoBase;
    protected int estoque;

    public Livro(String titulo, String autor, int anoPublicacao, double precoBase, int estoque) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        setPrecoBase(precoBase); // garante validação
        this.estoque = Math.max(estoque, 0); // impede estoque negativo

    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public double getPrecoBase() {
        return precoBase;
    }

    public void setPrecoBase(double precoBase) {
        if (precoBase >= 0) {
            this.precoBase = precoBase;
        } else {
            System.out.println("Preço base não pode ser negativo. Valor mantido.");
        }
    }

    public int getEstoque() {
        return estoque;
    }

    public void adicionarEstoque(int quantidade) {
        if (quantidade > 0) {
            this.estoque += quantidade;
        } else {
            System.out.println("Quantidade deve ser maior que zero.");
        }
    }

    // 1.2 Método exibirDetalhes()
    public String exibirDetalhes() {
        return String.format(
                "Título: %s\nAutor: %s\nAno de Publicação: %d\nPreço Base: R$ %.2f\nEstoque: %d",
                titulo, autor, anoPublicacao, precoBase, estoque
        );
    }

    // 1.3 b) Operação para remover do estoque
    public void removerEstoque(int quantidade) {
        if (quantidade > 0) {
            if (quantidade <= estoque) {
                this.estoque -= quantidade;
            } else {
                System.out.println("Quantidade a remover excede o estoque.");
            }
        } else {
            System.out.println("Quantidade deve ser maior que zero.");
        }
    }

    public double calcularPrecoVenda() {
        return precoBase;
    }

}

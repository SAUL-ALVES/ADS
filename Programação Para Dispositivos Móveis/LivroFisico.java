package atividade1_pdm;

public class LivroFisico extends Livro {

    private double pesoGramas;

    public LivroFisico(String titulo, String autor, int anoPublicacao, double precoBase, int estoque, double pesoGramas) {
        super(titulo, autor, anoPublicacao, precoBase, estoque);
        setPesoGramas(pesoGramas);
    }

    public double getPesoGramas() {
        return pesoGramas;
    }

    public void setPesoGramas(double pesoGramas) {
        if (pesoGramas > 0) {
            this.pesoGramas = pesoGramas;
        } else {
            System.out.println("Peso deve ser maior que zero.");
        }
    }

    public void setEstoque(int estoque) {
        this.estoque = estoque;
    }

    @Override
    public String exibirDetalhes() {
        return super.exibirDetalhes() + String.format("\nPeso: %.2f g", pesoGramas);
    }

    // Polimorfismo
    @Override
    public double calcularPrecoVenda() {
        return getPrecoBase() * 1.10 + 5.00;
    }
}

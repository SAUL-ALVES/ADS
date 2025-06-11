package atividade1_pdm;

public class LivroDigital extends Livro {

    private double tamanhoArquivoMB;

    public LivroDigital(String titulo, String autor, int anoPublicacao, double precoBase, int estoque, double tamanhoArquivoMB) {
        super(titulo, autor, anoPublicacao, precoBase, estoque);
        setTamanhoArquivoMB(tamanhoArquivoMB);
    }

    public double getTamanhoArquivoMB() {
        return tamanhoArquivoMB;
    }

    public void setTamanhoArquivoMB(double tamanhoArquivoMB) {
        if (tamanhoArquivoMB > 0) {
            this.tamanhoArquivoMB = tamanhoArquivoMB;
        } else {
            System.out.println("Tamanho do arquivo deve ser maior que zero.");
        }
    }

    public void setEstoque(int estoque) {
        this.estoque = estoque;
    }

    @Override
    public String exibirDetalhes() {
        return super.exibirDetalhes() + String.format("\nTamanho do Arquivo: %.2f MB", tamanhoArquivoMB);
    }

    //Polimorfismo
    @Override
    public double calcularPrecoVenda() {
        return getPrecoBase() * 0.85;
    }
}

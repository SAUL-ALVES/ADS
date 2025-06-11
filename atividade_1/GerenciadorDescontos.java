package atividade1_pdm;

public class GerenciadorDescontos {

    private static final double CUPOM10 = 0.10;
    private static final double CUPOM20 = 0.20;

    public static void aplicarDesconto(Livro livro, String cupom) {
        double preco = livro.getPrecoBase();
        switch (cupom) {
            case "CUPOM10":
                livro.setPrecoBase(preco * (1 - CUPOM10));
                break;
            case "CUPOM20":
                livro.setPrecoBase(preco * (1 - CUPOM20));
                break;
            default:
                System.out.println("Cupom inválido. Nenhum desconto aplicado.");
        }
    }
}

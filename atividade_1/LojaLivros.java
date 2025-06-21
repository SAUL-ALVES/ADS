package atividade1_pdm;

import java.util.List;

public class LojaLivros {

    public static void imprimirPrecosVenda(List<Livro> livros) {
        for (Livro livro : livros) {
            System.out.printf("Título: %s | Preço Final: R$ %.2f\n",
                    livro.getTitulo(), livro.calcularPrecoVenda());
        }
    }
}

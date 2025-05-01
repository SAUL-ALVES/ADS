
package atividade1_pdm;
import java.util.*;

public class Atividade1_PDM {

    public static void main(String[] args) {
        LivroFisico livro1 = new LivroFisico("O Senhor dos Anéis", "Tolkien", 1954, 100.0, 10, 700);
        LivroDigital livro2 = new LivroDigital("Clean Code", "Robert Martin", 2008, 80.0, 5, 3.0);

        List<Livro> lista = Arrays.asList(livro1, livro2);
        LojaLivros.imprimirPrecosVenda(lista);

        // Criar cliente
        Cliente cliente = new Cliente("João Silva", "joao@email.com", 200.0);

        // Relatório de estoque inicial
        System.out.println("\n📚 Estoque inicial:");
        System.out.println(livro1.getTitulo() + ": " + livro1.getEstoque() + " unidades");
        System.out.println(livro2.getTitulo() + ": " + livro2.getEstoque() + " unidades");
        System.out.println("💰 Saldo inicial do cliente: R$ " + cliente.getSaldoCarteira());

        // Aplicar cupons
        GerenciadorDescontos.aplicarDesconto(livro1, "CUPOM10");
        GerenciadorDescontos.aplicarDesconto(livro2, "CUPOM20");

        // Criar pedido
        Pedido pedido = new Pedido(cliente);
        pedido.adicionarItem(livro1, 1);
        pedido.adicionarItem(livro2);  

        // Exibir total do pedido
        System.out.printf("\n🛒 Total do pedido: R$ %.2f\n", pedido.calcularTotal());

        // Finalizar pedido
        pedido.finalizar();

        // Atualizar estoques manualmente (simulando venda)
        livro1.setEstoque(livro1.getEstoque() - 1);
        livro2.setEstoque(livro2.getEstoque() - 1);

        
        System.out.println("\n📦 Estoque após venda:");
        System.out.println(livro1.getTitulo() + ": " + livro1.getEstoque() + " unidades");
        System.out.println(livro2.getTitulo() + ": " + livro2.getEstoque() + " unidades");
        System.out.println("💰 Saldo final do cliente: R$ " + cliente.getSaldoCarteira());
    }
}

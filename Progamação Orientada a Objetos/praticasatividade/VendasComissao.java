/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 30
import java.util.Scanner;

public class VendasComissao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double salarioBase = 200.0;
        double comissaoPorcentagem = 0.09;
        double[] valoresItens = {239.99, 129.75, 99.95, 350.89};
        
        double totalVendas = 0;
        int itemVendido;
        
        System.out.println("Digite os itens vendidos (1 a 4). Digite 0 para finalizar.");
        
        while (true) {
            System.out.print("Digite o número do item vendido: ");
            itemVendido = scanner.nextInt();
            
            if (itemVendido == 0) {
                break;
            }
            
            if (itemVendido >= 1 && itemVendido <= 4) {
                totalVendas += valoresItens[itemVendido - 1];
            } else {
                System.out.println("Número de item inválido. Digite um número entre 1 e 4.");
            }
        }
        
        double comissao = totalVendas * comissaoPorcentagem;
        double rendimentoTotal = salarioBase + comissao;
        
        System.out.printf("Total de vendas: R$ %.2f\n", totalVendas);
        System.out.printf("Comissão: R$ %.2f\n", comissao);
        System.out.printf("Rendimento total: R$ %.2f\n", rendimentoTotal);
        
        scanner.close();
    }
}

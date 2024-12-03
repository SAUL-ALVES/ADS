/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;

//Questão 24

import java.util.Scanner;

public class FaturaTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número da fatura: ");
        String numero = scanner.nextLine();

        System.out.print("Digite a descrição do item: ");
        String descricao = scanner.nextLine();

        System.out.print("Digite a quantidade comprada: ");
        int quantidade = scanner.nextInt();

        System.out.print("Digite o preço por item: ");
        double precoPorItem = scanner.nextDouble();

        Fatura fatura = new Fatura(numero, descricao, quantidade, precoPorItem);

        System.out.println("\nDetalhes da Fatura:");
        System.out.println("Número: " + fatura.getNumero());
        System.out.println("Descrição: " + fatura.getDescricao());
        System.out.println("Quantidade: " + fatura.getQuantidade());
        System.out.println("Preço por Item: " + fatura.getPrecoPorItem());
        System.out.println("Valor Total da Fatura: " + fatura.getValorDaFatura());

        scanner.close();
    }
}


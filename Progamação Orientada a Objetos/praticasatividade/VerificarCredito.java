/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 29
import java.util.Scanner;

public class VerificarCredito {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o número da conta: ");
        int numeroConta = scanner.nextInt();
        
        System.out.print("Digite o saldo no início do mês: ");
        int saldoInicial = scanner.nextInt();
        
        System.out.print("Digite o total de itens cobrados no mês: ");
        int totalItensCobrados = scanner.nextInt();
        
        System.out.print("Digite o total de créditos aplicados ao cliente no mês: ");
        int totalCreditos = scanner.nextInt();
        
        System.out.print("Digite o limite de crédito autorizado: ");
        int limiteCredito = scanner.nextInt();
        
        int novoSaldo = saldoInicial + totalItensCobrados - totalCreditos;
        
        System.out.println("Novo saldo: " + novoSaldo);
        
        if (novoSaldo > limiteCredito) {
            System.out.println("Limite de crédito excedido");
        } else {
            System.out.println("Limite de crédito dentro do permitido");
        }
        
        scanner.close();
    }
}

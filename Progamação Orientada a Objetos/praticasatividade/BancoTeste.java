/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 23
import java.util.Scanner;

public class BancoTeste {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Conta minhaConta = new Conta();

        System.out.print("Digite o número da agência: ");
        minhaConta.setAgencia(scanner.nextLine());

        System.out.print("Digite o número da conta: ");
        minhaConta.setNumero(scanner.nextLine());

        System.out.print("Digite o valor do depósito inicial: ");
        double depositoInicial = scanner.nextDouble();
        minhaConta.depositar(depositoInicial);

        minhaConta.verSaldo();

        System.out.print("Digite o valor para sacar: ");
        double valorSaque = scanner.nextDouble();
        minhaConta.sacar(valorSaque);

        minhaConta.verSaldo();

        scanner.close();
    }
}


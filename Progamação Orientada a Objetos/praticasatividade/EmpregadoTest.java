/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 25
import java.util.Scanner;

public class EmpregadoTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Empregado empregado1 = new Empregado("Carlos", "Silva", 2500.00);
        Empregado empregado2 = new Empregado("Ana", "Oliveira", 3000.00);

        System.out.println("Salário Anual de " + empregado1.getPrimeiroNome() + " " + empregado1.getSobrenome() + ": " + empregado1.calcularSalarioAnual());
        System.out.println("Salário Anual de " + empregado2.getPrimeiroNome() + " " + empregado2.getSobrenome() + ": " + empregado2.calcularSalarioAnual());

        empregado1.aplicarAumento(10);
        empregado2.aplicarAumento(10);

        System.out.println("\nApós aumento de 10%:");

        System.out.println("Salário Anual de " + empregado1.getPrimeiroNome() + " " + empregado1.getSobrenome() + ": " + empregado1.calcularSalarioAnual());
        System.out.println("Salário Anual de " + empregado2.getPrimeiroNome() + " " + empregado2.getSobrenome() + ": " + empregado2.calcularSalarioAnual());

        scanner.close();
    }
}

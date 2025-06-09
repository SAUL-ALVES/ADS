/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;

import java.util.Scanner;

//Questão 21

public class Adicao {

    
    public static void realizarSoma() {
        Scanner scanner = new Scanner(System.in);

        
        System.out.print("Digite o primeiro número: ");
        int numero1 = scanner.nextInt();

        System.out.print("Digite o segundo número: ");
        int numero2 = scanner.nextInt();

        
        int soma = numero1 + numero2;

        
        System.out.println("A soma dos dois números é: " + soma);

        scanner.close();
    }
}


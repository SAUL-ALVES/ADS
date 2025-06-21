/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package escola_2024;

import java.util.Scanner;

public class Escola_2024 {

    public static void main(String[] args) {

       boolean temProximo = true;
       while(temProximo) {

        double nota1, nota2, media;
        Scanner leitor = new Scanner(System.in);
        System.out.println("Informe a nota 1:");
        nota1 = leitor.nextDouble();
        System.out.println("Informe a nota 2:");
        nota2 = leitor.nextDouble();
        media = (nota1 + nota2) / 2;
        System.out.println("A media e: " + media);
        System.out.printf("A media e: %.2f\n", media);

        String situacao = "";
        if (media >= 7) {
            situacao = "Aprovado";
        } else if (media >= 3) {
            situacao = "Final";
        } else {
            situacao = "Reprovado";
        }

        System.out.printf("A sua situacao e: %s\n", situacao);
        
        System.out.println("Deseja calcular outra nota?");
        temProximo = leitor.nextBoolean();
         
    } }
       
}

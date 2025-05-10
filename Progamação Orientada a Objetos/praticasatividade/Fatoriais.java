/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 32
public class Fatoriais {
    public static void main(String[] args) {
        long fatorial = 1;
        
        System.out.println("Número  Fatorial");
        
        for (int i = 1; i <= 20; i++) {
            fatorial *= i;  // Multiplica o fatorial atual pelo próximo número
            System.out.printf("%d       %d\n", i, fatorial);
        }
    }
}


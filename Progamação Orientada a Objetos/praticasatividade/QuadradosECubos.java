/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 27
public class QuadradosECubos {
    public static void main(String[] args) {
        System.out.println("Número\tQuadrado\tCubo");
        
        for (int i = 0; i <= 10; i++) {
            int quadrado = i * i;
            int cubo = i * i * i;
            
            System.out.println(i + "\t" + quadrado + "\t\t" + cubo);
        }
    }
}

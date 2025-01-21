/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 28
import java.util.Scanner;

public class ConsumoCombustivel {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int quilometragemTotal = 0;
        int litrosTotal = 0;
        
        while (true) {
            System.out.print("Digite os quilômetros dirigidos (ou -1 para sair): ");
            int quilometragem = scanner.nextInt();
            
            if (quilometragem == -1) {
                break;
            }
            
            System.out.print("Digite os litros de combustível consumidos: ");
            int litros = scanner.nextInt();
            
            double consumo = (double) quilometragem / litros;
            
            quilometragemTotal += quilometragem;
            litrosTotal += litros;
            
            System.out.printf("Consumo desta viagem: %.2f km/l\n", consumo);
        }
        
        System.out.println("\nTotal de quilômetros dirigidos: " + quilometragemTotal);
        System.out.println("Total de litros de combustível consumidos: " + litrosTotal);
        
        if (litrosTotal > 0) {
            double mediaConsumo = (double) quilometragemTotal / litrosTotal;
            System.out.printf("Consumo médio: %.2f km/l\n", mediaConsumo);
        } else {
            System.out.println("Nenhuma viagem foi registrada.");
        }
        
        scanner.close();
    }
}

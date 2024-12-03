/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package praticasatividade;
//Questão 31
import java.util.Scanner;

public class SalarioBruto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numEmpregados = 3;
        double salarioBruto;
        
        for (int i = 1; i <= numEmpregados; i++) {
            System.out.println("Empregado " + i + ":");
            
            System.out.print("Digite o número de horas trabalhadas na semana: ");
            int horasTrabalhadas = scanner.nextInt();
            
            System.out.print("Digite o salário por hora: ");
            double salarioHora = scanner.nextDouble();
            
            if (horasTrabalhadas > 40) {
                int horasExtras = horasTrabalhadas - 40;
                salarioBruto = (40 * salarioHora) + (horasExtras * salarioHora * 1.5);
            } else {
                salarioBruto = horasTrabalhadas * salarioHora;
            }
            
            System.out.printf("Salário bruto do empregado %d: R$ %.2f\n\n", i, salarioBruto);
        }
        
        scanner.close();
    }
}

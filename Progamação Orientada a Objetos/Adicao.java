package praticasatividade;

import java.util.Scanner;

public class Adicao {
   public Adicao() {
   }

   public static void realizarSoma() {
      Scanner scanner = new Scanner(System.in);
      System.out.print("Digite o primeiro n\u00famero: ");
      int numero1 = scanner.nextInt();
      System.out.print("Digite o segundo n\u00famero: ");
      int numero2 = scanner.nextInt();
      int soma = numero1 + numero2;
      System.out.println("A soma dos dois n\u00fameros \u00e9: " + soma);
      scanner.close();
   }
}

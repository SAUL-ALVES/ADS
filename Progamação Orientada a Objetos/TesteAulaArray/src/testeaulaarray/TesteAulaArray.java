/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package testeaulaarray;

/**
 *
 * @author IFCE
 */
public class TesteAulaArray {

    
    public static void main(String[] args) {
        int [][] tabela = new int [5][7];
        int contador = 10;
        
        for(int i = 0; i < tabela.length; i++ ){
            for(int j = 0; j < tabela[i].length; j++){
                tabela[i][j] = contador;
                contador ++;
            }
        
        }
        
        for(int linha[] : tabela){
            for(int c : linha){
                System.out.print(c + " "); 
            }
          System.out.println();
        }
        
    }
    
}

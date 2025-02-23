/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import java.util.ArrayList;
import javax.swing.JOptionPane;

public class ColecaoArrayList {
    public static void main(String[] args){
        ArrayList<String> cores = new ArrayList<>();
        String opcoes = "1. Adicionar cor.\n2. Remover a cor.\n3. Exibir as cores.\nOutro valor para sair.\n";

        while(true) {
            try {
                String opcao = JOptionPane.showInputDialog(opcoes);
                int op = Integer.parseInt(opcao);
                if(op < 1 || op > 3) {
                    break;
                }
                switch (op) {
                    case 1:   
                        String corAdd = JOptionPane.showInputDialog("Informe uma cor.");
                        cores.add(corAdd);
                        break;
                    case 2:
                        String corRemove = JOptionPane.showInputDialog("Informe uma cor a ser removida.");
                        cores.remove(corRemove);
                        break;
                    case 3:
                        String coresExibicao = "";
                        for(String s : cores) {
                            coresExibicao = coresExibicao.concat(s).concat("\n");
                        }
                        JOptionPane.showMessageDialog(null, coresExibicao);
                        break;                    
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, 
                        "Opção inválida. Digite um número inteiro.", 
                        "Erro", JOptionPane.ERROR_MESSAGE);
            }            
        }
        JOptionPane.showMessageDialog(null, "Tchau!");
    }
    
}
        
       

    
   

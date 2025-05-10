/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package negocio;


public class Funcionario {
    private String nome;
    private Double salario;
    
    public void calcularSalario(double desconto){
        if(salario != null){
            salario = Math.random() * 10000 - desconto;
        }
    }
    
    public void show(){
        
        System.out.println("Eu sou o funcionário" + nome);
    }

    public String getNome() {
        return nome;
    }

    /**
     * @param nome the nome to set
     */
    public void setNome(String nome) {
        this.nome = nome;
    }

    /**
     * @return the salario
     */
    public double getSalario() {
        return salario;
    }

    /**
     * @param salario the salario to set
     */
    public void setSalario(double salario) {
        this.salario = salario;
    }
    
    
}

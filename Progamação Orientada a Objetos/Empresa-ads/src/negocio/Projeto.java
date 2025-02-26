/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package negocio;


public class Projeto {
    private String nome;
    private Integer numero;
    private String local;
    
    
    public void show(){
        System.out.println("Eu sou o projeto" + nome);
    }

    public String getNome() {
        return nome;
    }

    
    public void setNome(String nome) {
        this.nome = nome;
    }

    
    public Integer getNumero() {
        return numero;
    }

    
    public void setNumero(Integer numero) {
        this.numero = numero;
    }

    
    public String getLocal() {
        return local;
    }

    
    public void setLocal(String local) {
        this.local = local;
    }
}

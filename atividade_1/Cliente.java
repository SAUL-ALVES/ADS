package atividade1_pdm;

public class Cliente {

    private String nome;
    private String email;
    private double saldoCarteira;

    public Cliente(String nome, String email, double saldoCarteira) {
        this.nome = nome;
        this.email = email;
        this.saldoCarteira = saldoCarteira;
    }

    public double getSaldoCarteira() {
        return saldoCarteira;
    }

    public void debitar(double valor) {
        if (valor <= saldoCarteira) {
            saldoCarteira -= valor;
        } else {
            throw new RuntimeException("Saldo insuficiente.");
        }
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }
}

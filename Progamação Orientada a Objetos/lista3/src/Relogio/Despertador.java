package Relogio;

public class Despertador {
    private Relogio relogio;
    private Relogio alarme;
    
    public void configurarRelogio(int h, int m, int s) {
        this.relogio = new Relogio(h, m, s);
    }
    
    public void configuraAlarme(int h, int m, int s) {
        this.alarme = new Relogio(h, m, s);
    }
    
    public String executar() {
        String valor = "Silencio";
        this.getRelogio().incrementarSegundo();
        if (this.getRelogio().getHora() == this.getAlarme().getHora() 
            && this.getRelogio().getMinuto() == this.getAlarme().getMinuto()
            && this.getRelogio().getSegundo() == this.getAlarme().getSegundo()) {
            valor = "Bip Bip Bip";
        }
        return valor;   
    }

    public Relogio getRelogio() {
        return relogio;
    }

    public Relogio getAlarme() {
        return alarme;
    }
    
    
}

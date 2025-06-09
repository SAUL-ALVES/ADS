package Relogio;

public class Relogio {
    private int hora;
    private int minuto;
    private int segundo;

    public Relogio() {  
    }
    
    public Relogio(int h) {
        this(h, 0);
    }
    
    public Relogio(int h, int m) {
        this(h, m, 0);
    }
    
    public Relogio(int h, int m, int s) {
        alterarHora(h, m, s);
    }
    
    public void alterarHora(int h, int m, int s) {
        setHora(h);
        setMinuto(m);
        setSegundo(s);
    }
          
    public void incrementarSegundo() {
        this.segundo++;
        if (this.segundo == 60) {
             this.segundo = 0;
             this.minuto++;
             if (this.minuto == 60) {
                 this.minuto = 0;
                 this.hora++;
                 if (this.hora == 24) {
                    this.hora = 0;
                }
            }
        }
    }
    
    public int getHora() {
        return hora;
    }

    public void setHora(int hora) {
        if (hora >= 0 && hora < 24) {
            this.hora = hora;
        }
    }

    public int getMinuto() {
        return minuto;
    }

    public void setMinuto(int minuto) {
        if (minuto >= 0 && minuto < 60) {
            this.minuto = minuto;
        }
    }

    public int getSegundo() {
        return segundo;
    }

    public void setSegundo(int segundo) {
        if (segundo >= 0 && segundo < 60) {
            this.segundo = segundo;
        }
    }

    @Override
    public String toString() {
        return String.format("%02d:%02d:%02d", hora, minuto, segundo);
    }
}

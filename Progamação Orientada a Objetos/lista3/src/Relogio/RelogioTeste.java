package Relogio;

public class RelogioTeste {
    public static void main(String[] args) {
        Relogio r = new Relogio();
        System.out.println(r);
        for (int i = 0; i < 3601; i++) {
            r.incrementarSegundo();
            System.out.println(r);
        }
    }
}

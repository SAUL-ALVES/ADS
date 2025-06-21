package Relogio;

public class DespertadorTeste {
    
    public static void main(String[] args) {
        Despertador desp = new Despertador();
        desp.configurarRelogio(5, 4, 10);
        desp.configuraAlarme(8, 0, 0);
        System.out.println(desp.getRelogio());
        for (int i = 0; i < 30000; i++) {
            String str = desp.executar();
            System.out.println(desp.getRelogio());
            System.out.println(str);
            if (str.startsWith("Bip")) {
                break;
            }
        }
    }
}

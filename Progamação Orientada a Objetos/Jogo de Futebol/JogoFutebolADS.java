package jogofutebolads;

public class JogoFutebolADS {

    public static void main(String[] args) {
        Bola b1 = new Bola();
        b1.coordX = 0;
        b1.coordY = 0;
        b1.cor = "Amarela";
        b1.peso = 340;
        
        Jogador j1 = new Jogador();
        j1.nome = "Schevchenko";
        j1.numero = 23;
        j1.posicao = "Atacante";
        
        j1.chutar(b1, 2);
        
        Jogador j2 = new Jogador();
        j2.nome = "Yashin";
        j2.numero = 12;
        j2.posicao = "Goleiro";
        j2.chutar(b1, 10);
    }
}

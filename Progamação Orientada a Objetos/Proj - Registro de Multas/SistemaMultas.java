import java.util.*;

class Infrator {
    private String nome;
    private String cpf;
    private String endereco;
    private String cnh;
    private List<Multa> multas;

    public Infrator(String nome, String cpf, String endereco, String cnh) {
        this.nome = nome;
        this.cpf = cpf;
        this.endereco = endereco;
        this.cnh = cnh;
        this.multas = new ArrayList<>();
    }

    public void adicionarMulta(Multa multa) {
        multas.add(multa);
    }

    public void consultarInfracoes() {
        System.out.println("Multas do Infrator: " + nome);
        for (Multa multa : multas) {
            multa.consultarInformacoes();
        }
    }
}

class Infracao {
    private String codigo;
    private String descricao;
    private double valor;
    private int pontos;

    public Infracao(String codigo, String descricao, double valor, int pontos) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.valor = valor;
        this.pontos = pontos;
    }

    public void consultarInformacoes() {
        System.out.println("Código: " + codigo + ", Descrição: " + descricao + ", Valor: R$" + valor + ", Pontos: " + pontos);
    }
}

class Multa {
    private String numero;
    private Date data;
    private Infrator infrator;
    private Infracao infracao;
    private Fiscal fiscal;

    public Multa(String numero, Date data, Infrator infrator, Infracao infracao, Fiscal fiscal) {
        this.numero = numero;
        this.data = data;
        this.infrator = infrator;
        this.infracao = infracao;
        this.fiscal = fiscal;
        infrator.adicionarMulta(this);
    }

    public void consultarInformacoes() {
        System.out.println("Número: " + numero + ", Data: " + data + ", Fiscal: " + fiscal.getNome());
        infracao.consultarInformacoes();
    }
}

class Fiscal {
    private String nome;
    private String matricula;
    private String orgao;

    public Fiscal(String nome, String matricula, String orgao) {
        this.nome = nome;
        this.matricula = matricula;
        this.orgao = orgao;
    }

    public String getNome() {
        return nome;
    }

    public Multa emitirMulta(String numero, Date data, Infrator infrator, Infracao infracao) {
        return new Multa(numero, data, infrator, infracao, this);
    }
}

public class SistemaMultas {
    public static void main(String[] args) {
        
        Infrator infrator1 = new Infrator("João Silva", "123.456.789-00", "Rua A, 123", "CNH12345");
        Infracao infracao1 = new Infracao("001", "Excesso de Velocidade", 150.0, 5);
        Fiscal fiscal1 = new Fiscal("Carlos Mendes", "F001", "DETRAN");

        
        Multa multa1 = fiscal1.emitirMulta("M001", new Date(), infrator1, infracao1);

        
        infrator1.consultarInfracoes();
    }
    
}



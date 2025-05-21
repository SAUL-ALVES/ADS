class Estado:

    def __init__(self, id: int, nome: str, sigla: str, populacao: int, capital: str):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.populacao = populacao
        self.capital = capital

    def __str__(self):
        return f"Estado(id={self.id}, nome='{self.nome}', sigla='{self.sigla}', populacao={self.populacao}, capital='{self.capital}')"

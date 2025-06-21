# models.py
class Cliente:
    def __init__(
        self,
        id=0,
        idade=0,
        sexo="",
        credito=0,
        moradia="",
        conta_poupanca="",
        conta_corrente="",
        duracao=0,
        proposito="",
        aprovacao=0,
    ):
        self.id = id
        self.idade = idade
        self.sexo = sexo
        self.credito = credito
        self.moradia = moradia
        self.conta_poupanca = conta_poupanca
        self.conta_corrente = conta_corrente
        self.duracao = duracao
        self.proposito = proposito
        self.aprovacao = aprovacao

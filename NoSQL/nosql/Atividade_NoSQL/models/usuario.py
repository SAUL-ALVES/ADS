class Usuario:

    def __init__(self, id: int = None, nome: str = ""):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}')"

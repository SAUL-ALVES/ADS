from db import get_connection
from models.estado import Estado


class DAOEstado:

    def __init__(self):
        self.conn = get_connection()

        self.estados_info = {
            "AC": "Rio Branco",
            "AL": "Maceió",
            "AP": "Macapá",
            "AM": "Manaus",
            "BA": "Salvador",
            "CE": "Fortaleza",
            "DF": "Brasília",
            "ES": "Vitória",
            "GO": "Goiânia",
            "MA": "São Luís",
            "MT": "Cuiabá",
            "MS": "Campo Grande",
            "MG": "Belo Horizonte",
            "PA": "Belém",
            "PB": "João Pessoa",
            "PR": "Curitiba",
            "PE": "Recife",
            "PI": "Teresina",
            "RJ": "Rio de Janeiro",
            "RN": "Natal",
            "RS": "Porto Alegre",
            "RO": "Porto Velho",
            "RR": "Boa Vista",
            "SC": "Florianópolis",
            "SP": "São Paulo",
            "SE": "Aracaju",
            "TO": "Palmas",
        }

    def buscar_por_sigla(self, sigla: str) -> Estado | None:
        sigla = sigla.upper()
        nome_estado = self.estados_info.get(sigla)

        if not nome_estado:
            return None

        cursor = self.conn.cursor()
        cursor.execute("SELECT population FROM city WHERE name = ?", (nome_estado,))
        row = cursor.fetchone()

        populacao = row[0] if row else 0

        return Estado(
            id=None,
            nome=nome_estado,
            sigla=sigla,
            populacao=populacao,
            capital=nome_estado,
        )

    def buscar_todos(self) -> list[Estado]:
        return [self.buscar_por_sigla(sigla) for sigla in self.estados_info]

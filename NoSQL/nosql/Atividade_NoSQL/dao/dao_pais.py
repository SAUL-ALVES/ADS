from db import get_connection
from models.country import Country


class DAOPais:

    def __init__(self):
        self.conn = get_connection()

    def buscar_por_codigo(self, code: str) -> Country | None:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT code, name, population FROM country WHERE code = ?", (code,)
        )
        row = cursor.fetchone()

        if row:
            return Country(code=row[0], name=row[1], population=row[2])

        return None

    def listar_todos(self) -> list[Country]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT code, name, population FROM country")
        return [
            Country(code=row[0], name=row[1], population=row[2])
            for row in cursor.fetchall()
        ]

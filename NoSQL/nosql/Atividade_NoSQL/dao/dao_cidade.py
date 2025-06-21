from db import get_connection
from models.city import City


class DAOCidade:

    def __init__(self):
        self.conn = get_connection()

    def buscar_por_id(self, id: int) -> City | None:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, name, countrycode, population FROM city WHERE id = ?", (id,)
        )
        row = cursor.fetchone()

        if row:
            return City(id=row[0], name=row[1], country_code=row[2], population=row[3])

        return None

    def listar_todos(self) -> list[City]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, countrycode, population FROM city")
        return [
            City(id=row[0], name=row[1], country_code=row[2], population=row[3])
            for row in cursor.fetchall()
        ]

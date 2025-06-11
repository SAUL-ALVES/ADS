from db import get_connection
from models.usuario import Usuario


class DAOUsuario:

    def __init__(self):
        self.conn = get_connection()
        self._criar_tabela()

    def _criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    def salvar(self, usuario: Usuario):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (usuario.nome,))
        self.conn.commit()
        usuario.id = cursor.lastrowid

    def remover(self, id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def buscar_por_id(self, id: int) -> Usuario | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome FROM usuarios WHERE id = ?", (id,))
        row = cursor.fetchone()
        return Usuario(id=row[0], nome=row[1]) if row else None

    def listar_todos(self) -> list[Usuario]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome FROM usuarios")
        return [Usuario(id=row[0], nome=row[1]) for row in cursor.fetchall()]

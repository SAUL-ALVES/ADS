
from server.server import Server
from routes import usuarios

app = Server()

app.route("/")(usuarios.index)
app.route("/usuarios")(usuarios.listar_usuarios)
app.route("/usuarios/novo")(usuarios.novo_usuario)
app.route("/usuarios", methods=["POST"])(usuarios.criar_usuario)
app.route("/usuarios/<id>")(usuarios.detalhar_usuario)
app.route("/usuarios/<id>/editar")(usuarios.editar_usuario)
app.route("/usuarios/<id>/atualizar", methods=["POST"])(usuarios.atualizar_usuario)
app.route("/usuarios/<id>/excluir", methods=["POST"])(usuarios.excluir_usuario)

if __name__ == "__main__":
    app.start()

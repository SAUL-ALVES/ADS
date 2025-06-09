
import os
from urllib.parse import parse_qs
from server.plumbing import html_response

CAMINHO_ARQUIVO = "usuarios.txt"


def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    usuarios = []
    for linha in linhas:
        if linha.strip():
            partes = linha.strip().split("|")
            usuarios.append(
                {
                    "id": int(partes[0]),
                    "nome": partes[1],
                    "email": partes[2],
                    "telefone": partes[3],
                }
            )
    return usuarios


def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        for u in usuarios:
            linha = f"{u['id']}|{u['nome']}|{u['email']}|{u['telefone']}\n"
            f.write(linha)


def listar_usuarios(request, response):
    usuarios = carregar_usuarios()
    html = """
    <html>
        <head><title>Usuários</title></head>
        <body>
            <h1>Usuários</h1>
            <ul>
    """

    for u in usuarios:
        html += f"<li>{u['nome']} - <a href='/usuarios/{u['id']}'>Detalhes</a></li>"

    html += """
            </ul>
            <a href="/usuarios/novo">Novo Usuário</a>
        </body>
    </html>
    """

    response.update(
        {
            "status": 200,
            "headers": {"Content-Type": "text/html; charset=utf-8"},
            "body": html,
        }
    )


def novo_usuario(request, response):
    html = """
    <h1>Novo Usuário</h1>
    <form method='POST' action='/usuarios'>
        Nome: <input name='nome'><br>
        Email: <input name='email'><br>
        Telefone: <input name='telefone'><br>
        <button type='submit'>Salvar</button>
    </form>
    """
    response["body"] = html


def criar_usuario(request, response):
    dados = parse_qs(request["body"])
    usuarios = carregar_usuarios()
    novo_id = max([u["id"] for u in usuarios], default=0) + 1
    novo_usuario = {
        "id": novo_id,
        "nome": dados["nome"][0],
        "email": dados["email"][0],
        "telefone": dados["telefone"][0],
    }
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    response["status"] = 302
    response["headers"] = {"Location": "/usuarios"}


def detalhar_usuario(request, response):
    id = int(request["path"].split("/")[-1])
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        response["body"] = "Usuário não encontrado"
        return
    html = f"""
    <h1>{usuario['nome']}</h1>
    <p>Email: {usuario['email']}</p>
    <p>Telefone: {usuario['telefone']}</p>
    <a href='/usuarios/{id}/editar'>Editar</a>
    <form method='POST' action='/usuarios/{id}/excluir' style='margin-top:10px;'>
        <button type='submit'>Excluir</button>
    </form>
    """
    response["body"] = html


def editar_usuario(request, response):
    id = int(request["path"].split("/")[2])
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        response["body"] = "Usuário não encontrado"
        return
    html = f"""
    <h1>Editar Usuário</h1>
    <form method='POST' action='/usuarios/{id}/atualizar'>
        Nome: <input name='nome' value='{usuario['nome']}'><br>
        Email: <input name='email' value='{usuario['email']}'><br>
        Telefone: <input name='telefone' value='{usuario['telefone']}'><br>
        <button type='submit'>Atualizar</button>
    </form>
    """
    response["body"] = html


def atualizar_usuario(request, response):
    id = int(request["path"].split("/")[2])
    dados = parse_qs(request["body"])
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["id"] == id:
            u["nome"] = dados["nome"][0]
            u["email"] = dados["email"][0]
            u["telefone"] = dados["telefone"][0]
            break
    salvar_usuarios(usuarios)
    response["status"] = 302
    response["headers"] = {"Location": f"/usuarios/{id}"}


def excluir_usuario(request, response):
    id = int(request["path"].split("/")[2])
    usuarios = carregar_usuarios()
    usuarios = [u for u in usuarios if u["id"] != id]
    salvar_usuarios(usuarios)
    response["status"] = 302
    response["headers"] = {"Location": "/usuarios"}


def index(request, response):
    response["status"] = 302
    response["headers"] = {"Location": "/usuarios"}

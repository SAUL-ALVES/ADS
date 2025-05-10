from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "teste"  # Necessário para usar sessões


# Exercício 1: Verificação de Acesso por Idade
@app.route("/idade", methods=["GET", "POST"])
def verificar_idade():
    mensagem = None
    if request.method == "POST":
        idade = int(request.form["idade"])
        if idade >= 18:
            mensagem = "Acesso permitido"
        else:
            mensagem = "Acesso negado"
    return render_template("idade.html", mensagem=mensagem)


# Exercício 2: Classificação de Notas
@app.route("/nota", methods=["GET", "POST"])
def classificar_nota():
    classificacao = None
    if request.method == "POST":
        nota = float(request.form["nota"])
        if nota >= 9:
            classificacao = "Excelente"
        elif nota >= 6:
            classificacao = "Aprovado"
        else:
            classificacao = "Reprovado"
    return render_template("nota.html", classificacao=classificacao)


# Exercício 1 (Repetição): Bem-vindo com lista de nomes
@app.route("/boas-vindas")
def boas_vindas():
    nomes = ["Ana", "Carlos", "Maria", "João", "Sofia"]
    return render_template("boas_vindas.html", nomes=nomes)


# Exercício 2 (Repetição): Sistema de Tentativa de Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if "tentativas" not in session:
        session["tentativas"] = 0

    bloqueado = False
    mensagem = None

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "1234":
            session["tentativas"] = 0
            mensagem = "Login realizado com sucesso!"
        else:
            session["tentativas"] += 1
            if session["tentativas"] >= 3:
                bloqueado = True

    return render_template(
        "login.html",
        tentativas=session.get("tentativas", 0),
        bloqueado=bloqueado,
        mensagem=mensagem,
    )


# Exercício 3 (Repetição): Números com continue e break
@app.route("/numeros", methods=["GET", "POST"])
def controle_numeros():
    mensagem = None
    if request.method == "POST":
        numero = int(request.form["numero"])
        if numero == -1:
            mensagem = "Programa encerrado pelo usuário."
        elif numero == 3:
            mensagem = "Número 3 ignorado."
        else:
            mensagem = f"Número processado: {numero}"
    return render_template("numeros.html", mensagem=mensagem)


# Desafio 1: Sistema de Mensagens Inteligentes
@app.route("/mensagens", methods=["GET", "POST"])
def sistema_mensagens():
    resposta = None
    if request.method == "POST":
        tipo = request.form["mensagem"].lower()
        if tipo == "ok":
            resposta = "Operação realizada com sucesso"
        elif tipo == "erro":
            resposta = "Erro genérico"
        else:
            resposta = "Tipo não reconhecido"
    return render_template("mensagens.html", resposta=resposta)


# Desafio 2: Simulador de Verificação de Acesso
@app.route("/acesso", methods=["GET", "POST"])
def verificacao_acesso():
    mensagem = None
    sucesso = False
    if request.method == "POST":
        login = request.form["login"].strip()
        senha = request.form["senha"].strip()

        if not login or not senha:
            mensagem = "Preencha todos os campos"
        elif login == "admin" and senha == "1234":
            mensagem = "Login realizado com sucesso"
            sucesso = True
        else:
            mensagem = "Dados inválidos"

    return render_template("acesso.html", mensagem=mensagem, sucesso=sucesso)


# Rota principal para navegação
@app.route("/")
def index():
    return """
    <h1>Menu de Exercícios</h1>
    <ul>
        <li><a href="/idade">1. Verificação de Idade</a></li>
        <li><a href="/nota">2. Classificação de Notas</a></li>
        <li><a href="/boas-vindas">3. Lista de Boas-vindas</a></li>
        <li><a href="/login">4. Sistema de Login</a></li>
        <li><a href="/numeros">5. Controle de Números</a></li>
        <li><a href="/mensagens">Desafio 1: Sistema de Mensagens</a></li>
        <li><a href="/acesso">Desafio 2: Verificação de Acesso</a></li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)

from dao.dao_usuario import DAOUsuario
from models.usuario import Usuario
from dao.dao_estado import DAOEstado
from dao.dao_cidade import DAOCidade
from dao.dao_pais import DAOPais

param = 4


def test_DAOUser():

    # Esse funciona, mas não executa com ele toda hora, foi só mais pra debugg
    '''# Teste DAOUsuario
    print("== Teste DAOUsuario ==")

    dao_usuario = DAOUsuario()
    novo_usuario = Usuario(nome="Luppps")
    dao_usuario.salvar(novo_usuario)

    # So pra debugg
    """removido = dao_usuario.remover(param) #

    if removido:
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado para remoção.")"""

    for usuario in dao_usuario.listar_todos():
        print(" -", usuario)'''


def test_DAOCity():

    # Teste DAOCidade
    print("\n== Teste DAOCidade ==")

    dao_cidade = DAOCidade()
    cities = dao_cidade.listar_todos()[89:100]

    for city in cities:
        print(" -", city)


def test_DAOState():

    # Teste DAOEstado
    print("\n== Teste DAOEstado ==")

    dao_estado = DAOEstado()
    estado = dao_estado.buscar_por_sigla("CE")

    if estado:
        print("Estado encontrado:", estado)
    else:
        print("Estado não encontrado.")


def test_DAOCountry():

    # Teste DAOPais
    print("\n== Teste DAOPais ==")
    dao_country = DAOPais()
    country = dao_country.buscar_por_codigo("BR")

    if country:
        print("País encontrado:", country)
    else:
        print("País não encontrado.")


def main():

    test_DAOUser()
    test_DAOCity()
    test_DAOState()
    test_DAOCountry()


main()

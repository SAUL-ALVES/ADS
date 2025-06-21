
def test_array_list():
# Teste de inicialização
    vec = LinkedList[int]()
    assert vec.is_empty(), "Erro: O vetor deveria estar vazio após a inicialização."

    # vec_with_values = LinkedList[int](5, 10)
    # assert len(vec_with_values) == 5, "Erro: O vetor deveria ter 5 elementos."
    # assert all(x == 10 for x in vec_with_values), "Erro: Todos os elementos deveriam ser iguais a 10."

    # Teste do método add
    vec.add(5)
    assert len(vec) == 1, "Erro: O método add não incrementou o tamanho corretamente."
    assert vec.get_at(0) == 5, "Erro: O valor adicionado não é igual ao esperado."

    # Teste do método clear
    vec.clear()
    assert vec.is_empty(), "Erro: O vetor deveria estar vazio após clear()."

    # Teste de comparação com equals
    vec.add(1)
    vec.add(2)
    vec2 = LinkedList[int]()
    vec2.add(1)
    vec2.add(2)
    assert vec.equals(vec2), "Erro: Vetores iguais não foram reconhecidos como iguais."

    # Teste do método first
    assert vec.first() == 1, "Erro: O método first deveria retornar o primeiro elemento."

    # Teste do método last
    assert vec.last() == 2, "Erro: O método last deveria retornar o último elemento."

    # Teste de manipulação de índices
    vec.insert_at(1, 3)

    assert vec.get_at(1) == 3, "Erro: O valor no índice 1 deveria ser 3."
    vec.set_at(1, 4)
    assert vec.get_at(1) == 4, "Erro: O valor no índice 1 deveria ser 4 após a substituição."
    vec.remove_at(1)
    assert len(vec) == 2, "Erro: O tamanho deveria ser 2 após a remoção."

    # Teste de reversão
    vec.reverse()
    assert vec.get_at(0) == 2 and vec.get_at(1) == 1, "Erro: O vetor não foi revertido corretamente."

    # Teste de sublist
    vec.add(3)
    vec.add(4)
    sub = vec.sublist(1, 3)
    assert len(sub) == 2 and sub.get_at(0) == 1 and sub.get_at(1) == 3, "Erro: O método sublist não retornou os elementos corretos."

    # Teste de ordenação
    vec.sort()
    assert vec.get_at(0) == 1 and vec.get_at(-1) == 4, "Erro: O método sort não ordenou corretamente."

    # Teste de embaralhamento
    vec.shuffle()
    assert set(vec) == {1, 2, 3, 4}, "Erro: O método shuffle alterou os elementos do vetor."

    # Teste do método map
    vec.map(lambda x: x * 2)
    assert vec.get_at(0) == 2, "Erro: O método map não aplicou a transformação corretamente."

    # Teste do método to_str
    assert str(vec) == "[2, 4, 6, 8]", "Erro: O método to_str não retornou a string esperada."

    print("Todos os testes passaram com sucesso!")

# Executar os testes
test_array_list()
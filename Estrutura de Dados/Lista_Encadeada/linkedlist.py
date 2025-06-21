from typing import Generic, TypeVar, Self

T = TypeVar('T')

class ListNode(Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self._next = None

class LinkedList(Generic[T]):

    def __init__(self, n: int=0, value: T=None) -> Self:
        """
        Inicializa uma nova Lista.
        O construtor padrão cria um vetor vazio.
        A segunda forma cria um array com ```n``` elementos, cada um dos quais é inicializado para ```value```;
        Se ```value``` estiver faltando, os elementos são inicializados com None.

        Args:
            n (int): a quantidade de posições pré-alocadas.
            value (T): o valor padrão a ser preenchido.

        Returns:
            Uma nova lista de tuplas.
        """
        super().__init__()

        self._size = n
        self._head: ListNode = value
        self._tail: ListNode = value

        if n > 0:
          for qtt in range(n):
            self.add(value)

    def index_out_of_bounds(self, index: int) -> bool:
       if index < 0 or index >= self._size: # Verifica se o índice esta dentro do intervalo
          return True
       return False

    def add(self, value: T) -> None:
        node = ListNode(value)

        if self.is_empty(): # Se a lista estiver vazia, adiciona o no como Head e Tail
            self._head = node
            self._tail = node
        else: # Se não estiver vazia, atualizamos o ponteiro do antigo último nó e o novo nó passa a ser Tail
            self._tail._next = node
            self._tail = node
        
        self._size += 1


    def clear(self) -> None:
        self._head = None 
        self._tail = None
        self._size = 0

    def equals(self, other: T) -> bool:
        """
        Retorna ```True``` se os dois vetores contêm exatamente os mesmos valores de elementos na mesma ordem.

        Uso:
            if (vec1.equals(vec2)):
        """

        if self.size() != other.size(): # Verifica se os tamanhos são diferentes
          return False

        else: # Variável auxilar para percorrer as duas listas
          node1 = self._head 
          node2 = other._head

          # Verifica elemento por elemento
          while node1 and node2:
            if node1._value != node2._value:  # Se forem diferentes, intercepta
              return False

            # Apontam para a próxima referência
            node1 = node1._next
            node2 = node2._next

        return True # Se chegar aqui, são iguais

    def first(self) -> T:
        if self.is_empty():
          raise IndexError('Lista vazia')

        return self._head._value


    def get_at(self, index: int) -> T:
        if self.index_out_of_bounds(index):
          raise IndexError()

        node = self._head # Iniciando a busca pelo Head
       
        for i in range(index):  
          if node is None:  
            raise IndexError("Índice fora dos limites!")
          node = node._next  # Vai para o próximo nó

        return node._value

    def insert_at(self, index: int, value: T) -> None:
        """
        Insere um novo valor neste vetor no índice especificado.
        Todos os elementos subsequentes são deslocados uma posição para a direita.
        Este método sinaliza um erro (```IndexError```) se o índice estiver fora do intervalo de 0 até e incluindo o comprimento deste ArrayList.

        Uso:
            vec.insert_at(0, valor)
        """

        if self.index_out_of_bounds(index):
          raise IndexError("Índice fora dos limites da lista!")

        new_node = ListNode(value) # Cria o nó com o valor

        if index == 0: # Verifica se a inserção é no head
          new_node._next = self._head # Novo nó agora aponta para o antigo First_Node
          self._head = new_node # Novo nó passa a ser o First_Node (Head)

          if self._size == 0: # Verifica se a lista possui apenas um único elemento
            self._tail = new_node # Caso sim, Head e Tail são a mesma coisa

        else: # Caso a inserção seja no meio da lista
          previous = self._head # Variavel auxiliar que aponta para o primeiro nó  

          for no in range(index - 1): # Percorremos a lista até a posição anterior a que queremos inserir
            previous = previous._next # O nó atual da iteração aponta para o próximo, até chegarmos aonde queremos

          new_node._next = previous._next # O novo nó agora aponta para o seu nó a frente
          previous._next = new_node # o nó anterior aponta para o novo nó
          
        self._size += 1 # Aumenta o tamanho da lista após a inserção do novo elemento

    def is_empty(self) -> bool:
        return self.size() == 0

    def last(self) -> T:
        if self.is_empty():
            raise IndexError()

        return self._tail._value

    def map(self, fn: callable) -> None:
        node = self._head

        while node:
            node._value = fn(node._value)
            node = node._next

    def remove_at(self, index: int) -> None:
        """
        Remove o elemento no índice especificado deste ArrayList.
        Todos os elementos subsequentes são deslocados uma posição para a esquerda.
        Este método sinaliza um erro (```IndexError```) se o índice estiver fora do intervalo do ArrayList.

        Uso:
            vec.remove_at(0, valor)
        """
        if self.index_out_of_bounds(index):
          raise IndexError()
        
        if index == 0:
          self._head = self._head._next # Ao apontar para o próximo, Head atual deixa de existir

          if self._head is None: # Será True apenas quando a lista tiver apenas um único elemento, pois head agora seria None, resultando numa lista vazia
            self._tail = None

        else: 
          previous = self._head 

          for no in range(index - 1):
            previous = previous._next
          
          previous._next = previous._next._next

          if previous._next is None:
            previous._tail = previous
          
        self._size -= 1


    def reverse(self) -> None:
        aux = LinkedList() # List auxiliar para reverter o objeto
        node = self._head # Nó para iniciar iteração

        while node: 
            aux.add(node._value) # Adicionando nós na lista auxiliar  
            node = node._next # Apontando para a próxima referência

        self.clear() # Limpando a lista original para começar a preenchê-la com a revertida

        for i in range(aux.size() - 1, -1, -1): # Percorrendo a lista auxiliar de trás para frente
            self.add(aux.get_at(i)) # Adicionando o nó no objeto

    def set_at(self, index: int, value: T) -> None: 
        if self.index_out_of_bounds(index):
          raise IndexError()

        node = self._head # Iniciando a busca pelo Head
       
        for i in range(index): # Percorre até o índice desejado  
          if node is None:  
            raise IndexError("Índice fora dos limites!")
          node = node._next  # Vai para o próximo nó
        node._value = value 

    def shuffle(self) -> None:
        """
        Reorganize os elementos neste ArrayList em ordem aleatória.

        Uso:
            vec.shuffle()
        """
        raise NotImplementedError()

    def size(self) -> int:
        return self._size

    def sort(self) -> None:
        """
        Reorganiza os elementos neste vetor em ordem crescente.
        Os elementos são comparados usando o operador ```<```.
        Em ordem crescente, o elemento mínimo é colocado no índice ```0```; o máximo está no índice ```size()-1```.

        Uso:
            vec.sort()
        """

        
        raise NotImplementedError()

    def sublist(self, start: int, end: int=-1) -> Self:
        """
        Retorna um novo vetor contendo elementos de um subintervalo deste vetor.
        Se apenas um argumento for fornecido, o comprimento do subintervalo será até o fim deste vetor.
        Por exemplo, a chamada de ```sublist(2, 4)``` retornaria um novo vetor contendo os elementos 2-5 do vetor original em seus índices 0-3.
        Gera um erro se o intervalo ```[start, end)``` não estiver contido no intervalo ```[0, size()]```.

        Uso:
            sub1 = vec.sublist(3)
            sub2= vec.sublist(1, 4)
        """

        if start < 0 or end >= self._size():
          raise IndexError("Index Out Of Bounds!")

        node = self._head 
        sublist = LinkedList()

        while node: 
          if node._value == start:
            while node:
              sublist.add(node._value)
              node = node._next   
           
        return sublist

    def to_str(self) -> str:
        """
        Retorna uma representação de string imprimível deste ArrayList, como "[value1, value2, value3]".
        """ 

        if self.is_empty():
          return "[]"

        # Inicializa uma lista para armazenar os valores dos nós
        values = []
        node = self._head  # Começa a iteração no Head

        while node:
            values.append(str(node._value))  # Adiciona o valor do nó à lista
            node = node._next  # Aponta para o próximo nó

        return f"[{', '.join(values)}]"

    ## truques do Python

    def __bool__(self) -> bool:
        return not self.is_empty()


    def __eq__(self, other: Self) -> bool:
        return self.equals(other)


    def __str__(self) -> str:
        return self.to_str()


    def __len__(self) -> int:
        return self.size()


    def __get_item__(self, index: int) -> T:
        return self.get_at(index)


    def __set_item__(self, index, value) -> None:
        return self.set_at(index, value)


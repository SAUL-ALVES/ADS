class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adiciona um elemento ao final da fila"""
        self.items.append(item)  # Adiciona no final da lista

    def dequeue(self):
        """Remove e retorna o primeiro elemento da fila"""
        if not self.is_empty():
            return self.items.pop(0)  # Remove do início da lista
        return "A fila está vazia"

    def front(self):
        """Retorna o primeiro elemento da fila sem remover"""
        if not self.is_empty():
            return self.items[0]  # Primeiro elemento
        return "A fila está vazia"

    def is_empty(self):
        """Verifica se a fila está vazia"""
        return len(self.items) == 0

    def size(self):
        """Retorna o tamanho da fila"""
        return len(self.items)

    def __repr__(self):
        return str(self.items)


# Testando a Fila
f = Queue()
f.enqueue(10)
f.enqueue(20)
f.enqueue(30)

print(f.front())  # Saída: 10
f.dequeue()  # Remove 10
print(f)  # Saída esperada: [20, 30]

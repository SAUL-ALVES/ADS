class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Adiciona um elemento ao topo da pilha"""
        self.items.append(item)  # Adiciona no final da lista

    def pop(self):
        """Remove e retorna o elemento do topo da pilha"""
        if not self.is_empty():
            return self.items.pop()  # Remove do final da lista
        return "A pilha está vazia"

    def top(self):
        """Retorna o elemento do topo sem remover"""
        if not self.is_empty():
            return self.items[-1]  # Último elemento
        return "A pilha está vazia"

    def is_empty(self):
        """Verifica se a pilha está vazia"""
        return len(self.items) == 0

    def size(self):
        """Retorna o tamanho da pilha"""
        return len(self.items)

    def __repr__(self):
        return str(self.items)

# Testando a Pilha
p = Stack()
p.push(10)
p.push(20)
p.push(30)

print(p.top())  # Saída: 30
p.pop()         # Remove 30
print(p)        # Saída esperada: [10, 20]

class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return not bool(self.itens)

    def empilhar(self, dado):
        self.itens.append(dado)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        
    def __str__(self):
        return str(self.itens)

pilha = Pilha()
pilha.empilhar('A')
print(pilha)
pilha.empilhar('B')
print(pilha)
pilha.empilhar('C')
print(pilha)

print(pilha.desempilhar())  
print(pilha)
print(pilha.desempilhar())  
print(pilha)
print(pilha.desempilhar())  
print(pilha)

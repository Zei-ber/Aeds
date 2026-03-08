class Node:
    def __init__(self, valor=None, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior
class ListaDL:
    def __init__(self):
        self.head = None

    def inserir_no_inicio(self, valor):
        novo = Node(valor)
        if self.head is None:
            self.head = novo
        else:
            novo.proximo = self.head
            self.head.anterior = novo
            self.head = novo

    def inserir_no_fim(self, valor):
        novo = Node(valor)
        if self.head is None:
            self.head = novo
            return

        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo
        novo.anterior = atual
    def remover(self, valor):
        if self.head is None:
            return False
        atual = self.head
        while atual is not None and atual.valor != valor:
            atual = atual.proximo

        if atual is None:
            return False
        if atual.anterior is None:
            self.head = atual.proximo
            if self.head is not None:
                self.head.anterior = None
        else:
            atual.anterior.proximo = atual.proximo
            if atual.proximo is not None:
                atual.proximo.anterior = atual.anterior
        return True
    def buscar(self, valor):
        atual = self.head
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False
    def exibir(self):
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(" -> ".join(elementos) if elementos else "Lista vazia")
    def tamanho(self):
        cont = 0
        atual = self.head
        while atual is not None:
            cont += 1
            atual = atual.proximo
        return cont
    def inverter(self):
        atual = self.head
        ultimo = None
        while atual is not None:
            proximo_original = atual.proximo
            atual.proximo, atual.anterior = atual.anterior, atual.proximo
            ultimo = atual
            atual = proximo_original

        if ultimo is not None:
            self.head = ultimo

lista = ListaDL()

lista.inserir_no_inicio(10)
lista.inserir_no_inicio(5)
lista.inserir_no_fim(20)

lista.exibir()

lista.remover(10)
lista.exibir()

print(lista.buscar(20))
print(lista.buscar(15))

print("Tamanho:", lista.tamanho())

lista.inverter()
lista.exibir()
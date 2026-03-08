# Classe que representa um nó da lista
class Node:
    def __init__(self, valor):
        self.valor = valor              # Dado armazenado no nó
        self.proximo = None             # Ponteiro para o próximo nó (ou None)


# Classe que representa a lista ligada
class ListaLigada:
    def __init__(self):
        self.head = None                # Referência para o primeiro nó (lista vazia no início)

    # Inserir um novo nó no início da lista
    def inserir_no_inicio(self, valor):
        novo_no = Node(valor)           # Cria o novo nó
        novo_no.proximo = self.head     # Faz o novo nó apontar para o antigo primeiro
        self.head = novo_no             # Atualiza o início da lista

    # Inserir um novo nó no final da lista
    def inserir_no_fim(self, valor):
        novo_no = Node(valor)
        if self.head is None:           # Se a lista estiver vazia
            self.head = novo_no
            return
        atual = self.head
        while atual.proximo:            # Percorre até o último nó
            atual = atual.proximo
        atual.proximo = novo_no         # Liga o último nó ao novo nó

    # Remover o primeiro nó que contenha o valor informado
    def remover(self, valor):
        atual = self.head
        anterior = None

        # Procura o valor na lista
        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if atual is None:               # Valor não encontrado
            print(f"Valor {valor} não encontrado.")
            return

        if anterior is None:            # Caso o valor esteja no primeiro nó
            self.head = atual.proximo
        else:
            anterior.proximo = atual.proximo  # Pula o nó removido
        print(f"Valor {valor} removido com sucesso.")

    # Verifica se um valor está na lista
    def buscar(self, valor):
        atual = self.head
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    # Exibe todos os elementos da lista
    def exibir(self):
        if self.head is None:
            print("Lista vazia.")
            return

        atual = self.head
        elementos = []
        while atual:
            elementos.append(str(atual.valor))  # Armazena o valor como texto
            atual = atual.proximo
        print(" → ".join(elementos))            # Mostra os valores separados por setas

    # Retorna o número de elementos da lista
    def tamanho(self):
        contador = 0
        atual = self.head
        while atual:
            contador += 1
            atual = atual.proximo
        return contador

    # Inverte a ordem dos nós da lista
    def inverter(self):
        anterior = None
        atual = self.head

        # Percorre invertendo os ponteiros
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo

        self.head = anterior            # Novo início da lista


# Testes de funcionamento
if __name__ == "__main__":
    lista = ListaLigada()

    lista.inserir_no_inicio(10)
    lista.inserir_no_inicio(5)
    lista.inserir_no_fim(20)
    lista.exibir()  # Saída esperada: 5 → 10 → 20

    lista.remover(10)
    lista.exibir()  # Saída esperada: 5 → 20

    print(lista.buscar(20))  # True
    print(lista.buscar(15))  # False

    print("Tamanho da lista:", lista.tamanho())  # 2
    lista.inverter()
    lista.exibir()  # Saída esperada: 20 → 5
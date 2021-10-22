class Cliente():
    def __init__(self, nome):
        self.nome = nome


class Produto():
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho():
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos

    def adicionar_produtos(self, produtos):
        self.produtos.append(produtos)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"{produto.descricao} | {produto.valor}")
    
    def calcular_total(self):
        total = [produto.valor for produto in self.produtos]
        print(f"Total = {sum(total)}")


produto_1 = Produto("Pen Drive", 30)
produto_2 = Produto("HD Externo", 100)

cliente_1 = Cliente("Pedro")

carrinho_1 = Carrinho(cliente_1, [])

carrinho_1.adicionar_produtos(produto_1)
carrinho_1.adicionar_produtos(produto_2)

carrinho_1.listar_produtos()

carrinho_1.calcular_total()


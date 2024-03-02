# Crie uma classe chamada Fatura , a classe Fatura deve incluir os seguintes atributos o nome do item; o preço unitário do item;
# quantidade de item a ser faturado; valor total da fatura; Sua classe deve ter um construtor que inicialize todos os atributos
# menos o valor total da fatura. Forneça um método chamado gerar_fatura que calcula o valor da fatura (isto é, multiplicar a
# quantidade pelo preço por item).

class Fatura: 
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0
    
    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade

    def __str__(self):
        return f'Item: {self.nome_item}, Preço unitário: R${self.preco_unitario}, Quantidade: {self.quantidade}, Valor total: R${self.valor_total}'

# Uso da class Fatura
fatura1 = Fatura('Cerveja', 4.99, 24)
fatura1.gerar_fatura()
print(fatura1)

fatura2 = Fatura('Fraldinha', 34.00, 2)
fatura2.gerar_fatura()
print(fatura2)

fatura3 = Fatura('Carvão', 12.00, 1)
fatura3.gerar_fatura()
print(fatura3)
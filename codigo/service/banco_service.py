from codigo.model.conta import Conta
class BancoSerice:

    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []


    def adicionar_conta(self, conta: Conta):
        self.__contas.append(conta)


    def pesquisar_conta_cliente(self, cpf):
        conta: Conta
        for id, c in enumerate(self.__contas):
            if c.cpf == cpf:
                conta = self.__contas[id]
        return conta

    def listar_contas_alta_renda(self):
        filtered = filter(lambda conta: conta.saldo >= 10000, self.__contas )
        return list(filtered)

    def filtrar_contas(self, filtro: Conta):
        filter(lambda conta: filtro in conta, self.__contas)


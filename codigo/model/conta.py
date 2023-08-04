class Banco:

    def __init__(self, cpf):
        self.__cpf = cpf
        self.__saldo = None

    @property
    def saldo(self):
        return self.__saldo

    @property
    def cpf(self):
        return self.__cpf

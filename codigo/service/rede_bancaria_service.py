from codigo.gateway.banco_central_gateway import BancoCentralGateway
class RedeBancariaService:

    def __init__(self, banco_central_gateway:BancoCentralGateway):
        self.__banco_central_gateway = banco_central_gateway

    def registrar_banco(self, banco):
        return self.__banco_central_gateway.cadastrar_banco(banco)
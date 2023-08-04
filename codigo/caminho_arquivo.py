class CaminhoArquivo:

    def __init__(self,diretorio,arquivo):
        self.__diretorio = diretorio
        self.__arquivo = arquivo

    @property
    def diretorio(self):
        return self.__diretorio

    @property
    def arquivo(self):
        return self.__arquivo

    @staticmethod
    def instance(id):
        b = '/tmp/'
        d = None
        if id <= 1000:
            d = b + str(id)
        else:
            i = id
            f = True
            while f:
                if id <= (i * 1000):
                    d = b + i
                    f = False
                i += i
        return CaminhoArquivo(d, d)

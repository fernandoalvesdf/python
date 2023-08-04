import pytest
from codigo.caminho_arquivo import CaminhoArquivo
class TestCaminhoArquivo:
    def test_montar_caminho_para_arquivo(self):
        caminho_arquivo = CaminhoArquivo.instance(1)
        print(caminho_arquivo.diretorio)
        assert caminho_arquivo.diretorio == "/tmp/1"
        assert caminho_arquivo.arquivo == "/tmp/1/1"

        caminho_arquivo = CaminhoArquivo.instance(2)
        assert caminho_arquivo.diretorio == "/tmp/1"
        assert caminho_arquivo.arquivo == "/tmp/1/2"

        caminho_arquivo = CaminhoArquivo.instance(1000)
        assert caminho_arquivo.diretorio == "/tmp/1"
        assert caminho_arquivo.arquivo == "/tmp/1/1000"

        caminho_arquivo = CaminhoArquivo.instance(1500)
        assert caminho_arquivo.diretorio == "/tmp/2"
        assert caminho_arquivo.arquivo == "/tmp/2/1500"

        caminho_arquivo = CaminhoArquivo.instance(2000)
        assert caminho_arquivo.diretorio == "/tmp/2"
        assert caminho_arquivo.arquivo == "/tmp/2/2000"

        caminho_arquivo = CaminhoArquivo.instance(2001)
        assert caminho_arquivo.diretorio == "/tmp/3"
        assert caminho_arquivo.arquivo == "/tmp/3/2001"

## 9.6 O candidato deverá estar apto a realizar as seguintes ações na mesma prova, podendo ser questões distintas, contendo apenas uma dessas solicitações, ou mesmo todas elas em uma mesma questão:

### a) desenvolver um programa a partir de uma especificação, com ou sem acesso a banco de dados;
* 1 -  Criar uma classe Aluno no pacote model contendo os campos id, nome e email
* 2 -  Fazer o mapeamento da classe usando sqlalchemy
* 3 -  Criar um repository usando sqlalchemy
* 3 -  Criar um teste usando pytest e o sqlalchemy que salve e consulte Aluno

### b) desenvolver um programa que apresente os dados solicitados e(ou) calculados, a partir de entrada de dados;
* 1 - Criar no pacote model uma classe Empregado com os campo nome, email e salario
* 2 - Criar no pacote service uma classe chamada EmpregadoService e criar um método para calcular salário líquido, aplicando 9% de desconto de INSS sobre o salário
* 3 - Criar um main que receba como parâmetro o nome, email e salário. Após a execução escrever no console o nome, o email, o salario bruto salário líquido calculado

### c) desenvolver um programa que execute uma ou mais rotinas a partir de uma especificação de software;
* 1 - Criar uma classe Agenda com os campos nome, telefone e endereço
* 2 - Criar uma classe main passando o nome, telefone e endereço. O Objeto endereço deve ser salvo em um arquivo texto. O arquivo deve ser legível em um editor de texto

### d) encontrar erros no código-fonte em uma solução de software previamente disponibilizada e solucioná-los, detalhando cada erro encontrado e apresentando para cada erro a(s) solução(ções) necessária(s);

* 1 - Na classe CaminhoArquivo, consertar o bug no código e fazer o teste passar
* 2 - Refatorar o código. Técnicas como análise de complexidade ciclomática, duplicação de código, clean code e LOC serão utilizadas para avaliação;
> Atenção, a assinatura do método deve ser mantida, assim como os testes da classe CaminhoArquivoTest

### e) elaborar o teste unitário de um código-fonte disponibilizado.

* 1 - Fazer os testes de unidade da classe BancoService para os métodos:
    * adicionarConta
    * pesquisarContaDoCliente
    * listarContasAltaRenda

* 2 - A classe RedeBancariaService é responsável por registrar os bancos junto ao Banco Central (BACEN). BancoCentralGateway é um Gateway que faz chamadas ao WebService do BACEN. É necessário testar a classe RedeBancariaService unitariamente, sendo assim é necessário isolar a classe. Dessa forma, deve ser realizado o seguinte:
    * Criar 3 testes de sucesso do registro bancário, sendo um isolando a classe BancoCentralGateway com fake, com stub e com mock
    * Criar um teste de exceção usando mock, tendo como caso o cadastro do banco no BACEN tenha dado algum problema, a exceção BancoNaoCadastradoException usando MagicMock deve ser retornada.



### f) refatorar um código-fonte disponibilizado com objetivo de melhorá-lo sem que haja mudança na sua funcionalidade;

* 1 - Refatorar o método pesquisarContaDoCliente da classe BancoService para resolver os problemas de lentidão



## 9.7 Na prova de conhecimentos aplicados serão avaliados, no mínimo:
* a) sintaxe do código-fonte;
* b) avaliação do resultado (saída do software);
* c) correta execução do software a partir dos requisitos descritos, incluindo, dados de entrada e resultado esperado.
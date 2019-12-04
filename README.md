# Toth

<img src="https://user-images.githubusercontent.com/20601076/70105955-2644db00-1621-11ea-905c-9fe7b55cbe75.jpg">

Sistemas de gerenciamento de estoques de um conjunto de lojas de construção

## Pasta telas
* Os arquivos *.ui* são gerados no QtDesigner;
* Os arquivos *.py* desta pasta são extraído a partir do comando *pyuic5 -x arquivo.ui -o arquivo.py*;
* Os arquvis .png são gerados a partir de cada compra, e são sobrescrevido;
* O arquivo *stack_telas.py* é reponsavel pelo genrênciamento das mudanças das telas;
## Pasta Protótipos
* Os arquivos *.png* são os protótipos das telas para o desenvolvimento;
* O arquivo *.pdf* é a junção dos arquivos *.png* em um unico arquivo;
## Arquivos Externos
* Arquivo *Banco.py*, se refere a criação do banco de dados utilizando o **SQLite**, neste arquivo contem todas as consultas utilizadas; 
* Arquivo *principal.py*, se refere ao servidor, ele gerencia as atividades solicitadas pela filial;
* Arquivo *Loja*, banco de dados gerado com o **SQLite**;

## Pasta Classes
* Nesta pasta contem arquivos *.py* que são utilizados quando o trabalho estava utilizando a manipulação sem *server*;

## Necessidades para o Uso
* Python 3.6.9 ou Superiores;
* Biblioteca qrcode -> instalação com o PIP -> *pip3 install qrcode[pil]*
* Biblioteca Matplotlib -> instalação com o PIP -> *pip3 install matplotlib*
* Banco de dados SQLite3 -> instalação -> 
> sudo apt install sqlite3
>
> sudo apt install sqlite3 libsqlite3-dev
>
> sudo add-apt-repository ppa:linuxgndu/sqlitebrowser
>
> sudo apt install sqlitebrowser

* PyQt5 -> instalação com o PIP -> *pip3 install PyQt5*

## Telas da Aplicação
* Tela de Acesso

![tela_de_acesso](https://user-images.githubusercontent.com/20601076/70103165-0e695900-1619-11ea-920d-4e7958bd23ab.png)

* Tela de Estoque de Produtos

![tela_de_estoque_e_venda](https://user-images.githubusercontent.com/20601076/70103236-55574e80-1619-11ea-8dec-261577b8bcfc.png)

* Tela de Opções

![pagina_de_opcoes](https://user-images.githubusercontent.com/20601076/70103257-66a05b00-1619-11ea-85ec-bec05d8fdbe0.png)

* Tela de Listagem de Lojas

![tela_de_busca_de_lojas](https://user-images.githubusercontent.com/20601076/70103320-8e8fbe80-1619-11ea-94f3-f7d208f4ae48.png)

* Tela de Opções de Funcionários

![tela_de_opcoes_de_funcionario](https://user-images.githubusercontent.com/20601076/70103354-a5ceac00-1619-11ea-8e59-c18cb17b85df.png)

* Tela de Opções de Lojas

![pagina_de_opcoes_de_loja](https://user-images.githubusercontent.com/20601076/70103381-c7c82e80-1619-11ea-8a54-57a0b93bdfd7.png)

* Tela de Opções de Produtos

![tela_de_opcoes_de_produto](https://user-images.githubusercontent.com/20601076/70103404-d57db400-1619-11ea-8568-512fe81af9d4.png)

* Tela de Vendas

![tela_de_vendas](https://user-images.githubusercontent.com/20601076/70103446-eb8b7480-1619-11ea-8d99-eeca33b69981.png)

## Ferramentas Utilizadas
* Pycharm -> [Instalação do Pycharm ](https://www.youtube.com/watch?v=cVROiVgR_qg)
* Linux
* Qt Designer -> instalação -> *sudo apt-get install python-qt5 qt5-designer*
* DB Browser for SQLite -> *sudo apt-get install sqlitebrowser*

## Esquema de Funcionamento
![esquema](https://user-images.githubusercontent.com/20601076/70104773-df091b00-161d-11ea-8cde-8ce26c01f104.png)

## O que precisa ser Adicionado
- [ ] Gráfico mensal e de intervalos de tempo
- [ ] Ocultar senhas na digitação
- [ ] Não deixar qualquer funcionário alterar a senha
- [ ] Não deixar que seja vendas de produtos mais do que tem no estoque
- [ ] Utilizar um banco com IP (Internet Protocol) Fixo

## Responsáveis pelo trabalho
[Francisco Maik](https://github.com/FranciscoMaik)

[Francisco Nathanael](https://github.com/NatSilva)

## Licença
O Software **Toth**  é open-source licenciado pelo [MIT license](https://github.com/FranciscoMaik/toth/blob/master/LICENSE.md)
# Toth
Sistemas de gerenciamento de estoques de um conjunto de lojas de construção

* Adição da tela de vendas -> telas -> vender.py,vender.ui

* Alteração do arquivo home.py,home.ui para adição do botão vender

* Adição do banco de dados -> Banco de Dados -> Banco.py

* Alteração do arquivo stack_telas.py para incremento da funcionalidade vender

* Arquivo principal.py -> Até o presente momento não é visto a necessidade explicita de inclusão de multithreads, visto quê não há a concorrência de acesso a execução de programas simultâneos, fugindo desta forma do proposito de criação de multithreads.

* Telas alteradas, funções de exclusão, busca e alteração adicionada;

* Função venda mudada de tela;

* Servidor recebendo e tratando as mensagens;

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

    
    sudo apt install sqlite3
    sudo apt install sqlite3 libsqlite3-dev
    sudo add-apt-repository ppa:linuxgndu/sqlitebrowser
    sudo apt install sqlitebrowser
    
## Telas da Aplicação
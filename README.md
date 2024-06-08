# Lógica I

On35 | Semana 2 | 2024 | Agnes Ignácio

![enter image description here](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDhzdjVmdnNwdzZ3b2FmZ3VpZjRxbzdtamJzbjJnc3g4eDBxcDg0aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kQvyCMS08izkI/giphy.webp)

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)

### Resumo
O que veremos na aula de hoje?
* O que é Python?
* Variáveis
* Tipos de dados
* Operadores
* Funções

### O que é Pyhton?
Python é uma linguagem de programação amplamente usada em aplicações da Web, desenvolvimento de software, ciência de dados e machine learning (ML). Os desenvolvedores usam o Python porque é eficiente e fácil de aprender e pode ser executada em muitas plataformas diferentes.

 É uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.

### Variáveis
As variáveis em Python são fundamentais para o armazenamento e manipulação de dados. Elas agem como “caixas” ou “recipientes” que guardam informações. Essas informações podem variar de números a textos, passando por uma ampla variedade de tipos de dados. Uma das características marcantes do Python é a sua flexibilidade em atribuir e reatribuir diferentes tipos de dados a uma mesma variável, o que torna essa linguagem incrivelmente versátil e amigável para programadores de todos os níveis.

Em Python, uma variável é criada no momento em que você atribui um valor a ela. A atribuição é feita usando o sinal de igual (=). À esquerda do sinal, colocamos o nome da variável, e à direita, o valor que desejamos armazenar. Por exemplo, nome = "Maria" cria uma variável chamada nome e armazena a string “Maria” nela. Não é necessário declarar o tipo de dados antecipadamente, o Python é inteligente o suficiente para entender o tipo de dado baseado no valor atribuído.

Utilizar variáveis em Python é extremamente simples. Depois de criar uma variável e atribuir um valor a ela, você pode usar essa variável em operações, funções e como parte de expressões mais complexas. Por exemplo, `idade = 30` seguido por `print(idade + 5)` exibirá _35_ na tela. Isso demonstra como as variáveis podem ser utilizadas para armazenar dados e depois manipulados através do código.

### Tipos de dados

Python suporta diversos tipos de dados, e entender esses tipos é crucial para utilizar as variáveis de maneira eficaz. Os principais tipos são:  **inteiros**  (int), para números sem parte fracionária;  **floats**, para números com parte fracionária;  **strings**  (str), para texto; e  **booleanos**  (bool), que representam verdadeiro ou falso. Vamos explorar cada um desses tipos com mais detalhes.

* #### Inteiros e Floats

Os tipos inteiros e floats representam números em Python. Enquanto os inteiros são usados para números sem parte decimal, os floats são utilizados quando esta parte é necessária. A declaração desses tipos é feita de maneira intuitiva:  `numero_inteiro = 10`  e  `numero_float = 10.5`. É importante notar que operações matemáticas podem ser realizadas com essas variáveis, como adição, subtração, multiplicação e divisão, tornando Python uma ferramenta poderosa para cálculos numéricos.

* #### Strings

Strings são sequências de caracteres usadas para armazenar texto em Python. Elas podem ser declaradas usando aspas simples (`' '`) ou duplas (`" "`). Por exemplo:  `nome = "João"`  ou  `mensagem = 'Bem-vindo!'`. Strings em Python são objetos e, como tal, vêm com uma variedade de métodos úteis para manipulação de texto, como conversão para maiúsculas ou minúsculas, divisão de strings e substituição de caracteres.

* #### Booleanos

Os booleanos são um tipo de dados simples em Python, representando um de dois valores:  `True`  (verdadeiro) ou  `False`  (falso). Eles são particularmente úteis em estruturas condicionais e loops, permitindo que o programador controle o fluxo do programa com base em condições. Por exemplo,  `ativo = True`  pode ser usado para controlar se uma parte do código deve ser executada ou não.

* #### List

Uma lista é uma sequência de valores. É um tipo de “contêiner” usado para armazenar um número indefinido de dados arbitrários do mesmo tipo ou de tipos diferentes. Uma lista homogênea contém elementos do mesmo tipo, por exemplo,  _strings_:

    animais = ["gato", "cachorro", "pássaro", "leão"]

 Uma lista heterogênea combina diferentes tipos de dados:

    professora = ["agnes", 30, 1.83, true]

As listas são ordenadas, ou seja, a posição de suas informações importa e pode ser acessada por seu número (que chamamos de _index_), começando pelo número 0:

    professora[0] # "agnes"
    professora[1] # 30
    professora[2] # 1.83
    professora[3] # true

  

 * #### Dictionary

Um dicionário é uma estrutura de dados que permite armazenar dados em pares. Chamamos cada par de dados de par chave-valor. Assim, cada elemento em um dicionário consiste em uma chave e um valor associado a essa chave. Podemos utilizar esta associação para representar relações que existem no mundo real, como um produto e seu preço. Por exemplo:

    pessoa = {
	    "nome": "Paula", 
	    "idade": 29, 
	    "filhos": ["João", "Maria"]
    }

Para acessar uma das informações de um dicionário, usamos seu nome e a chave desejada entre aspas e colchetes:

    pessoa["idade"]

* #### NoneType

NoneType simboliza o vazio em Python. Apesar de ser um conceito um pouco abstrato, imagine que todos os outros tipos são caixas que contém coisas dentro e, no caso do NoneType, a caixa está vazia. Mais adiante no curso vamos entender melhor para que esse tipo serve e em que contextos nos deparamos com ele.

### Operadores

Os Operadores em Python possibilitam que a desenvolvedora consiga transcrever a lógica para o código. Em resumo, para fazermos afirmações comparando valores, precisamos da ajuda dos operadores para nos comunicarmos com Python.

* #### Operadores lógicos
Operador | Nome | Função
-------- |------|-------
`+`|**Adição**|Realiza a soma de ambos operandos.
`-`|**Subtração**|Realiza a subtração de ambos operandos.
`*`|**Multiplicação**|Realiza a multiplicação de ambos operandos.
`/`|**Divisão**|Realiza a Divisão de ambos operandos.
`//`|**Divisão inteira**|Realiza a divisão entre operandos e remove a parte decimal de ambos operandos.
`%`|**Módulo**|Retorna o resto da divisão de ambos operandos.
`**`|**Exponenciação**|Retorna o resultado da elevação da potência pelo outro.
 
* #### Operadores de comparação
Operador|Nome|Função
--------|----|------
`==`|Igual a|Verifica se um valor é igual ao outro
`!=`|Diferente de|Verifica se um valor é diferente ao outro
`>`|Maior que|Verifica se um valor é maior que outro
`>=`|Maior ou igual|Verifica se um valor é maior ou igual ao outro
`<`|Menor que|Verifica se um valor é menor que outro
`<=`|Menor ou igual|Verifica se um valor é menor ou igual ao outro

* #### Operadores de atribuição

Operador|Equivalente a
--------|----------
`=`|x = 1
`+=`|x = x + 1
`-=`|x = x - 1
`*=`|x = x * 1
`/=`|x = x / 1
`%=`|x = x % 1

* #### Operadores lógicos

Operador|Definição
--------|------
`and`|Retorna True se ambas as afirmações forem verdadeiras
`or`|Retorna True se uma das afirmações for verdadeira
`not`|retorna Falso se o resultado for verdadeiro

* #### Operadores de identidade
Operador|Definição
--------|---------
`is`|Retorna  `True`  se ambas as variáveis são o mesmo objeto
`is not`|Retorna  `True`  se ambas as variáveis não forem o mesmo objeto

### Funções

As funções permitem definir um bloco de código reutilizável que pode ser executado muitas vezes dentro de um programa. É uma estrutura que agrupa partes do código, criando soluções modulares para problemas complexos.

As funções em Python cumprem objetivos específicos definidos pelo usuário ou pela linguagem. Eles recebem como parâmetros dados de entrada chamados argumentos que são indicados pelo usuário ou automaticamente, sendo processados e retornando como dados de saída.

* #### Funções built-in
São funções nativas, ou seja, já vêm programadas na linguagem e prontas para serem utilizadas. Alguns exemplos são:
* * print() - retorna uma informação no terminal, inserida como parâmetro entre os parenteses.
* * input() - captura uma informação inserida pela pessoa usuária no terminal.
* * type() - retorna o tipo do dado inserido como parâmetro, entre os parenteses.
* * str() - retorna o dado inserido como parâmetro, entre parenteses, traduzido para o tipo string.

Aqui está uma [lista de built-in functions em Python](https://docs.python.org/3/library/functions.html).
* #### Funções personalizadas
Também é possível que nós criemos nossas próprias funções, para reutilizarmos um trecho de código inúmeras vezes. Para isso, utilizamos a seguinte sintaxe:

    def nome_da_funcao(parametro1, parametro2):
	    codigo_a_ser_repetido...
	    return valor_a_ser_retornado # se houver

Depois disso, se quisermos invocar essa função:

    nome_da_funcao(parametro1, parametro 2)


### Links úteis
* [O que é Python? - AWS](https://aws.amazon.com/pt/what-is/python/#:~:text=O%20Python%20%C3%A9%20uma%20linguagem,executada%20em%20muitas%20plataformas%20diferentes.)
* [Python - Wikipedia](https://pt.wikipedia.org/wiki/Python)
* [Variáveis - O que são, tipos de dados](https://didatica.tech/tudo-sobre-variaveis-em-python-aprenda-com-exemplos-praticos/#:~:text=Em%20Python,%20uma%20vari%C3%A1vel%20%C3%A9,a%20string%20%E2%80%9CMaria%E2%80%9D%20nela.)
* [Listas - EBAC](https://ebaconline.com.br/blog/listas-em-python-seo)
* [Dicionários - Asimov Academy](https://hub.asimov.academy/blog/dicionario-python/)
* [Operadores em Python - Python Academy](https://pythonacademy.com.br/blog/operadores-aritmeticos-e-logicos-em-python)
* [Funções](https://ebaconline.com.br/blog/funcoes-python)
* [Exercícios - Python Brasil](https://wiki.python.org.br/EstruturaSequencial)

# Entendendo o PYTEST_ADDOPTS e como desabilitar warnings no pytest




Ao executar testes automatizados em Python, é comum receber avisos (warnings) durante a execução dos testes. Para lidar com esses avisos, o Pytest oferece diversas opções para desativá-los. Neste artigo vamos explorar como utilizar a `PYTEST_ADDOPTS` para desabilita-los.



## Entendendo o problema

Vamos imaginar que estamos executando testes em uma aplicação **Python** utilizando o **Pytest** e nos deparamos com a seguinte saída:


```bash
===================================== warnings summary ======================================
tests/test_translator.py::test_translator_hello_world
tests/test_translator.py::test_api_manager
  /home/ztz/projects/ztranslator/.venv/lib/python3.10/site-packages/httpx/_config.py:156: DeprecationWarning: ssl.PROTOCOL_TLS is deprecated
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

tests/test_translator.py::test_translator_hello_world
tests/test_translator.py::test_api_manager
  /home/ztz/projects/ztranslator/.venv/lib/python3.10/site-packages/httpx/_config.py:159: DeprecationWarning: ssl.OP_NO_SSL*/ssl.OP_NO_TLS* options are deprecated
    context.options |= ssl.OP_NO_TLSv1

tests/test_translator.py::test_translator_hello_world
tests/test_translator.py::test_api_manager
  /home/ztz/projects/ztranslator/.venv/lib/python3.10/site-packages/httpx/_config.py:160: DeprecationWarning: ssl.OP_NO_SSL*/ssl.OP_NO_TLS* options are deprecated
    context.options |= ssl.OP_NO_TLSv1_1

-- Docs: https://docs.pytest.org/en/stable/warnings.html
```



Esses avisos podem ser gerados por diversos motivos, como o uso de funções obsoletas, comportamentos não recomendados, entre outros, sendo úteis para que o desenvolvedor identifique possíveis problemas na sua aplicação ou nas bibliotecas utilizadas. No entanto, em alguns casos, eles podem não ser importantes para o teste em questão ou podem simplesmente ser irritantes, sujando a tela e tirando o foco do resultado dos testes. 


## Utilizando o PYTEST_ADDOPTS


> PYTEST_ADDOPTS¶ 
> This contains a command-line (parsed by the py:mod:shlex module) that will be prepended 
> to the command line given by the user, see Builtin configuration file options 
> for more information.



O **PYTEST_ADDOPTS** é uma variável de ambiente, que armazena parâmetros de linha de comando, que durante a execução do pytest serão adicionados a linha de comando fornecida pelo usuário. É possível defini-la exportando-a no terminal ou direto no arquivo `Makefile`. Para desabilitar os avisos (warnings) no pytest, podemos utilizar a opção `-p no:warnings`.


### Desativar os avisos usando o makefile

Para utilizar o `PYTEST_ADDOPTS` em conjunto com o `Makefile`, podemos definir a variável de ambiente no início do arquivo, antes da definição da regra `test`. Veja o exemplo abaixo:

```bash

export PYTEST_ADDOPTS=-p no:warnings

.PHONY: test
test:
    poetry run pytest -s -v
``` 

Com a variável `PYTEST_ADDOPTS` definida, o `pytest` será executado com a opção `-p no:warnings`, que desabilita todos os avisos (warnings) durante a execução dos testes. Caso você queira desabilitar somente alguns avisos específicos, é possível utilizar a opção `-W` do `pytest` em conjunto com a opção `-p no:warnings`. Veja o exemplo abaixo:


```bash

export PYTEST_ADDOPTS=-p no:warnings -W ignore::DeprecationWarning

.PHONY: test
test:
    poetry run pytest -s -v
```

Com a opção `-W ignore::DeprecationWarning`, o `pytest` irá desabilitar somente os avisos do tipo `DeprecationWarning`. 

### Desativando os avisos na linha de comando

Além de definir a variável de ambiente no arquivo `makefile`, também é possível exportá-la na linha de comando utilizando o comando `export`. Veja o exemplo abaixo:

```
$ export PYTEST_ADDOPTS="-p no:warnings"
$ poetry run pytest -s -v
```

Para remover a variável `PYTEST_ADDOPTS`, use o comando:

```
$ unset PYTEST_ADDOPTS
```

Utilizando o comando `env` a variável de ambiente `PYTEST_ADDOPTS` será definida apenas para a execução do `pytest` e não afetará outras execuções. Veja o exemplo abaixo:  

``` 
$ env PYTEST_ADDOPTS="-p no:warnings" pytest -s -v
```

## Conclusão

O [Pytest](https://docs.pytest.org/en/7.2.x/) é uma ferramenta importante para garantir a qualidade do código em projetos Python. No entanto, durante a execução dos testes automatizados, podem ser gerados avisos (warnings) que, em alguns casos, podem ser irrelevantes ou irritantes. Nesse sentido, a opção `-p no:warnings`, definida na variável de ambiente [PYTEST_ADDOPTS¶](https://docs.pytest.org/en/7.2.x/reference/reference.html#envvar-PYTEST_ADDOPTS) pode ser utilizada para desativar todos os avisos durante a execução dos testes. No entanto, é importante lembrar que esses avisos podem conter informações importantes para identificar possíveis problemas na aplicação ou bibliotecas utilizadas. Portanto, a desativação dos avisos deve ser feita com cuidado e de forma criteriosa, de modo a não comprometer a qualidade do código.



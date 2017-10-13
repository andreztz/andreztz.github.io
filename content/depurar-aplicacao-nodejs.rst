Como depurar aplicações em nodejs.
##################################

:date: 2017-10-13 04:27
:category: nodjs
:tags: javascript, nodejs, depurar, debug

Muitas ferramentas e bibliotecas estão disponíveis para ajudá-lo a depurar
aplicativos desenvolvidos com nodejs, o próprio já possui uma ferramenta de depuração, 
basta executá-lo passando "inspect" como argumento seguido do caminho do 
script que será depurado.


.. code-block:: ps1con

    $ node --inspect --inspect-brk app.js


Agora basta acessar a seguinte url no navegador:

chrome://inspect

Pronto, é só depurar no browser!


`debugger <https://nodejs.org/api/debugger.html>`_

`inspector <https://nodejs.org/en/docs/inspector>`_

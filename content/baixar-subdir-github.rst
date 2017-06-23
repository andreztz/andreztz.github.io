Como baixar subdiretorios em projetos do GitHub
###############################################

:date: 2017-06-22
:category: github
:tags: git, github, svn, subversion


Se você deseja baixar um projeto inteiro do GitHub sem os dados de controle de versão,
você pode usar a opção Download ZIP do site.

Alternativamente, você pode usar ferramentas de linha de comando, por exemplo:

.. code-block:: bash

  $ curl -L -o pyqt5-master.zip https://github.com/baoboa/pyqt5/archive/master.zip

E se você quiser baixar apenas um subdiretório? O site não tem uma opção para isso,
pelo menos ainda não. Isso não é problema! Graças ao suporte do Subversion no GitHub,
você pode usar a ferramenta de linha de comando svn para esse efeito.
Por exemplo, digamos que nosso alvo seja o diretório activeqt do projeto pyqt5.

A url do nosso alvo é ``https://github.com/baoboa/pyqt5/tree/master/examples/activeqt``

usando o formato ``https://github.com/USER/PROJECT/trunk/PATH DEST`` temos:

USER = baoboa

PROJECT = pyqt5

PATH = examples/activeqt

DEST = webbrowser

``https://github.com/baoboa/pyqt5/trunk/examples/activeqt webbrowser``

agora podemos deixar o resto por conta do svn.

.. code-block:: bash

  $ svn export https://github.com/baoboa/pyqt5/trunk/examples/activeqt browser

Isso cria um diretório localmente com o conteúdo do subdiretório especificado do projeto.

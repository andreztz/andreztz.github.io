Como instalar o Wxpython3 Phoenix.
##################################

:date: 2017-10-06 17:45
:category: python
:tags: python3, wxpython, wxpython3, Phoenix
:Image: https://upload.wikimedia.org/wikipedia/commons/c/c0/WxPython-logo.png



wxPython é um wrapper da biblioteca wxWidgets. Assim como a Tkinter, as aplicações são facilmente portáveis. A diferença é que a wxWidgets utiliza um wrapper sobre a interface gráfica padrão do sistema operacional (GTK em Linux, MFC em Windows), o que permite que as aplicações sejam mais facilmente portáveis e que tenham a aparência de uma aplicação nativa.

.. code-block:: bash

    $ sudo mount -o remount,size=4G /tmp
    $ virtualevn -p python3 venv
    $ source venv/bin/activate
    (venv) $ pip install -U --pre -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython 


`snapshot-builds <https://wxpython.org/Phoenix/snapshot-builds/>`_

Como configurar teclas de atalho no Openbox.
############################################

:date: 2017-03-07 01:51
:category: linux
:tags: archlinux, openbox
:Image: https://www.gadgetdaily.xyz/wp-content/uploads/2012/12/archbang1web.png


Teclas de atalho fornecem um método rápido e fácil para a execução comandos, a partir de uma combinação de teclas predefinida.
No openbox, para definir uma tecla de atalho basta editar o arquivo ~/.config/openbox/rc.xml.



Syntax
------

.. code-block:: python

    <keyboard>
        ...
        <keybind key="KEY-COMBINATION...">
          ...ACTIONS...
        </keybind>
        ...
     </keyboard>

KEY-COMBINATION é a combinação de teclas para ligar à uma ação. O formato para KEY-COMBINATION é: Modificador-Modificador-tecla (ex.: C-S-T). Qualquer número de modificadores (0 ou mais) podem ser usados juntos e cada um é separado por um "-".


Modificadores
-------------

* S tecla Shift
* C tecla Control
* A tecla Alt
* W tecla Super (tecla Windows)
* M tecla Meta
* H tecla Hyper


Exemplo
-------


.. code-block:: xml

    <keybind key="S-A-T">
        <action name="Execute">
            <command>python /caminho/para/executável</command>
        </action>
    </keybind>

O Openbox nem sempre reflete automaticamente as alterações feitas em seus arquivos de configuração. Consequentemente, será necessário recarregar manualmente esses arquivos depois de editados.

.. code-block:: zsh

    $ openbox --reconfigure

`Referencia: http://openbox.org/wiki/Help:Bindings#Key_bindings <http://openbox.org/wiki/Help:Bindings#Key_bindings>`_

Como fazer backup de drivers no Windows
#######################################

:date: 2017-04-07
:category: windows
:tags: windows

Abra o prompt de comando do Windows.

Fazendo backup dos drivers
---------------------------

No prompt de comando digite:

.. code-block:: ps1con

    c:\> dism /online /export-driver /destination:D:\backup_drivers


Restaurando o backup dos drivers
--------------------------------

Os drivers do backup podem ser restaurados pelo gerenciador de dispositivos do Windows solicitando à partir dali a instalação do driver de dispositivo em questão.

Para restaurar todos os drivers de uma vez só pelo prompt de comando digite:

.. code-block:: ps1con

    c:\> dism /online /Add-Driver /Driver:D:\backup_drivers /Recurse


Todos os comandos acima devem ser executados com privilégios administrativos.

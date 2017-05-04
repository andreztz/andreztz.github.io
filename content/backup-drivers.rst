Como fazer backup de drivers no Windows
#######################################

:date: 2017-04-07
:category: windows
:tags: windows

Neste post veremos duas maneiras para fazer backup de drivers no Windows usando ferramentas internas do sistma. A primeira é usar o dism.exe ("Deployment Image Servicing and Management Tool") no velho prompt de comando e a segunda é usar o PowerShell, que de qualquer forma vai chamar o dism em background.


Fazendo backup de drivers
---------------------------

No prompt de comando:

.. code-block:: ps1con

    C:\Windows\System32> dism /online /export-driver /destination:D:\backup_drivers


No PowerShell:

.. code-block:: ps1con

    PS C:\WINDOWS\system32> Export-WindowsDriver -Online -Destination D:\Drivers-Backup


O resultado dos dois comandos acima é o mesmo.

Restaurando o backup de drivers
--------------------------------

Os drivers do backup podem ser restaurados pelo gerenciador de dispositivos do Windows solicitando à partir dali a instalação do driver de dispositivo em questão.

Para restaurar todos os drivers de uma vez só no prompt de comando:


.. code-block:: ps1con

    c:\> dism /online /Add-Driver /Driver:D:\backup_drivers /Recurse


Todos os comandos acima devem ser executados com privilégios administrativos.

https://msdn.microsoft.com/en-us/windows/hardware/commercialize/manufacture/desktop/what-is-dism

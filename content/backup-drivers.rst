Como fazer backup de drivers no Windows
#######################################

:date: 2017-04-07
:category: windows
:tags: windows

Existem muitas maneiras de fazer backup de drivers de dispositivos no Windows, nesse post vamos ver duas maneiras que fazem uso de ferramentas internas do Windows. A primeira é usar o dism.exe ("Deployment Image Servicing and Management Tool") no prompt do Windows, a segunda é usar o PowerShell que de qualquer forma vai chamar o dism em background.


No prompt de comando do Windows.

Fazendo backup de drivers
---------------------------

No prompt de comando:

.. code-block:: ps1con

    C:\Windows\System32> dism /online /export-driver /destination:D:\backup_drivers


No PowerShell:

.. code-block:: ps1con

    PS C:\WINDOWS\system32> Export-WindowsDriver -Online -Destination D:\Drivers-Backup


O resultado dos comandos acima é o mesmo.

Restaurando o backup de drivers
--------------------------------

Os drivers do backup podem ser restaurados pelo gerenciador de dispositivos do Windows solicitando à partir dali a instalação do driver de dispositivo em questão.

Para restaurar todos os drivers de uma vez só no prompt de comando:


.. code-block:: ps1con

    c:\> dism /online /Add-Driver /Driver:D:\backup_drivers /Recurse


Todos os comandos acima devem ser executados com privilégios administrativos.

https://msdn.microsoft.com/en-us/windows/hardware/commercialize/manufacture/desktop/what-is-dism

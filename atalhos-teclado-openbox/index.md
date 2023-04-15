# Como configurar teclas de atalho no Openbox


Teclas de atalho fornecem um método rápido e fácil para a executar comandos a partir de uma combinação de teclas predefinida.
No openbox para definir uma tecla de atalho basta editar o arquivo ~/.config/openbox/rc.xml.


## Syntax


```xml {linenos=true}
<keyboard>
    ...
    <keybind key="KEY-COMBINATION...">
    ...ACTIONS...
    </keybind>
    ...
</keyboard>
```

KEY-COMBINATION é a combinação de teclas que liga a uma ação. O formato para KEY-COMBINATION é: Modificador-Modificador-Tecla (ex.: C-S-T). Qualquer número de modificadores (0 ou mais) podem ser usados juntos e cada um é separado por um "-".


# Modificadores

* S tecla Shift
* C tecla Control
* A tecla Alt
* W tecla Super (tecla Windows)
* M tecla Meta
* H tecla Hyper


# Exemplo

```xml {linenos=true}
<keybind key="S-A-T">
    <action name="Execute">
        <command>python /caminho/para/executável</command>
    </action>
</keybind>

```


O Openbox nem sempre reflete automaticamente as alterações feitas em seus arquivos de configurações, consequentemente será necessário recarregar manualmente esses arquivos depois de editados.

```bash-session
$ openbox --reconfigure
```

[Referência: http://openbox.org/wiki/Help:Bindings#Key_bindings](http://openbox.org/wiki/Help:Bindings#Key_bindings)


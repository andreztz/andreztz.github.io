# Depurar strings com caracteres invisiveis


Recentemente, precisei criar um script bash que iterava sobre o barramento 
USB, listando os dispositivos conectados e comparando seus nomes com uma lista
de dispositivos específicos que eu queria configurar. 

Primeiro identifiquei o nome dos dispositivos com um loop:

```
$ for d in /sys/bus/usb/devices/*/product; do
  printf "%s: " "$(cat "$d")"
  echo "$d"
done
USB OPTICAL MOUSE : /sys/bus/usb/devices/2-3/product
Gaming KB : /sys/bus/usb/devices/2-4/product
EHCI Host Controller: /sys/bus/usb/devices/usb1/product
xHCI Host Controller: /sys/bus/usb/devices/usb2/product
EHCI Host Controller: /sys/bus/usb/devices/usb3/product
xHCI Host Controller: /sys/bus/usb/devices/usb4/product
xHCI Host Controller: /sys/bus/usb/devices/usb5/product
xHCI Host Controller: /sys/bus/usb/devices/usb6/product

```

A ideia parecia simples, verificar se o nome do dispositivo, por exemplo USB 
OPTICAL MOUSE, correspondia a um item da minha lista e, se sim, executar um comando.

No entanto, ao rodar o script, percebi que a comparação nunca entrava no bloco
condicional, mesmo quando o texto parecia ser igual. Usei o comando `echo`
para  imprimir o valor das variáveis, mas tudo parecia correto, até que me dei
conta que o problema estava nos caracteres "invisíveis".

Arquivos no `/sys` geralmente contêm uma quebra de linha `\n` no final, e em 
alguns casos, podem incluir espaços em branco adicionais. Esses caracteres não 
são visíveis com o `echo`, mas afetam as comparações de strings. 


## Identificando caracteres "invisíveis"

Para depurar esse tipo de problema, é importante inspecionar o conteúdo real da
string, incluindo caracteres de controle. Aqui estão alguns métodos úteis:

1. Usando o comando `hexdump`

```
cat /sys/bus/usb/devices/2-3/product | hexdump -C
00000000  55 53 42 20 4f 50 54 49  43 41 4c 20 4d 4f 55 53  |USB OPTICAL MOUS|
00000010  45 20 0a                                          |E .|
00000013
```

O `hexdump` exibe os bytes em formato hexadecimal na coluna do meio e sua 
representação em string (ASCII) na coluna da direita. No exemplo, o `20` representa 
um espaço (caractere imprimível) e o `0a` representa a quebra de linha (`\n`, um 
caractere de controle e não imprimível). Repare que há um espaço (`20`) antes do 
`0a`, o que, embora seja um caractere imprimível, é "invisível" ao usar `echo` 
e foi a causa do problema.

2. Usando o comando `cat`

```
$ cat -A /sys/bus/usb/devices/2-3/product
USB OPTICAL MOUSE $
```

Nesse caso, a opção `-A` exibe os caracteres não imprimíveis. O simbolo `$` 
indica a quebra de linha (`\n`)

3. Usando o comando `od`

```
od -c /sys/bus/usb/devices/2-3/product
0000000   U   S   B       O   P   T   I   C   A   L       M   O   U   S
0000020   E      \n
0000023
```

Com `od -c`, você pode ver claramente os espaços e a quebra de linha na representação 
do caractere.

## Corrigindo o problema

Em Python, um simples `str.strip()` resolve o problema, removendo espaços e quebras
de linha do início e do final da string. No entanto, no Bash, e as alternativas 
são muitas. Para esse caso, o comando `xargs` foi suficiente.

```
product_name=$(<"$product_file")
product_name=$(echo "$product_name" | xargs) # remove espaços e quebras de linha
```

## Conclusão

Ao trabalhar com strings de arquivos de sistema, especialmente nos diretórios 
`/sys` e `/proc`, é fundamental ter em mente que caracteres invisíveis podem 
comprometer suas comparações.

Ferramentas como `hexdump`, `od` e `cat -A` são essenciais para a depuração, 
pois permitem visualizar o conteúdo real do arquivo e entender por que seu 
código não está se comportando como esperado.

[Padrão ASCII](https://pt.wikipedia.org/wiki/ASCII)



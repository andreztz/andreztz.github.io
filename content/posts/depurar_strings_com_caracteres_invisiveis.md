---
title: "Depurar_strings_com_caracteres_invisiveis"
date: 2025-08-09T18:46:47-03:00
draft: false
---

Recentemente, precisei criar um script bash o qual iterava sobre o barramento 
USB, listando os dispositivos conectados e comparando seus nomes com uma lista
de dispositivos específicos que eu queria configurar. 

Primeiro identifiquei o nome dos dispositivos:

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

A idéia parecia simples: verificar se o nome do dispositivo, por exemplo USB 
OPTICAL MOUSE, correspondia a um item da minha lista e, se sim, executar um comando.

No entanto, ao rodar o script, percebi que a comparação nunca entrava no bloco
condicional, mesmo quando aparentemente o texto era igual. Usei o comando `echo`
para  imprimir o valor das variáveis, mas tudo parecia correto, até que percebi 
que o problema estava nos caracteres "invisíveis".

Arquivos no `/sys` geralmente contêm uma quebra de linha `\n` no final, e em 
alguns casos podem incluir espaços em branco adicionais. Esses caracteres não 
são visíveis com o `echo`, e afetam comparações de strings. 



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

O hexdump na coluna do meio, exibe os bytes representados em hexadecimal, na 
diretira a sua representação em forma de string (ASCII) correspondentes da 
coluna do meio. No nosso exemplo, na sequência da coluna do meio o `20` 
representa espaço (imprimível), temos três. O `0a` representa o caractere de 
controle de quebra de linha `\n` (não imprimível). Note que existe um espaço 
em branco antes do útimo caractere `\n`, esse embora imprimível, é invisível 
ao usar o `echo`, sendo a causa do problema.


2. Usando o comando `cat`

```
$ cat -A /sys/bus/usb/devices/2-3/product
USB OPTICAL MOUSE $
```

Nesse caso o caractere `$` indica a quebra de linha (`\n`)

3. Usando o comando `od`

```
od -c /sys/bus/usb/devices/2-3/product
0000000   U   S   B       O   P   T   I   C   A   L       M   O   U   S
0000020   E      \n
0000023
```
Aqui é possível ver claramente os espaço e a quebra de linha.

## Corrigindo o problema

Em python um simples `str.strip()` remove espaços e quebra de linha do início e
do final da string, garantindo que a comparação funcione. Entre tanto, estamos
lidando com Bash, e as alternativas são muitas, o comando xargs foi suficiente.

```
product_name=$(<"$product_file")
product_name=$(echo "$product_name" | xargs) # remove espaços e quebras de linha
```

## Conclusão

Quando trabalhamos com strings provenientes de arquivos de sistema, especialmente
no `/sys` e `/proc`, é fundamental lembrar que caracteres invisíveis podem quebrar 
comparações.

Ferramentas como `hexdump`, `od` e `cat -A` podem ser usadas para depuração, 
permitindo enxergar o que está no arquivo e entender por que seu código não está
se comportando como esperado.

[Padrão ASCII](https://pt.wikipedia.org/wiki/ASCII)


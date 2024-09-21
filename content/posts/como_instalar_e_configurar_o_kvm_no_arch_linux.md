---
title: "Máquinas virtuais no Arch Linux"
date: 2023-07-24T00:22:42-03:00
draft: false
---

## KVM (Kernel-Based Virtual Machine)

KVM é uma infraestrutura de virtualização integrada ao Linux é faz uso das extensões de virtualização do processador (como Intel VT-x e AMD-V). O KVM é composto do modulo do kernel kvm.ko que fornece a infraestrutura principal de virtualização e modulos especificos para processadores kvm-intel.ko e kvm-amd.ko. 

O KVM permite que uma máquina host execute vários ambientes virtuais isolados, chamados de máquinas virtuais (VMs), transformando o Linux em um [hipervisor](https://pt.wikipedia.org/wiki/Hipervisor). O KVM faz parte do kernel Linux a partir da versão 2.6.20.

## QEMU

O QEMU é um emulador e virtualizador de máquinas de código aberto. Ele permite a execução de sistemas operacionais e programas de diferentes plataformas (como ARM) em uma máquina host (como um PC x86) através de uma técnica chamada tradução dinâmica. Esta técnica traduz, em tempo real, o código de máquina de uma arquitetura para outra, possibilitando um desempenho eficiente em comparação com métodos mais lentos, como a interpretação de instruções.

Quando utilizado como virtualizador, o QEMU pode empregar hipervisores como KVM ou Xen, utilizando extensões de CPU (Intel VT-x ou AMD-V) para permitir que várias máquinas virtuais rodem simultaneamente no mesmo hardware. Isso resulta em um desempenho quase nativo, já que o código do sistema convidado é executado diretamente na CPU do host.

## Diferença entre Emulador e Virtualizador:

- **Emulador**: Simula completamente o hardware de uma máquina diferente, permitindo a execução de sistemas operacionais e programas de uma arquitetura de CPU específica em outra. Este processo envolve tradução de instruções, o que geralmente resulta em desempenho mais lento.

- **Virtualizador**: Permite a execução simultânea de múltiplos sistemas operacionais compatíveis com a arquitetura do host em um único hardware. Quando usado com KVM, o QEMU executa máquinas virtuais da mesma arquitetura da CPU do host, evitando a emulação e proporcionando desempenho próximo ao nativo.

### Pré-instalação

Para verificar se seu sistema suporta a virtualização, execute os seguintes comandos:

```
LC_ALL=C lscpu | grep Virtualization
Virtualization:                  VT-x
```

```
grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo
...
```

Se esses comandos não retornarem nenhum resultado, é provável que o suporte à virtualização esteja desativado na configuração do BIOS/UEFI. A maioria dos processadores x86_64 AMD/Intel desenvolvidos a partir de 2000/2001 suportam virtualização.

### Instalando pacotes necessários

O primeiro passo é instalar os pacotes necessários para executar o KVM:

```
sudo pacman -S --needed qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat ebtables iptables-nft
```

### Libguestfs

A Libguestfs é uma coleção de ferramentas úteis para executar tarefas comuns em imagens de disco de VMs de forma segura, como acessar e editar arquivos, monitorar discos, clonar VMs, criar VMs e muito mais. Também vem com um shell interativo (guestfish e virt-rescue).

O pacote libguestfs esta disponível no repositório extra do Arch Linux, por tanto esse deve estar habilitado.

```
sudo pacman -S --noconfirm --needed libguestfs 
```

### Iniciando o serviço libvirt no boot

```
sudo systemctl enable libvirtd.service && systemctl start libvirtd.service
```

### Gerenciando KVMs como usuário padrão

Para gerenciar KVMs como usuário padrão, execute os seguintes comandos:

```
sudo usermod -a -G libvirt $(whoami)
newgrp libvirt
```

### Reiniciando o serviço libvirt

```
sudo systemctl restart libvirtd.service
```

### Suporte para UEFI

Para habilitar o suporte ao UEFI, instale o pacote `ovmf` com o comando:

```
sudo pacman -S ovmf
```





[O que é KVM?](https://www.redhat.com/pt-br/topics/virtualization/what-is-KVM)

[archlinux kvm](https://wiki.archlinux.org/title/KVM)

[libvirt](https://wiki.archlinux.org/index.php/Libvirt)

[Libguestfs](http://www.libguestfs.org/)

[Gerenciar KVMs como usuário padrão](https://documentation.suse.com/sles/11-SP4/html/SLES-kvm4zseries/cha-libvirt-connect.html)

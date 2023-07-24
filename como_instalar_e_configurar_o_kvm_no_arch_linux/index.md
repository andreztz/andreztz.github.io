# KVM: uma ferramenta poderosa para virtualizar no Arch Linux


## KVM (Kernel-Based Virtual Machine) no Arch Linux

KVM é uma infraestrutura de virtualização integrada ao Linux. Permite que uma máquina host execute vários ambientes virtuais isolados, chamados de máquinas virtuais (VMs), transformando o Linux em um hipervisor. O KVM faz parte do kernel Linux a partir da versão 2.6.20.

### Pré-instalação

Para verificar se seu sistema suporta a virtualização, execute os seguintes comandos:

```
$ LC_ALL=C lscpu | grep Virtualization
Virtualization:                  VT-x
```

```
$ grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo
...
```

Se esses comandos não retornarem nenhum resultado, é provável que o suporte à virtualização esteja desativado na configuração do BIOS/UEFI. Os processadores x86_64 AMD/Intel dos últimos 10 anos todos suportam a virtualização.

### Instalando pacotes necessários

O primeiro passo é instalar os pacotes necessários para executar o KVM:


$ sudo pacman -S --needed qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat ebtables iptables-nft


### Libguestfs

A Libguestfs é uma coleção de ferramentas úteis para executar tarefas comuns em imagens de disco de VMs de forma segura, como acessar e editar arquivos, monitorar discos, clonar VMs, criar VMs e muito mais. Também vem com um shell interativo (guestfish e virt-rescue).

```
$ yay -S --noconfirm --needed libguestfs
```

### Iniciando o serviço libvirt no boot

```
# systemctl enable libvirtd.service && systemctl start libvirtd.service
```

### Gerenciando KVMs como usuário padrão

Para gerenciar KVMs como usuário padrão, você precisa alterar as seguintes configurações no arquivo `/etc/libvirt/libvirtd.conf`:

```
unix_sock_group = "libvirt"
unix_sock_rw_perms = "0770"
auth_unix_rw = "none"
```

Em seguida, adicione o usuário ao grupo libvirt:

```
$ sudo usermod -a -G libvirt $(whoami)
$ newgrp libvirt
```

### Reiniciando o serviço libvirt

```
$ sudo systemctl restart libvirtd.service
```

### Suporte para UEFI

Para habilitar o suporte ao UEFI, instale o pacote `ovmf` com o seguinte comando:

```
$ sudo pacman -S ovmf
```

### Conclusão

Este blog post forneceu um guia passo a passo sobre como instalar e configurar o KVM no Arch Linux.


[O que é KVM?](https://www.redhat.com/pt-br/topics/virtualization/what-is-KVM)

[archlinux kvm](https://wiki.archlinux.org/title/KVM)

[libvirt](https://wiki.archlinux.org/index.php/Libvirt)

[Libguestfs](http://www.libguestfs.org/)

[Gerenciar KVMs como usuário padrão](https://documentation.suse.com/sles/11-SP4/html/SLES-kvm4zseries/cha-libvirt-connect.html)


---
title: "Protegendo o acesso a interface web do Openwrt"
date: 2022-04-05T03:49:21-03:00
draft: false
---

O Openwrt pode ser gerenciado no terminal via ssh, ou pela interface web do usuário [LuCI](https://openwrt.org/docs/guide-user/luci/start). O uso da interface web facilita a administração do sistema, no entanto, por padrão a interface web não tem suporte a conexão segura usando o  HTTPS. Por esse motivo  existe o risco de um invasor capturar o tráfego de rede e obter as credenciais de autenticação, visto que a troca de mensagens entre cliente e servidor sem a camada de segurança do HTTPS (SSL/TLS) é feito em texto puro.


![captura do tráfego http com wireshark](/images/openwrt_captura_de_credenciais.png)


O Openwrt oferece a opção de implementar o HTTPS,  mas é preciso gerar e armazenar um certificado TLS autoassinado e requer a instalação de pacotes adicionais (uci-ssl e dependências). No caso de dispositivos com pouca memoria, instalar pacotes adicionais não é uma opção, então gostaria de apresentar outra configuração que pode ser usada para proteger o acesso à interface web do Openwrt, que é **encapsular o tráfego http via ssh**.

Primeiro vamos fazer uma cópia e olhar o arquivo de configuração padrão do servidor web.

```
$ scp openwrt:/etc/config/uhttpd ~
uhttpd                                                       100%  710   458.3KB/s   00:00 
```

```
$ head ~/uhttpd 
# Server configuration
config uhttpd main

	# HTTP listen addresses, multiple allowed
	list listen_http	0.0.0.0:80
	list listen_http	[::]:80

	# HTTPS listen addresses, multiple allowed
	list listen_https	0.0.0.0:443
	list listen_https	[::]:443
```

Usando o comando `netstat -apn | grep :80` listamos os soquetes TCP/IP abertos pelo servidor web.

```bash-session
root@openwrt:~# netstat -apn | grep :80
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      
tcp        0      0 :::80                   :::*                    LISTEN
root@openwrt:~# netstat -ana | grep :443
root@openwrt:~# 
```

A linha `0.0.0.0:80` nos diz que o computador local esta ouvindo a porta 80, a espera de conexões de qualquer computador remoto.  O `0.0.0.0` é um endereço especial que representa todas as interfaces de rede com um IP válido nesse host, por exemplo,  poderíamos ter duas interfaces com os seguintes endereços `192.168.1.1`, `172.17.0.2`  como o servidor web escuta usando o endereço  `0.0.0.0:80` ambos respondem por esse endereço de socket.


Agora  a configuração do servidor web uHTTPd deve ser ajustada, para fazer isso conectamos ao roteador via SSH e abrimos o arquivo `/etc/config/uhttpd`.

```bash
# vim /etc/config/uhttpd
```

Em seguida, comentamos as linhas que contêm `list listen_http *` e adicionamos a linha `list listen_http 127.0.0.1:80` . A seguir temos as primeiras linhas do arquivo de configuração após a edição.

```
# Server configuration
config uhttpd main

	# HTTP listen addresses, multiple allowed
	# list listen_http	0.0.0.0:80 # esta linha deve estar comentada
	# list listen_http	[::]:80 # esta linha deve estar comentada

	# HTTPS listen addresses, multiple allowed
	# list listen_https	0.0.0.0:443 # esta linha deve estar comentada
	# list listen_https	[::]:443  # esta linha deve estar comentada

    # linha adicionada
    list listen_http        127.0.0.1:80
	
    ...
```

Salve o arquivo e reinicie o serviço uHTTPd usando o comando:

```bash
# /etc/init.d/uhttpd restart
```


Com o comando `netstat` vemos que agora nosso servidor web escuta em um novo endereço:

```
root@openwrt:~# netstat -na | grep :80
tcp        0      0 127.0.0.1:80            0.0.0.0:*               LISTEN   
```

O uso do endereço `127.0.0.1` tem objetivo de restringir o acesso a interface web para host remotos usando a interface de loopback, que é uma interface de rede virtual que é reservada para a comunicação interna no host.

Depois de reiniciar o servidor, a interface web do LuCI não esta acessível através do IP usual `192.168.1.1`, agora o servidor web escuta por novas conexões usando o endereço `127.0.0.1:80` e só podemos alcançá-la por meio de um túnel ssh.

Para criar o túnel, execute o seguinte comando no terminal:

veja: [127.0.0.1 vs 0.0.0.0](https://stackoverflow.com/questions/20778771/what-is-the-difference-between-0-0-0-0-127-0-0-1-and-localhost)

```bash
# ssh -L 127.0.0.1:8080:127.0.0.1:80 root@192.168.1.1
```

veja:
	[manual ssh -L](https://man.archlinux.org/man/ssh.1#L~4) 
	[Encaminhamento de portas](https://wiki.archlinux.org/title/OpenSSH#Forwarding_other_ports)

Para evitar sempre digitar todo o comando que cria o túnel ssh adicione  ao arquivo `~/.ssh/config` o seguite:

```
Host luci-tunnel
	Hostname openwrt.lan
	Port 22
	User root
	LocalForward 127.0.0.1:8080 127.0.0.1:80
```

Então o tunel ssh pode ser criado com o seguinte comando:

```ssh
# ssh luci-tunnel
```

O endereço local `127.0.0.1:8080` da máquina cliente é ligado através do túnel ssh ao endereço `127.0.0.1:80` do openwrt, onde o servidor web uHTTPd está aguardando solicitações. Agora é possível abrir o endereço [http://127.0.0.1:8080](http://127.0.0.1) no navegador e todo a comunicação HTTP com o servidor web é encapsulada no túnel SSH. Com isso todo o tráfico HTTP tem o mesmo nível de encriptação de uma sessão SSH. Enquanto a sessão SSH estiver aberta, será possível acessar a interface web usando um cliente HTTP. No terminal a combinação de teclas `ctrl+c` encerra a sessão SSH e a interface web do LuCI fica indisponível.

Na minha opinião essa configuração não é mais complexa do que instalar o pacote luci-ssl e depois gerar um certificado TLS (autoassinado), e é a configuração ideal para dispositivos com pouca memória. 

## Segurança adicional

Para minimizar os riscos de acesso não autorizado através da interface web, ative o servidor web via ssh somente quando necessário.


```
/etc/init.d/uhttpd disable
/etc/init.d/uhttpd stop
```


## uci comandos

O [uci](https://openwrt.org/docs/guide-user/base-system/uci) pode ajustar a configuração do uhttpd sem usar um editor de texto, no terminal digite as linhas a seguir:

```bash
# uci -q delete uhttpd.main.listen_http
# uci add_list uhttpd.main.listen_http="127.0.0.1:80"
# uci add_list uhttpd.main.listen_http="[::1]:80"
# uci -q delete uhttpd.main.listen_https
# uci add_list uhttpd.main.listen_https="127.0.0.1:443"
# uci add_list uhttpd.main.listen_https="[::1]:443"
# uci commit uhttpd
# /etc/init.d/uhttpd restart

```

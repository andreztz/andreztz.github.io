# Como controlar uma instancia do MPV via socket usando o Python


O [MPV](https://mpv.io/) é um player de mídia livre e de código aberto que suporta uma ampla variedade de formatos de arquivo e codecs. Ele tem muitos recursos avançados e é altamente configurável, mas às vezes pode ser útil controlá-lo programaticamente. 

Felizmente, o MPV possui uma interface de soquete que permite que outros processos controlem sua execução. Isso significa que é possível enviar enviar comandos para o MPV usando Python ou qualquer outra linguagem que suporte soquete.


## Iniciando uma instancia do MPV 

>> --input-ipc-server=<filename>
>>
>>    Enable the IPC support and create the listening socket at the given path.
>>
>>    On Linux and Unix, the given path is a regular filesystem path. On Windows, named pipes are used, so the path refers to the pipe namespace (\\.\pipe\<name>). If the \\.\pipe\ prefix is missing, mpv will add it automatically before creating the pipe, so --input-ipc-server=/tmp/mpv-socket and --input-ipc-server=\\.\pipe\tmp\mpv-socket are equivalent for IPC on Windows.  

Ao executar o `mpv` no linux por padrão um soquete é iniciado em `/tmp/mpvsocket`, no entanto, é possível definir um exclusivo com a opção `--input-ipc-server=<filename>`. 


```bash
$ mpv --player-operation-mode=pseudo-gui --input-ipc-server=/tmp/my_mpvsocket
```

## Configurando o soquete do tipo Unix

Para enviar comandos ao MPV, é necessário estabelecer uma conexão com o soquete que o MPV está ouvindo. Para isso é necessário criar um objeto [socket UNIX](https://en.wikipedia.org/wiki/Unix_domain_socket) usando a biblioteca `socket` do Python e conectá-lo ao caminho especificado na opção ``--input-ipc-server=`. 


```python
import socket

SOCKET_PATH = '/tmp/my_mpvsocket'

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect(SOCKET_PATH)

```

## Enviando comandos para o mpv 

Com a conexão foi estabelecida, é possível enviar comandos utilizando o método `sendall()` do objeto `socket`. Os comandos devem ser enviados no formato de bytes, codificados como UTF-8. Veja um exemplo:


```python
import socket

# Define o caminho do arquivo de socket
SOCKET_PATH = '/tmp/my_mpvsocket'

def enviar_comando_mpv(command):
    # estabelece a conexão com a interface de soquete do MPV
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(SOCKET_PATH)
        # Envia um comando 
        s.sendall(bytes(command, encoding='utf-8'))
        response = s.recv(1024)
        # retorna as resposta decodificada para string UTF-8
        return response.decode()

# carregar um arquivo de mídia, todos os comandos devem 
# terminar com o caractere `\n` para indicar o fim do comando
comando = "loadfile caminho/do/arquivo\n"
resposta = enviar_comando_mpv(comando)
print(resposta)

# pausar a reprodução
comando = "cycle pause\n"
resposta = enviar_comando_mpv(comando)
print(resposta)

# reproduzir o próximo arquivo na lista de reprodução
comando = "playlist-next\n"
resposta = enviar_comando_mpv(comando)
print(resposta)

```

**Alguns dos comandos disponíveis são**:

- `loadfile`: carrega um arquivo de mídia.
- `playlist-clear`: limpa a lista de reprodução.
- `playlist-add`: adiciona um arquivo à lista de reprodução.
- `playlist-remove`: remove um arquivo da lista de reprodução.
- `playlist-move`: move um arquivo dentro da lista de reprodução.
- `playlist-next`: reproduz o próximo arquivo da lista de reprodução.
- `playlist-prev`: reproduz o arquivo anterior da lista de reprodução.
- `seek`: move a reprodução para um determinado tempo.
- `pause`: pausa ou despausa a reprodução.
- `stop`: para a reprodução.
- `quit`: fecha o mpv.


Todos os comandos disponíveis estão [listados na documentação do MPV](https://mpv.io/manual/stable/#list-of-input-commands). 

A sintaxe para enviar comandos é  `<comando> [arg1 arg2]\n`, onde `comando` é o nome do comando, `arg1 arg2` são os argumentos do comando separados por espaços. É altamente recomendável consultar a documentação para obter informações detalhadas sobre todos os comandos disponíveis e sua sintaxe exata.

## Bibliotecas Python para controlar o MPV

A interface de soquete é uma maneira poderosa e flexível de controlar o MPV. Mas, para simplificar o controle por meio do Python e evitar erros de baixo nível, existem várias bibliotecas que abstraem os detalhes de baixo nível, simplificando a interação com MPV. Aqui estão alguns exemplos:

- **python-mpv-jsonipc**: uma biblioteca Python que oferece uma interface de alto nível para interagir com o MPV usando JSON IPC. Isso abstrai muitos dos detalhes de baixo nível do soquete Unix do MPV e oferece uma maneira mais fácil de enviar comandos e receber respostas do MPV.
- **MPV Python Binding**: uma biblioteca Python que oferece uma interface de alto nível semelhante à biblioteca python-mpv-jsonipc, mas usa a API de binding do MPV.
- **Python-mpv**: outra biblioteca Python que oferece uma interface de alto nível para interagir com o MPV, mas usa a API de soquete Unix.

É importante observar também que o mpv oferece suporte a scripts [Lua e JavaScript](https://github.com/mpv-player/mpv/wiki/User-Scripts) que podem ser usados para realizar tarefas complexas, como personalização de teclas de atalho, modificação de legendas e muito mais. 

Com isso em mente, é possível explorar as possibilidades de integração entre o MPV e Python para criar aplicativos poderosos que controlam a reprodução de mídia de maneira sofisticada e personalizada.


[MPV - Manual de referência](https://mpv.io/manual/)

[Python - socket](https://docs.python.org/3/library/socket.html#socket-families)

[IPC - Inter Process Communication](https://en.wikipedia.org/wiki/Inter-process_communication)

[Unix Domain Socket](https://en.wikipedia.org/wiki/Unix_domain_socket)


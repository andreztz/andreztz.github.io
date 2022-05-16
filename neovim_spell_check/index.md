# Corretor ortográfico no Neovim

# Corretor ortográfico no neovim 


O neovim usa o formato de arquivo `.spl` para armazenar palavras de uma determinada linguagem, a quais são usadas para fazer a verificação ortográfica. O arquivo `.spl` é um arquivo binário, esse formato proporciona o rápido carregamento da lista de palavras ao mesmo tempo que a mantém pequena.

O arquivo `.spl` pode ser criado a partir de arquivos myspell `.aff` e `.dic` usados pelo verificador ortográfico [VERO](https://pt-br.libreoffice.org/projetos/vero/#baixarvero) sigla que significa **VER**ificador **O**rtografico do LibreOffice.


### [Gerar um arquivo spell](https://neovim.io/doc/user/spell.html#spell-mkspell) 

Para gerar o arquivo `.spl` português do Brasil siga os passos a seguir: 


```bash
$ mkdir /tmp/vero && cd /tmp/vero
$ wget https://pt-br.libreoffice.org/assets/Uploads/PT-BR-Documents/VERO/VeroptBR3215AOC.oxt
$ file VeroptBR3215AOC.oxt
VeroptBR3215AOC.oxt: Zip archive data, at least v2.0 to extract, compression method=deflate
$ unzip VeroptBR3215AOC.oxt
```

Abra o vim no diretório corrente e execute o comando `:mkspell pt pt_BR` para gerar o `.spl`


```bash
:mkspell pt pt_BR
# ... Saída suprimida
Reading dictionary file pt_BR.dic...
Compressed case-folded of 16207519 nodes; 290324 (1%) remaining             
Compressed keep-case of 189406 nodes; 10459 (5%) remaining                  
# ... Saída suprimida
Compressed keep-case of 596998 nodes; 596998 (100%) remaining
Compressing word tree...
Compressed case-folded of 55323495 nodes; 47773995 (86%) remaining
Compressed keep-case of 746484 nodes; 601437 (80%) remaining
Writing spell file pt.utf-8.spl...
Done!
```


A saída é um arquivo `pt.utf-8.spl`, mova-o para `~/.local/share/nvim/spell/`


```bash
$ mv /tmp/vero/pt.utf-8.spl ~/.local/share/nvim/spell

```

Obs.: De acordo com a documentação, o neovim busca por spellfiles no [runtimepath](https://neovim.io/doc/user/spell.html#spell-load) no diretório `spell`. 



### Uso 

A medida que o corretor ortográfico detecta a palavra incorreta, essa é marcada com um sublinhado. Para corrigi-la, posicione o cursor sob a mesma, no modo Visual pressione `z + =`. Um menu irá mostrar as palavras sugeridas pelo corretor, então é só escolher a correta.  

No modo de inserção, com o cursor posicionado no fim da palavra com erro, pressione `ctrl + x + s` para exibir a caixa de sugestões, funciona como o autocompletar de palavras usando o `ctrl + p`. 


- Ativar o corretor ortográfico:

    ```vim
    :setlocal spell spelllang=pt_br,en
    ```

    Obs.: É possivel ativar mais de uma linguagem 


- Carregar um arquivo `.spl` e ativá-lo:

    ```vim
    : setlocal spell spellfile="/usr/share/vim/vimfiles/spell/pt.utf-8.spl" spelllang=pt_br 
    ```

- Para desativar o corretor:

    ```vim
    :set nospell
    ```

### Comandos do corretor ortográfico no modo visual


|Comando    |Ação 
|-----------|------
|]s         |busca a próxima palavra
|[s         |busca a palavra anterior
|z=         |mostra a lista de sugestões para a palavra
|zg         |adiciona a palavra sob o cursor no dicionário, assim ela não será mais marcada como errada
|zug        |desfaz a última palavra adicionada
|zw         |remove a palavra sob o cursor do dicionário, assim ela será marcada como errada
|zuw        |desfaz a última palavra removida


### Comandos do corretor ortográfico no modo inserção 


|Comando     |Ação 
|------------|----
|ctrl + x + s| Exibir a caixa de sugestões   
|ctrl + n    |Avançar para a próxima sugestão   
|ctrl + p    |Voltar para a sugestão anterior   



### Ativar o corretor ortográfico baseado no tipo de arquivo

```vim
vim.cmd [[ autocmd BufRead, BufNewFile *.md setlocal spell spelllang=pt_br]]
```


### Ativar o corretor ortográfico sob demanda 


```vim 
nnoremap <silent> <F3> :set spell!<CR>
inoremap <silent> <F3><C-O>:set spell!<CR> 
```


### Configuração global (opcional)

No arquivo `init.vim`

```vim
"spell languages
set spelllang=pt_br
```

No arquivo `init.lua`

```lua
vim.o.spelllang="pt_br"
```


### [Outras linguagens](http://ftp.vim.org/vim/runtime/spell/)

No web site do vim.org existe um [diretório](http://ftp.vim.org/vim/runtime/spell/) com as linguagens usadas pelo vim. Então simplesmente escolha uma, baixe no diretório `~/.local/share/nvim/spell` e ative o corretor ortográfico. 

[Nvim documentation: spell](https://neovim.io/doc/user/spell.html)


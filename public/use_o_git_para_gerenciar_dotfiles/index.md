# Use o git para gerenciar dotfiles


# Use o Git para gerenciar dotfiles.

A técnica de versionamento de [dotfiles](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory) consiste em criar um repositório Git do tipo [bare](https://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/) dentro de $HOME, que, ao contrário de um repositório Git padrão, não possui um diretório de trabalho associado. Sendo assim, é necessário definir explicitamente o que o repositório bare deve rastrear. Por fim, é necessário um alias para interagir com esse repositório de forma exclusiva.


**Vantagens**:

- Não há necessidade de usar ferramentas externas
- Não há uso de links simbólicos
- Os arquivos são rastreados pelo Git
- É possível usar branches diferentes para computadores diferentes
- É possível replicar a configuração facilmente em uma nova instalação


## Configuração inicial

Para iniciar a configuração do seu repositório bare, execute os seguintes comandos no terminal:


1. Cria o repositório ~/.dotfiles 
```python
git init --bare $HOME/.dotfiles
``` 
2. Define o alias `dotfiles`
```python
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```
3. Configura o Git para ignorar a $HOME inteira 
```python
dotfiles config --local status.showUntrackedFiles no
```

4. Adiciona o alias no `~/.bashrc`

```
echo "alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.bashrc
```

Depois de executar a configuração inicial, qualquer arquivo dentro da pasta `$HOME` pode ser versionado através do alias `dotfiles` com as opções normais do comando `git`, conforme mostrado abaixo:

```python
dotfiles status
dotfiles add .vimrc
dotfiles commit -m "Add vimrc"
dotfiles add .bashrc
dotfiles commit -m "Add bashrc"
dotfiles push
```

## Configurando repositório remoto

Para configurar o repositório remoto, primeiro crie um repositório no seu Gitlab ou GitHub e siga os passos a seguir, substituindo o `<username>` pelo seu usuário no remoto.

1. Adicione o remoto

```python
dotfiles remote add origin git@gitlab.com:<username>/dotfiles.git
dotfiles remote -v 
```

2. Envie os arquivos para o remoto

```
dotfiles push -uf origin main
```


## Instalar os dotfiles em um novo sistema


Primeiro, verifique se o alias foi adicionado ao seu `.bashrc` ou `.zshrc`. Certifique-se também de adicionar a pasta onde você irá clonar o repositório no arquivo `.gitignore`, para evitar problemas de recursão.


```python
echo ".dotfiles" >> .gitignore
```

Agora, clone seus dotfiles em um repositório **bare** em uma pasta oculta do seu $HOME:

```python
git clone --bare <git-repo-url> $HOME/.dotfiles
```

Defina o alias no escopo do shell atual:

```python
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

Faça o checkout do conteúdo real do repositório vazio para o seu $HOME:

```python
dotfiles checkout
```

**Nota:** O passo anterior pode falhar e retornar uma mensagem de erro:

```ruby
error: The following untracked working tree files would be overwritten by checkout:
    .bashrc
    .gitignore
Please move or remove them before you can switch branches.
Aborting
```

>> Isso ocorre porque sua pasta `$HOME` pode conter alguns arquivos de configurações locais, que serão substituídos pelos do Git. A solução é simples: faça backup dos arquivos se você se importa com eles, ou remova-os. Segue abaixo um possível atalho para mover todos os arquivos incorretos para uma pasta. 

```python
mkdir -p .dotfiles-backup && \
dotfiles checkout 2>&1 | grep -e "\s+\." | awk {'print $1'} | \
xargs -I{} mv {} .dotfiles-backup/{}
```

**Nota:** Se você teve o problema mencionado anteriormente, após mover os arquivos, execute novamente o `dotfiles checkout`.


Agora defina o valor de `showUntrackedFiles` como `no` para este repositório:

```bash
dotfiles config --local status.showUntrackedFiles no
```

Pronto, a partir de agora você pode usar o alias definido anteriormente para gerenciar seus dotfiles na sua nova maquina:


```python
dotfiles status
dotfiles add .vimrc
dotfiles commit -m "Add vimrc"
dotfiles add .bashrc
dotfiles commit -m "Add bashrc"
dotfiles push
```


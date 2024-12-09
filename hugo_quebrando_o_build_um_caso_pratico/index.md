# Hugo Quebrando o Build: Um Caso Prático


## Hugo Quebrando o Build: Um Caso Prático

Nos últimos meses, mantive meu sistema operacional **Arch Linux** atualizado diariamente. Como é baseado no modelo **rolling-release**, o Arch Linux oferece as versões mais recentes e estáveis dos pacotes de software. Embora isso permita acesso rápido a novas funcionalidades, também traz consigo alguns riscos.

Hoje, ao realizar uma simples alteração em uma imagem do meu blog, construído com o **Hugo**—um gerador de sites estáticos escrito em Go—encontrei um problema inesperado. O Hugo não conseguiu processar as mudanças, exibindo erros que interromperam o build.

**Mensagem de Erro:**

```bash
19:36:54 with ztz in ~/Workspace/andreztz.github.io on  main …
➜ make
rm -rf plublic/*
hugo
WARN  DEPRECATED: Kind "taxonomyterm" used in outputs configuration is deprecated, use "taxonomy" instead.
Start building sites …
hugo v0.139.3+extended linux/amd64 BuildDate=unknown

ERROR deprecated: .Site.Author was deprecated in Hugo v0.124.0 and will be removed in Hugo 0.140.0. Implement taxonomy 'author' or use .Site.Params.Author instead.
ERROR deprecated: .Site.IsMultiLingual was deprecated in Hugo v0.124.0 and will be removed in Hugo 0.140.0. Use hugo.IsMultilingual instead.
Total in 1046 ms
Error: error building site: logged 2 error(s)
make: *** [makefile:10: build] Error 1
```

O problema não foi causado por um bug do Hugo, mas pela incompatibilidade entre o ambiente de desenvolvimento (rolling-release) e as mudanças recentes no software. Isso resultou em **breaking changes**.


## O Que São **Breaking Changes**?

> No contexto de desenvolvimento de software, breaking changes são mudanças em sistemas, APIs ou bibliotecas que quebram a compatibilidade com versões anteriores. Isso exige que o código dependente seja ajustado para funcionar corretamente.
> 
> Essas alterações são inevitáveis em projetos de software em constante evolução, mas podem gerar problemas se o ambiente de desenvolvimento ou produção não acompanhar as atualizações. 

No meu caso, enquanto o Hugo foi automaticamente atualizado no Arch Linux, o código do meu blog permaneceu inalterado, criando a incompatibilidade.


## Soluções para o Problema

Identifiquei duas abordagens possíveis para resolver o problema:

1. **Atualizar o código do blog:** Ajustar arquivos de configuração, temas e scripts para se adequar à nova versão do Hugo.
2. **Fazer o downgrade do Hugo:** Reverter para uma versão anterior do Hugo, compatível com o ambiente atual.

Optei pelo **downgrade do Hugo**, pois foi a solução mais rápida e prática para o meu caso.

---

## Como Fazer o Downgrade do Hugo no Arch Linux

> ⚠️ *Atenção*: O downgrade pode exigir alterações nas dependências associadas ao pacote. Confira a [documentação oficial](https://wiki.archlinux.org/title/Downgrading_packages_(Portugu%C3%AAs)) para detalhes.

1. **Verificar dependências e conflitos**
   
   Use o comando abaixo para identificar as dependências do Hugo:

   ```bash
   pactree -r hugo
   ```

2. **Listar versões disponíveis no cache**

   Confira as versões armazenadas localmente:

   ```bash
   ls /var/cache/pacman/pkg/hugo*
   ```

3. **Reinstalar a versão desejada**

   Reinstale a versão do Hugo diretamente do cache:

   ```bash
   sudo pacman -U /var/cache/pacman/pkg/hugo-<versao>.pkg.tar.zst
   ```

4. **Bloquear atualizações futuras**

   Adicione a seguinte linha no arquivo `/etc/pacman.conf` para evitar atualizações automáticas do pacote:

   ```bash
   IgnorePkg = hugo
   ```

   Agora, ao executar `sudo pacman -Syu`, um aviso como este será exibido:

   ```bash
   warning: hugo: ignoring package upgrade (0.135.0-1 => 0.139.3-1)
   ```


## Ajustando o Workflow de deploy no GitHub Actions

Além de corrigir o ambiente local, foi necessário ajustar o deploy no **GitHub Actions**, fixando a versão compatível do Hugo na etapa de configuração:

```yaml
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v3
  with:
    hugo-version: '0.135.0'  # Versão fixada, evite o uso de 'latest'
    extended: true
```

Fixar a versão evita surpresas com futuras atualizações que possam introduzir 
novas **breaking changes**.


## Lições Aprendidas e Boas Práticas

**Breaking changes** são comuns em ambientes modernos, especialmente com ferramentas que evoluem rapidamente, como o Hugo. Para mitigar seus impactos, considere adotar boas práticas, como:

- Controlar atualizações automáticas.
- Fixar versões específicas para desenvolvimento e produção.
- Manter-se informado sobre mudanças nas ferramentas utilizadas.

Outra abordagem interessante é o uso de **containers**. Eles permitem criar ambientes isolados e controlados, garantindo:

- Reprodutibilidade.
- Isolamento.
- Facilidade no rollback.


Essa experiência reforça a importância de planejar e gerenciar cuidadosamente o ambiente de desenvolvimento para minimizar impactos de atualizações inesperadas.


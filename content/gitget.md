title: Como baixar subdiretórios em projetos do GitHub
slug: como-baixar-diretorios-do-GitHub
date: 2017-06-22
modified: 2019-09-16
category: github
tags: git, github, svn, subversion, python, script
Authors: André P. Santos



##### Segue o script:

```python
#!/usr/bin/env python
"""
Download a specific folder from a github repo:
    gitget.py https://github.com/divs1210/kilvish/tree/master/examples/bricksnball
"""
__author__ = 'Divyansh Prakash'

import sys
import subprocess

if __name__ == '__main__':
  if len(sys.argv) > 1:
    github_src = sys.argv[1]

    try:
      head, branch_etc = github_src.split('/tree/')
      folder_url = '/'.join(branch_etc.split('/')[1:])
    except:
      print('err:\tnot a valid folder url!')
    else:
      print('fetching...')
      subprocess.call(['svn', 'checkout', '/'.join([head, 'trunk', folder_url])])
  else:
    print('use:\tgitget.py https://github.com/user/project/tree/branch-name/folder\n')
```

Baseado no script acima que encontrei no [gist.githgub.com/divs1210](https://gist.github.com/divs1210/973493941a82b28f0d4a), criei um projeto no github e publiquei no pypi com o nome de gitget. Para instalar é só executar um `pip install gitget`. A syntax do gitget é simples `giget url_do_diretorio_no_git_hub`.

Ex.:

```py
  $ gitget https://github.com/boppreh/keyboard/tree/master/examples
```
No exemplo acima o gitget baixa o diretório `examples/` do projeto `keyboard`.


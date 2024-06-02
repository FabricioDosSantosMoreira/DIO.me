<h1>
    <a href="https://git-scm.com/">
    <img align="center" width="40px" src="./utils/git.svg"></a>
    <strong>Comandos Git</strong>
</h1>


## 💻 Principais Comandos do Git:
<table>
  <thead>
    <tr align="left">
      <th>💻 Comando</th>
      <th>📚 Descrição</th>
      <th>📋 Exemplo</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>Git Clone</td>
      <td>É utilizado para adquirir uma cópia local <br> de um repositório Git remoto.</td>
      <td align="left"> <code>$ git clone https://github.com/FabricioDosSantosMoreira/DIO.me.git</code></td>
    </tr>
    <tr>
      <td>Git Commit</td>
      <td>É utilizado para salvar as alterações <br> feitas nos arquivos do repositório.</td>
      <td align="left"> <code>$ git commit -m "UPDATE: DIO.me"</code></td>
    </tr>
    <tr>
      <td>Git Push</td>
      <td>É utilizado para enviar os commits <br> locais para um repositório remoto.</td>
      <td align="left"> <code>$ git push origin main</code></td>
    </tr>
    <tr>
      <td>Git Pull</td>
      <td>É utilizado para obter e integrar as <br> alterações de um repositório remoto <br> para o repositório local.</td>
      <td align="left"> <code>$ git pull origin https://github.com/FabricioDosSantosMoreira/DIO.me.git</code></td>
    </tr>
  </tbody>
  <tfoot></tfoot>
</table>


## ⚙ Comandos do Git:
<table>
  <thead>
    <tr align="left">
      <th>💻 Comando</th>
      <th>📚 Descrição</th>
      <th>📋 Exemplo</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>git init</td>
      <td>Inicializa um repositório Git.</td>
      <td align="left"> <code>$ git init</code></td>
    </tr>
    <tr>
      <td>git status</td>
      <td>Visualiza o status do repositório Git.</td>
      <td align="left"> <code>$ git status</code></td>
    </tr>
    <tr>
      <td>git config [ESCOPO] [CONFIGURAÇÃO]</td>
      <td>Visualiza ou define uma configuração do Git.</td>
      <td align="left"> <code>$ git config --global user.email</code><br><code>$ git config --global user.name</code><br><code>$ git config --global --list</code></td>
    </tr>
    <tr>
      <td>git log</td>
      <td>Visualiza as informações do commit.</td>
      <td align="left"> <code>$ git log</code></td>
    </tr>
    <tr>
      <td>git reflog</td>
      <td>Visualiza um log mais robusto.</td>
      <td align="left"> <code>$ git reflog</code></td>
    </tr>
    <tr>
      <td>git add [ARQUIVO]</td>
      <td>Adiciona um arquivo ao Git.</td>
      <td align="left"> <code>$ git add .</code><br><code>$ git add README.md</code></td>
    </tr>
    <tr>
      <td>git commit -m"[MENSAGEM]"</td>
      <td>Comita as mudanças com uma mensagem.</td>
      <td align="left"> <code>$ git commit -m "MENSAGEM"</code></td>
    </tr>
    <tr>
      <td>git commit --amend -m"[MENSAGEM]"</td>
      <td>Muda a mensagem de commit.</td>
      <td align="left"> <code>$ git commit --amend -m "MENSAGEM"</code></td>
    </tr>
    <tr>
      <td>git restore [TYPE] [ARQUIVO]</td>
      <td>Recupera um arquivo.</td>
      <td align="left"> <code>$ git restore --source exemplo.txt</code><br><code>$ git restore --staged exemplo.txt</code><br><code>$ git restore --worktree exemplo.txt</code></td>
    </tr>
    <tr>
      <td>git reset [TYPE] [HASH/ARQUIVO]</td>
      <td>Reseta o repositório.</td>
      <td align="left"> <code>$ git reset --mixed HEAD~1</code><br><code>$ git reset --soft HEAD~1</code><br><code>$ git reset --hard HEAD~1</code></td>
    </tr>
    <tr>
      <td>git config --global init.defaultbranch main</td>
      <td>Define a branch padrão.</td>
      <td align="left"> <code>$ git config --global init.defaultbranch main</code></td>
    </tr>
    <tr>
      <td>git config [ESCOPO] credential.helper [VALOR]</td>
      <td>Configura o armazenamento de credenciais.</td>
      <td align="left"> <code>$ git config --global credential.helper store</code><br><code>$ git config --global credential.helper cache</code><br><code>$ git config --global credential.helper manager</code></td>
    </tr>
    <tr>
      <td>git remote add origin [LINK]</td>
      <td>Conecta um repositório local com um remoto.</td>
      <td align="left"> <code>$ git remote add origin https://github.com/FabricioDosSantosMoreira/DIO.me</code></td>
    </tr>
    <tr>
      <td>git remote add upstream [LINK]</td>
      <td>Adiciona um remote upstream para manter o repositório local atualizado.</td>
      <td align="left"> <code>$ git remote add upstream https://github.com/FabricioDosSantosMoreira/DIO.me</code></td>
    </tr>
  </tbody>
  <tfoot></tfoot>
</table>


## 🔍 Comandos de Facilidade do Git:
<table>
  <thead>
    <tr align="left">
      <th>💻 Comando</th>
      <th>📚 Descrição</th>
      <th>📋 Exemplo</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>clear</td>
      <td>Limpa o terminal.</td>
      <td align="left"> <code>$ clear</code></td>
    </tr>
    <tr>
      <td>head [NOME_DO_ARQUIVO]</td>
      <td>Exibe as primeiras linhas de um arquivo.</td>
      <td align="left"> <code>$ head arquivo.txt</code></td>
    </tr>
    <tr>
      <td>pwd</td>
      <td>Mostra o caminho completo do diretório atual.</td>
      <td align="left"> <code>$ pwd</code></td>
    </tr>
    <tr>
      <td>man [COMANDO]</td>
      <td>Exibe o manual do usuário para um comando específico.</td>
      <td align="left"> <code>$ man ls</code></td>
    </tr>
    <tr>
      <td>cd [CAMINHO_DO_DIRETÓRIO]</td>
      <td>Muda para o diretório especificado.</td>
      <td align="left"> <code>$ cd Documents</code></td>
    </tr>
    <tr>
      <td>cat [NOME_DO_ARQUIVO]</td>
      <td>Exibe o conteúdo de um arquivo.</td>
      <td align="left"> <code>$ cat texto.txt</code></td>
    </tr>
    <tr>
      <td>ls</td>
      <td>Lista os arquivos e diretórios no diretório atual.</td>
      <td align="left"> <code>$ ls</code></td>
    </tr>
    <tr>
      <td>ls -l [ARQUIVO/DIRETÓRIO]</td>
      <td>Exibe informações detalhadas sobre um arquivo ou diretório.</td>
      <td align="left"> <code>$ ls -l arquivo.txt</code></td>
    </tr>
    <tr>
      <td>mkdir [NOME_DO_DIRETÓRIO]</td>
      <td>Cria um novo diretório com o nome especificado.</td>
      <td align="left"> <code>$ mkdir novo_diretorio</code></td>
    </tr>
    <tr>
      <td>mv [ORIGEM] [DESTINO]</td>
      <td>Movimenta arquivos ou diretórios.</td>
      <td align="left"> <code>$ mv arquivo.txt path_pasta_destino/</code></td>
    </tr>
    <tr>
      <td>cp [ORIGEM] [DESTINO]</td>
      <td>Copia arquivos ou diretórios.</td>
      <td align="left"> <code>$ cp arquivo.txt -path_pasta_destino/</code></td>
    </tr>
    <tr>
      <td>rm [ARQUIVO]</td>
      <td>Remove (apaga) um arquivo.</td>
      <td align="left"> <code>$ rm arquivo.txt</code></td>
    </tr>
    <tr>
      <td>rm -r [DIRETÓRIO]</td>
      <td>Remove (apaga) um diretório e seu conteúdo.</td>
      <td align="left"> <code>$ rm -r pasta</code></td>
    </tr>
    <tr>
      <td>rm -rf [DIRETÓRIO]</td>
      <td>Remove (apaga) a força um diretório e seu conteúdo.</td>
      <td align="left"> <code>$ rm -rf pasta</code></td>
    </tr>
    <tr>
      <td>touch [NOME_DO_ARQUIVO]</td>
      <td>Cria um novo arquivo vazio.</td>
      <td align="left"> <code>$ touch novo_arquivo.txt</code></td>
    </tr>
    <tr>
      <td>grep [PADRÃO] [ARQUIVO]</td>
      <td>Procura por um padrão em um arquivo.</td>
      <td align="left"> <code>$ grep "palavra" arquivo.txt</code></td>
    </tr>
    <tr>
      <td>history</td>
      <td>Exibe o histórico de comandos usados no terminal.</td>
      <td align="left"> <code>$ history</code></td>
    </tr>
  </tbody>
  <tfoot></tfoot>
</table>


## ⚙ Outros Comandos Úteis do Git:
<table>
  <thead>
    <tr align="left">
      <th>💻 Comando</th>
      <th>📚 Descrição</th>
      <th>📋 Exemplo</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>git checkout -b [NOME_DA_BRANCH]</td>
      <td>É utilizado para criar uma nova branch e mudar para ela.</td>
      <td align="left"> <code>$ git checkout -b teste</code></td>
    </tr>
    <tr>
      <td>git checkout [BRANCH] main</td>
      <td>É utilizado para mudar para uma branch específica a partir da branch principal (main).</td>
      <td align="left"> <code>$ git checkout main</code></td>
    </tr>
    <tr>
      <td>git checkout -v</td>
      <td>É utilizado para listar os últimos commits de cada branch.</td>
      <td align="left"> <code>$ git checkout -v</code></td>
    </tr>
    <tr>
      <td>git merge [BRANCH]</td>
      <td>É utilizado para mesclar uma branch específica com a branch atual.</td>
      <td align="left"> <code>$ git merge main</code></td>
    </tr>
    <tr>
      <td>git branch</td>
      <td>É utilizado para listar as branches no repositório atual.</td>
      <td align="left"> <code>$ git branch</code></td>
    </tr>
    <tr>
      <td>git branch -d [BRANCH]</td>
      <td>É utilizado para deletar uma branch específica.</td>
      <td align="left"> <code>$ git branch -d main</code></td>
    </tr>
    <tr>
      <td>git fetch origin main</td>
      <td>É utilizado para baixar as alterações do repositório remoto sem afetar o local.</td>
      <td align="left"> <code>$ git fetch origin main</code></td>
    </tr>
    <tr>
      <td>git diff main origin/main</td>
      <td>É utilizado para mostrar as diferenças entre as branches.</td>
      <td align="left"> <code>$ git diff main origin/main</code></td>
    </tr>
    <tr>
      <td>git merge origin/main</td>
      <td>É utilizado para mesclar as alterações da branch remota com a branch local.</td>
      <td align="left"> <code>$ git merge origin/main</code></td>
    </tr>
    <tr>
      <td>$ git stash <br> $ git stash list <br> $ git stash pop <br> $ git stash apply</td>
      <td>É utilizado para gerenciar o stash, que permite armazenar temporariamente mudanças que ainda não estão prontas para serem commitadas.</td>
      <td align="left"> <code>$ git stash</code> <br> <code>$ git stash list</code> <br> <code>$ git stash pop</code> <br> <code>$ git stash apply</code></td>
    </tr>
  </tbody>
  <tfoot></tfoot>
</table>

## 🔗 Fontes:
- <h2><a href="https://web.dio.me/home/"><img align="center" width="20px" src="./utils/dio.webp"></a><a href="https://web.dio.me/home"> Digital Inovation One (DIO)</a></h2>

- <h2><a href="https://github.com/"><img align="center" width="20px" src="./utils/github.svg"></a><a href="https://github.com/"> GitHub</a></h2>

- <h2><a href="https://git-scm.com/"><img align="center" width="20px" src="./utils/git.svg"></a><a href="https://git-scm.com/"> Git</a></h1>

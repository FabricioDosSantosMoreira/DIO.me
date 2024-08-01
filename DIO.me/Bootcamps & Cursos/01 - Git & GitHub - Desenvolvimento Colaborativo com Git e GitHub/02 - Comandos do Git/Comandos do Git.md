<h1>
    <a href="https://git-scm.com/">
      <img align="center" width="50px" src="./util/git.svg">
    </a>
    <strong> Comandos do Git</strong>
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
      <td>Git clone</td>
      <td>
        É utilizado para adquirir uma cópia local <br> de um repositório Git remoto.
      </td>
      <td align="left"> 
        <code>$ git clone https://github.com/FabricioDosSantosMoreira/DIO.me.git</code>
      </td>
    </tr>
    <tr>
      <td>Git commit</td>
      <td>
        É utilizado para salvar as alterações <br> feitas nos arquivos do repositório.
      </td>
      <td align="left"> 
        <code>$ git commit -m "[UPDATE] - DIO.me"</code>
      </td>
    </tr>
    <tr>
      <td>Git push</td>
      <td>
        É utilizado para enviar os commits <br> locais para um repositório remoto.
      </td>
      <td align="left"> 
        <code>$ git push origin main</code>
      </td>
    </tr>
    <tr>
      <td>Git pull</td>
      <td>
        É utilizado para obter e integrar as <br> alterações de um repositório remoto <br> para o repositório local.
      </td>
      <td align="left"> 
        <code>$ git pull origin https://github.com/FabricioDosSantosMoreira/DIO.me.git</code>
      </td>
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
      <td>Inicializar um repositório Git</td>
      <td align="left"> 
        <code>$ git init</code>
      </td>
    </tr>
    <tr>
      <td>git status</td>
      <td>Visualizar o status do repositório Git</td>
      <td align="left"> 
        <code>$ git status</code>
      </td>
    </tr>
    <tr>
      <td>git config [ESCOPO] [CONFIGURAÇÃO]</td>
      <td>Visualizar ou definir uma configuração do Git</td>
      <td align="left"> 
        <code>$ git config --global user.email</code><br>
        <code>$ git config --global user.name</code><br>
        <code>$ git config --global --list</code>
      </td>
    </tr>
    <tr>
      <td>git log</td>
      <td>Visualizar as informações do commit</td>
      <td align="left"> 
        <code>$ git log</code>
      </td>
    </tr>
    <tr>
      <td>git reflog</td>
      <td>Visualizar um log mais robusto</td>
      <td align="left"> 
        <code>$ git reflog</code>
      </td>
    </tr>
    <tr>
      <td>git add [ARQUIVOS]</td>
      <td>Adicionar arquivos ao Git</td>
      <td align="left"> 
        <code>$ git add .</code><br>
        <code>$ git add README.md</code>
      </td>
    </tr>
    <tr>
      <td>git commit -m"[MENSAGEM]"</td>
      <td>Comitar as mudanças com uma mensagem</td>
      <td align="left"> 
        <code>$ git commit -m "update"</code>
      </td>
    </tr>
    <tr>
      <td>git commit --amend -m"[MENSAGEM]"</td>
      <td>Mudar a mensagem de commit</td>
      <td align="left"> 
        <code>$ git commit --amend -m "update"</code>
        </td>
    </tr>
    <tr>
      <td>git restore [TIPO] [ARQUIVO]</td>
      <td>Recuperar um arquivo</td>
      <td align="left"> 
        <code>$ git restore --source exemplo.txt</code><br>
        <code>$ git restore --staged exemplo.txt</code><br>
        <code>$ git restore --worktree exemplo.txt</code>
      </td>
    </tr>
    <tr>
      <td>git reset [TIPO] [HASH/ARQUIVO]</td>
      <td>Resetar o repositório</td>
      <td align="left"> 
        <code>$ git reset --mixed HEAD~1</code><br>
        <code>$ git reset --soft HEAD~1</code><br>
        <code>$ git reset --hard HEAD~1</code>
      </td>
    </tr>
    <tr>
      <td>git config --global init.defaultbranch main</td>
      <td>Definir a branch padrão</td>
      <td align="left"> 
        <code>$ git config --global init.defaultbranch main</code>
      </td>
    </tr>
    <tr>
      <td>git config [ESCOPO] credential.helper [VALOR]</td>
      <td>Configurar o armazenamento de credenciais</td>
      <td align="left"> 
        <code>$ git config --global credential.helper store</code><br>
        <code>$ git config --global credential.helper cache</code><br>
        <code>$ git config --global credential.helper manager</code>
      </td>
    </tr>
    <tr>
      <td>git remote add origin [LINK]</td>
      <td>Conectar um repositório local com um remoto</td>
      <td align="left"> 
        <code>$ git remote add origin https://github.com/FabricioDosSantosMoreira/DIO.me</code>
      </td>
    </tr>
    <tr>
      <td>git remote add upstream [LINK]</td>
      <td>Adicionar um remote upstream para manter o repositório local atualizado</td>
      <td align="left"> 
        <code>$ git remote add upstream https://github.com/FabricioDosSantosMoreira/DIO.me</code>
      </td>
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
      <td>
        <code>$ git checkout -b [BRANCH]</code>
      </td>
      <td>É utilizado para criar uma nova branch e mudar para ela</td>
      <td align="left"> 
        <code>$ git checkout -b teste</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git checkout [BRANCH] main</code>
      </td>
      <td>É utilizado para mudar para uma branch específica a partir da branch principal</td>
      <td align="left"> 
        <code>$ git checkout main</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git checkout -v</code>
      </td>
      <td>É utilizado para listar os últimos commits de cada branch</td>
      <td align="left"> 
        <code>$ git checkout -v</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git merge [BRANCH]</code>
      </td>
      <td>É utilizado para mesclar uma branch específica com a branch atual</td>
      <td align="left"> 
        <code>$ git merge main</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git branch</code>
      </td>
      <td>É utilizado para listar as branches no repositório atual</td>
      <td align="left"> 
        <code>$ git branch</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git branch -d [BRANCH]</code>
      </td>
      <td>É utilizado para deletar uma branch específica</td>
      <td align="left"> 
        <code>$ git branch -d main</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git fetch origin main</code>
      </td>
      <td>É utilizado para baixar as alterações do repositório remoto sem afetar o local</td>
      <td align="left"> 
        <code>$ git fetch origin main</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git diff main origin/main</code>
      </td>
      <td>É utilizado para mostrar as diferenças entre as branches</td>
      <td align="left"> 
        <code>$ git diff main origin/main</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git merge origin/main</code>
      </td>
      <td>É utilizado para mesclar as alterações da branch remota com a branch local</td>
      <td align="left"> 
        <code>$ git merge origin/main</code>
      </td>
    </tr>
    <tr>
      <td>
        <code>$ git stash</code> <br> 
        <code>$ git stash list</code> <br> 
        <code>$ git stash pop</code> <br> 
        <code>$ git stash apply</code></td>
      <td>
        É utilizado para gerenciar o stash, que permite armazenar temporariamente mudanças que ainda não estão prontas para serem commitadas
      </td>
      <td align="left"> 
        <code>$ git stash</code> <br> 
        <code>$ git stash list</code> <br> 
        <code>$ git stash pop</code> <br> 
        <code>$ git stash apply</code>
      </td>
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
      <td>Limpa o terminal</td>
      <td align="left"> 
        <code>$ clear</code>
      </td>
    </tr>
    <tr>
      <td>head [ARQUIVO]</td>
      <td>Exibe as primeiras linhas de um arquivo</td>
      <td align="left"> 
        <code>$ head meu_arquivo.txt</code>
      </td>
    </tr>
    <tr>
      <td>pwd</td>
      <td>Mostra o caminho completo do diretório atual</td>
      <td align="left"> 
        <code>$ pwd</code>
      </td>
    </tr>
    <tr>
      <td>man [COMANDO]</td>
      <td>Exibe o manual do usuário para um comando específico</td>
      <td align="left"> 
        <code>$ man ls</code>
      </td>
    </tr>
    <tr>
      <td>cd [DIRETÓRIO]</td>
      <td>Muda para o diretório especificado</td>
      <td align="left"> 
        <code>$ cd Documents</code>
      </td>
    </tr>
    <tr>
      <td>cat [ARQUIVO]</td>
      <td>Exibe o conteúdo de um arquivo</td>
      <td align="left"> 
        <code>$ cat meu_arquivo.txt</code>
      </td>
    </tr>
    <tr>
      <td>ls</td>
      <td>Lista os arquivos e diretórios no diretório atual</td>
      <td align="left"> 
        <code>$ ls</code>
      </td>
    </tr>
    <tr>
      <td>ls -l [ARQUIVO OU DIRETÓRIO]</td>
      <td>Exibe informações detalhadas sobre um arquivo ou diretório.</td>
      <td align="left"> 
        <code>$ ls -l meu_arquivo.txt</code>
      </td>
    </tr>
    <tr>
      <td>mkdir [DIRETÓRIO]</td>
      <td>Cria um novo diretório com o nome especificado.</td>
      <td align="left"> 
        <code>$ mkdir meu_diretorio</code>
        </td>
    </tr>
    <tr>
      <td>mv [ORIGEM] [DESTINO]</td>
      <td>Movimenta arquivos ou diretórios</td>
      <td align="left"> 
        <code>$ mv meu_arquivo.txt /pasta_destino/</code>
      </td>
    </tr>
    <tr>
      <td>cp [ORIGEM] [DESTINO]</td>
      <td>Copia arquivos ou diretórios</td>
      <td align="left"> 
        <code>$ cp meu_arquivo.txt /pasta_destino/</code>
      </td>
    </tr>
    <tr>
      <td>rm [ARQUIVO]</td>
      <td>Remove um arquivo</td>
      <td align="left"> 
        <code>$ rm meu_arquivo.txt</code>
      </td>
    </tr>
    <tr>
      <td>rm -r [DIRETÓRIO]</td>
      <td>Remove um diretório e seu conteúdo.</td>
      <td align="left"> 
        <code>$ rm -r meu_diretorio</code>
      </td>
    </tr>
    <tr>
      <td>rm -rf [DIRETÓRIO]</td>
      <td>Remove a força um diretório e seu conteúdo.</td>
      <td align="left"> 
        <code>$ rm -rf meu_diretorio</code>
      </td>
    </tr>
    <tr>
      <td>touch [ARQUIVO]</td>
      <td>Cria um novo arquivo vazio</td>
      <td align="left"> 
        <code>$ touch novo_arquivo.txt</code>
      </td>
    </tr>
    <tr>
      <td>grep [PADRÃO] [ARQUIVO]</td>
      <td>Procura por um padrão em um arquivo</td>
      <td align="left"> 
        <code>$ grep "palavra" meu_arquivo.txt</code>
      </td>
    </tr>
    <tr>
      <td>history</td>
      <td>Exibe o histórico de comandos usados no terminal</td>
      <td align="left"> 
        <code>$ history</code>
      </td>
    </tr>
  </tbody>
  <tfoot></tfoot>
</table>


## 🔗 Fontes:
- <h2>
    <a href="https://web.dio.me/home/"><img align="center" width="25px" src="./util/dio.webp"></a>
    <a href="https://web.dio.me/home"> Digital Inovation One (DIO)</a>
</h2>

- <h2>
    <a href="https://github.com/"><img align="center" width="25px" src="./util/github.svg"></a>
    <a href="https://github.com/"> GitHub</a>
</h2>

- <h2>
    <a href="https://git-scm.com/"><img align="center" width="25px" src="./util/git.svg"></a>
    <a href="https://git-scm.com/"> Git</a>
</h1>

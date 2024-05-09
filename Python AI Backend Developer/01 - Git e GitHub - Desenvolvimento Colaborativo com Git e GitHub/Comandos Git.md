<h1>
    <a href="https://git-scm.com/">
    <img align="center" width="40px" src="./utils/git.svg"></a>
    <strong>Comandos Git</strong>
</h1>


## 💻 Comandos Básicos do Git:

### 📋 Git Clone:
Clona um repositório Git existente para um novo diretório local. 
```bash 
$ git clone 
``` 

### 📋 Git Commit:
Grava alterações no repositório.
```bash
$ git commit 
```  

### 📋 Git Pull:
"Puxa" as alterações do repositório remoto para o local (busca e mescla).
```bash
$ git pull 
```  

### 📋 Git Push:
"Empurra" as alterações do repositório local para o remoto.
```bash
$ git push 
```  


## 💻 Comandos de Facilidade:

### 📋 Limpa o terminal:
```bash
$ clear
```  

### 📋 Exibe as primeiras linhas de um arquivo:
```bash
$ head [NOME_DO_ARQUIVO]
```  

### 📋 Mostra o caminho completo do diretório atual:
```bash
$ pwd
```  

### 📋 Exibe o manual do usuário para um comando específico:
```bash
$ -man [COMANDO]
```  

### 📋 Muda para o diretório especificado:
```bash
$ cd [CAMINHO_DO_DIRETÓRIO]
```  

### 📋 Exibe o conteúdo de um arquivo:
```bash
$ -cat [NOME_DO_ARQUIVO]
```  

### 📋 Lista os arquivos e diretórios no diretório atual:
```bash
$ -ls
```  

### 📋 Exibe informações detalhadas sobre um arquivo ou diretório:
```bash
$ -ls -l [ARQUIVO/DIRETÓRIO]
```  

### 📋 Cria um novo diretório com o nome especificado:
```bash
$ -mkdir [NOME_DO_DIRETÓRIO]
```  

### 📋 Move arquivos ou diretórios:
```bash
$ -mv [ORIGEM] [DESTINO]
```  

### 📋 Copia arquivos ou diretórios:
```bash
$ -cp [ORIGEM] [DESTINO]
```  

### 📋 Remove (apaga) um arquivo:
```bash
$ -rm [ARQUIVO]
```  

### 📋 Remove (apaga) um diretório e seu conteúdo:
```bash
$ -rm -r [DIRETÓRIO]
```

### 📋 Remove (apaga) a força um diretório e seu conteúdo:
```bash
$ -rm -rf [DIRETÓRIO]
```  

### 📋 Cria um novo arquivo vazio:
```bash
$ -touch [NOME_DO_ARQUIVO]
```  

### 📋 Procura por um padrão em um arquivo:
```bash
$ -grep [PADRÃO] [ARQUIVO]
```  

### 📋 Exibe o histórico de comandos usados no terminal:
```bash
$ -history
```  


## ⚙ Comandos do Git:

### 📋 Inicializar um repositório git:
```bash
$ git init
```  

### 📋 Visualizar o status do repositório git:
```bash
$ git status
```  

### 📋 Visualizar uma configuração:
```bash
$ git config [ESCOPO] [CONFIGURAÇÃO]
```  
#### Exemplos
```bash
$ git config --global user.email
$ git config --global user.name
$ git config --global --list
```  

### 📋 Visualizar as informações do commit:
```bash
$ git log
```  

### 📋 Visualizar um log mais robusto:
```bash
$ git reflog
```  

### 📋 Definir uma configuração:
```bash
$ git config [ESCOPO] [CONFIGURAÇÃO] [VALOR]
```  
#### Exemplos
```bash
$ git config --global user.email meu_email@gmail.com
$ git config --global user.name meu_nome
```  

### 📋 Adicionar um arquivo ao git:
```bash
$ git add [ARQUIVO]
```  
#### Exemplos
```bash
$ git add .
$ git add README.md
```  

### 📋 Comitar as mudanças com uma mensagem:
```bash
$ git commit -m"[MENSAGEM]"
```  

### 📋 Muda a mensagem de commmit:
```bash
$ git commit --amend -m"MENSAGEM"
```  

### 📋 Recupera um arquivo:
```bash
$ git restore [TYPE] [ARQUIVO]: 
```  
#### Exemplos:
```bash
$ git restore --source exemplo.txt
$ git restore --staged exemplo.txt
$ git restore --worktree exemplo.txt
```  

### 📋 Reseta o repositório:
```bash
$ git reset [TYPE] [HASH/ARQUIVO]
```  
#### Exemplos:
```bash
git reset --mixed HEAD~1
git reset --soft HEAD~1
git reset --hard HEAD~1
```  

### 📋 Definir a branch padrão:
```bash
$ git config --global init.defaultbranch main
```  

### 📋 Configurar o armazenamento de credenciais:
```bash
$ git config [ESCOPO] credential.helper [VALOR]
```  
#### Exemplos:
```bash
$ git config --global credential.helper store
$ git config --global credential.helper cache
$ git config --global credential.helper manager
``` 

### 📋 Conectar um repositório local com um remoto:
```bash
$ git remote add origin [LINK]
```  
#### Exemplos:
```bash
$ git remote add origin https://github.com/FabricioDosSantosMoreira/DIO.me
``` 

### 📋 Adicionar um remote upstream para manter o repositório local atualizado:
```bash
$ git remote add upstream [LINK]
```  
#### Exemplos:
```bash
$ git remote add upstream https://github.com/FabricioDosSantosMoreira/DIO.me
``` 


## ⚙ Outros Comandos Úteis do Git:

### Criar uma nova branch e mudar para ela:
```bash
$ git checkout -b teste
``` 

### Mudar para uma branch específica a partir da branch principal (main):
```bash
$ git checkout [BRANCH] main
```

### Listar os últimos commits de cada branch:
```bash
$ git checkout -v
```

### Mesclar uma branch específica com a branch atual:
```bash
$ git merge [BRANCH]
```

### Listar as branches no repositório atual:
```bash
$ git branch
```

### Deletar uma branch específica:
```bash
$ git branch -d [BRANCH]
```

### Baixar as alterações do repositório remoto sem afetar o local:
```bash
$ git fetch origin main
```

### Mostrar as diferenças entre as branches:
```bash
$ git diff main origin/main
```

### Mesclar as alterações da branch remota com a branch local:
```bash
$ git merge origin/main
```

### Comandos relacionados ao stash:
```bash
$ git stash
```
#### Exemplos:
```bash
$ git stash list
$ git stash pop
$ git stash apply
```

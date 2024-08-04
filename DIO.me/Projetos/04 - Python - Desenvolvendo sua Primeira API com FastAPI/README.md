# 🥇 WorkOutAPI

O WorkOutAPI é uma API desenvolvida em `Python` utilizando o framework `FastAPI` (async), juntamente com as libs: `SQLAlchemy`, `Alembic` e `Pydantic`. Já na parte de banco de dados, foi utilizado o `Postgres` localmente. O projeto utiliza o `Poetry` para o controle de suas dependências.


## ⚙ Instalação

### 🔹 Clone o repositório principal do projeto

```bash
git clone https://github.com/FabricioDosSantosMoreira/DIO.me.git
```

### 🔹 Navegue até o diretório do projeto

```bash
cd .\WorkOutAPI\
```

### 🔹 Instale as dependências do projeto

```bash
pip install poetry 
```
```bash
poetry shell
```
```bash
poetry install
```

### 🔹 Configure o banco de dados

Crie um novo banco de dados localmente usando o `Postgres`, contendo:
- Usuário = `postgres`
- Senha = `123456`
- Nome = `workout`
- Host = `localhost`
- Porta = `5432`

Ou, se preferir você pode mudar as configurações em: `configs/settings.py`.


## 🟢 Execução da API
 
Utilize o `Make` para criar e executar as migrações, em seguida subir a API:
```bash
make first-run
```
Já com as migrações criadas, caso queira subir a API novamente, utilize:
```bash
make run
```

### 🔹 Documentação da API
Você pode visualizar a documentação da API e testar as rotas interativamente via Swagger em `/docs`.

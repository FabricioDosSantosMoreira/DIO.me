# 🛒 StoreAPI

A StoreAPI é uma API desenvolvida em `Python` com as técnicas de `Test Driven Development (TDD)` utilizando o framework `FastAPI`, juntamente com as libs: `Pydantic`, `Pytest` e `Uvicorn`. Já na parte de banco de dados foi utilizado o `MongoDB` localmente. O projeto utiliza o `Poetry` para o controle de suas dependências.


## ⚙ Instalação

### 🔹 Clone o repositório principal do projeto

```bash
git clone https://github.com/FabricioDosSantosMoreira/DIO.me.git
```

### 🔹 Navegue até o diretório do projeto

```bash
cd .\StoreAPI\
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

### 🔹 Configurar o MongoDB

Crie um novo banco de dados localmente usando o `MongoDB`, contendo:
- Nome= `store`
- Host= `localhost`
- Porta= `27017`
- Coleção= `products`

Ou, se preferir você pode mudar as configurações em: `core/config.py`.


## 🟢 Execução da API

Utilize o `Make` para testar e subir a API:
```bash
make run
```
```bash
make test
```
```bash
make test-matching K=controllers
```

### 🔹 Documentação da API

Você pode visualizar a documentação da API e testar as rotas interativamente via Swagger em `/docs`.

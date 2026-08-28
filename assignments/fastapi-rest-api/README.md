# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST usando o framework FastAPI, organizando rotas HTTP, validando dados com modelos Pydantic e retornando respostas JSON. Ao final, você terá uma API simples para gerenciar uma coleção de livros em memória.

## 📝 Tarefas

### 🛠️ Criar endpoints básicos

#### Descrição

Configure uma aplicação FastAPI e crie endpoints para apresentar informações da API e listar os livros disponíveis.

#### Requisitos

O programa concluído deve:

- Criar uma instância do FastAPI.
- Implementar `GET /` retornando uma mensagem indicando que a API está funcionando.
- Implementar `GET /books` retornando a lista de livros em formato JSON.
- Iniciar a aplicação com um servidor ASGI, como o Uvicorn.

### 🛠️ Validar dados de livros

#### Descrição

Defina um modelo Pydantic para representar livros e implemente um endpoint para adicionar novos livros à coleção.

#### Requisitos

O programa concluído deve:

- Criar um modelo `Book` com os campos `id`, `title`, `author` e `year`.
- Usar validação de tipos por meio do Pydantic.
- Implementar `POST /books` aceitando um livro no corpo da requisição.
- Retornar o livro criado com status HTTP `201`.
- Rejeitar requisições com campos obrigatórios ausentes ou tipos inválidos.

Exemplo de requisição:

```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```

### 🛠️ Implementar operações CRUD

#### Descrição

Complete a API adicionando endpoints para consultar, atualizar e remover livros específicos.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar um livro pelo ID.
- Retornar status HTTP `404` quando o livro solicitado não existir.
- Implementar `PUT /books/{book_id}` para atualizar os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Retornar respostas JSON claras e códigos HTTP adequados para cada operação.

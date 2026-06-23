# Aula 1 — Fundação do Sistema

## Objetivo

Ao final desta aula, o programa deve permitir **adicionar** e **listar**
tarefas através de um menu simples no terminal.

## O que vocês vão implementar em `main.py`

Procurem os comentários marcados com `# TODO (Aula 1)`:

- [ ] `adicionar_tarefa(titulo, prioridade)` — cria um dicionário de
      tarefa e adiciona à lista `tarefas`
- [ ] `listar_tarefas()` — exibe todas as tarefas formatadas
- [ ] Completar `exibir_menu()` com a opção de Sair
- [ ] Completar `main()` com a opção de Sair (usando `break`)

> Ignorem por enquanto os comentários marcados `# TODO (Aula 2)` e
> `# TODO (Aula 3)` — vocês vão voltar a eles nas próximas aulas.

## Como testar

```bash
python3 main.py
```

Teste o seguinte fluxo:
1. Escolha a opção 1 e adicione 2 ou 3 tarefas
2. Escolha a opção 2 e veja se elas aparecem listadas corretamente
3. Escolha a opção de sair e veja se o programa encerra

## Dicas

- Uma tarefa é só um dicionário: `{"titulo": ..., "concluida": ..., "prioridade": ...}`
- `enumerate(tarefas, start=1)` ajuda a numerar a lista a partir de 1
- Não esqueçam do `return` em `listar_tarefas()` quando a lista estiver vazia

## Perguntas para pensar

- Por que `adicionar_tarefa` recebe `prioridade="media"` como valor padrão?
- O que aconteceria se a opção de sair não tivesse um `break`?

## Ao terminar

```bash
git add main.py
git commit -m "Aula 1 concluida"
```

Na próxima aula, abram o arquivo `AULA2.md`.

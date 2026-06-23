# Aula 2 — Lógica e Manipulação de Tarefas

## Objetivo

Ao final desta aula, o programa deve permitir **concluir**, **remover** e
**editar** tarefas, além de tratar entradas inválidas sem quebrar.

## O que já deve estar pronto (da Aula 1)

- `adicionar_tarefa()`
- `listar_tarefas()`
- Opção de Sair no menu

Se algo da Aula 1 ainda não está funcionando, vale a pena resolver antes
de seguir.

## O que vocês vão implementar em `main.py`

Procurem os comentários marcados com `# TODO (Aula 2)`:

- [ ] `concluir_tarefa(indice)` — marca uma tarefa como concluída
- [ ] `remover_tarefa(indice)` — remove uma tarefa da lista
- [ ] `editar_tarefa(indice, novo_titulo)` — atualiza o título (desafio)
- [ ] Atualizar `exibir_menu()` com as opções 3 (Concluir), 4 (Remover)
      e 5 (Editar)
- [ ] Atualizar `main()` para tratar essas três opções, cada uma com
      `try/except` para entradas inválidas

> Ignorem por enquanto os comentários marcados `# TODO (Aula 3)`.

## Como testar

```bash
python3 main.py
```

Teste o seguinte fluxo:
1. Adicione 3 tarefas
2. Conclua a tarefa número 2 e liste — ela deve aparecer com `[X]`
3. Remova a tarefa número 1 e liste — a numeração deve se ajustar
4. Tente digitar uma letra em vez de um número na opção de concluir —
   o programa não deve quebrar
5. (Desafio) Edite o título de uma tarefa

## Dicas

- O índice que o usuário digita começa em 1, mas listas em Python começam
  em 0 — não esqueçam do `indice - 1`
- `tarefas.pop(indice - 1)` remove e retorna o item removido ao mesmo tempo
- `int(input(...))` pode lançar `ValueError` — usem `try/except` para tratar

## Perguntas para pensar

- Por que validar o índice antes de acessar `tarefas[indice - 1]`?
- O que aconteceria se vocês esquecessem o `except ValueError`?

## Ao terminar

```bash
git add main.py
git commit -m "Aula 2 concluida"
```

Na próxima aula, abram o arquivo `AULA3.md`.

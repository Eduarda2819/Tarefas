# Aula 3 — Persistência (CSV) e Finalização

## Objetivo

Ao final desta aula, o programa deve **salvar as tarefas em um arquivo
CSV** e **carregá-las automaticamente** quando o programa é aberto de
novo — ou seja, os dados não se perdem mais ao fechar o terminal.

## O que já deve estar pronto (das Aulas 1 e 2)

- `adicionar_tarefa()`, `listar_tarefas()`
- `concluir_tarefa()`, `remover_tarefa()`, `editar_tarefa()`
- Menu com as opções 1 a 5 e a opção de Sair

## O que vocês vão implementar em `main.py`

Procurem os comentários marcados com `# TODO (Aula 3)`:

- [ ] `salvar_tarefas()` — grava a lista `tarefas` em `tarefas.csv`
      usando `csv.DictWriter`
- [ ] `carregar_tarefas()` — lê `tarefas.csv` ao iniciar o programa
      usando `csv.DictReader`
- [ ] Chamar `salvar_tarefas()` dentro de `adicionar_tarefa`,
      `concluir_tarefa`, `remover_tarefa` e `editar_tarefa`
- [ ] Chamar `carregar_tarefas()` no início de `main()`
- [ ] `listar_pendentes()` — desafio: mostrar só as tarefas não concluídas
- [ ] Atualizar `exibir_menu()` e `main()` com a opção 6 (Listar
      pendentes) e renumerar a opção de Sair para 7

## Como testar

```bash
python3 main.py
```

Teste o seguinte fluxo:
1. Adicione algumas tarefas e conclua uma delas
2. Saia do programa
3. Rode `python3 main.py` de novo — as tarefas devem continuar lá
4. Abram o arquivo `tarefas.csv` gerado (pode ser num editor de texto ou
   no Excel/Google Sheets) e vejam como os dados ficaram salvos
5. (Desafio) Testem a opção de listar pendentes

## Atenção: tudo no CSV é texto

Diferente de um dicionário em Python, um arquivo CSV guarda tudo como
texto puro. Isso significa que a coluna `concluida`, que no programa é
`True` ou `False` (booleano), vai ser salva no arquivo como o texto
`"True"` ou `"False"`.

Quando vocês lerem o arquivo de volta com `carregar_tarefas()`, precisam
converter esse texto de volta para um valor booleano:

```python
linha["concluida"] = linha["concluida"] == "True"
```

Sem essa conversão, `if not tarefa["concluida"]` nunca vai funcionar
como esperado, porque a string `"False"` é, sim, um valor "verdadeiro"
em Python (qualquer string não vazia é).

## Dicas

- `tarefas.csv` é criado automaticamente na primeira vez que vocês
  chamarem `salvar_tarefas()` — não precisam criar o arquivo manualmente
- Esse arquivo está no `.gitignore`, então ele não deve aparecer no
  `git status` nem ser commitado
- Pensem: por que chamar `salvar_tarefas()` dentro de cada função que
  altera a lista, em vez de só uma vez ao sair do programa? Quais são
  as vantagens e desvantagens de cada abordagem?

## Ao terminar

```bash
git add main.py
git commit -m "Aula 3 concluida - projeto finalizado"
```

Parabéns — vocês concluíram o mini projeto! 🎉

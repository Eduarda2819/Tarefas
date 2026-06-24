"""
Gerenciador de Tarefas (To-Do List) em terminal
Mini projeto de 3 aulas — Python puro

Este arquivo cresce ao longo das 3 aulas. Cada bloco abaixo está marcado
com a aula em que deve ser implementado:

    # ===== AULA 1 =====
    # ===== AULA 2 =====
    # ===== AULA 3 =====

Leia o arquivo AULA1.md (depois AULA2.md, depois AULA3.md) para saber
exatamente o que fazer em cada parte. Procure os comentários "# TODO"
-- é ali que vocês vão escrever código. Não apague as docstrings, elas
explicam o que cada função deve fazer.
"""

import csv
import os

# ===== AULA 3 =====
ARQUIVO_TAREFAS = "tarefas.csv"
CAMPOS_CSV = ["titulo", "concluida", "prioridade"]

# Lista que vai guardar todas as tarefas.
# Cada tarefa é um dicionário com as chaves: "titulo", "concluida", "prioridade"
tarefas = []


# =====================================================================
# ===== AULA 1 — Fundação do sistema =====
# =====================================================================

def adicionar_tarefa(titulo, prioridade="media"):
    tarefa = {'titulo':titulo, 'concluida':False, 'prioridade':prioridade}
    tarefas.append(tarefa)
    print(f"Tarefa {titulo} adicionada")
   


    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def listar_tarefas():
    if len(tarefas) == 0:
          print("Não há tarefas cadastradas")
          return
    else:
         for index, itens in enumerate(tarefas, start=1):
          if itens['concluida' ] == True:
             status = "[X]"
          else:
              status = "[ ]"
          print(f"{index} - Título{itens['titulo']}; Concluida:{itens['concluida']}; Prioridade: {itens['prioridade']}" )




# =====================================================================
# ===== AULA 2 — Lógica e manipulação de tarefas =====
# =====================================================================

def concluir_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Número de tarefa inválido")
        return 
    tarefas[indice - 1]["concluida"] = True
    print(f'Tarefa "{tarefas[indice - 1]["titulo"]}" concluida')
   
  
   
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def remover_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Numero de tarefa invalido.")
        return
 
    tarefa_removida = tarefas.pop(indice - 1)
    print(f'Tarefa "{tarefa_removida["titulo"]}" removida com sucesso!')
 
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def editar_tarefa(indice, novo_titulo):
   if indice < 1 or indice > len(tarefas):
      print("Numero de tarefa invalido.")
      return
   tarefas[indice - 1]["titulo"] = novo_titulo
   print(f'Tarefa atualizada para "{novo_titulo}"!')
 
  
  
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
   pass


# =====================================================================
# ===== AULA 3 — Persistência (CSV) e finalização =====
# =====================================================================

def salvar_tarefas():
    """
    Salva a lista `tarefas` no arquivo CSV definido em ARQUIVO_TAREFAS.

    Use csv.DictWriter dentro de um bloco `with open(...)`.

    Passos:
        1. Abra o arquivo em modo de escrita ("w"), com newline=""
           e encoding="utf-8"
        2. Crie um csv.DictWriter passando o arquivo e fieldnames=CAMPOS_CSV
        3. Chame writer.writeheader() para escrever a linha de cabeçalho
        4. Chame writer.writerows(tarefas) para escrever todas as tarefas
    """
    # TODO (Aula 3): abra o arquivo em modo de escrita
    # TODO (Aula 3): crie o csv.DictWriter com fieldnames=CAMPOS_CSV
    # TODO (Aula 3): escreva o cabeçalho e as linhas
    pass


def carregar_tarefas():
    """
    Carrega as tarefas do arquivo CSV para a lista `tarefas`, caso o
    arquivo já exista.

    Regras:
        - Use `global tarefas` no início da função, já que vamos
          substituir a lista inteira.
        - Se o arquivo não existir, apenas mantenha `tarefas` como uma
          lista vazia (dica: os.path.exists(ARQUIVO_TAREFAS)).
        - Se existir, abra o arquivo e use csv.DictReader para ler cada
          linha como um dicionário.
        - Atenção: tudo que vem do CSV é texto (string)! A coluna
          "concluida" vai vir como a string "True" ou "False", não como
          um valor booleano. Vocês precisam converter isso de volta:
              linha["concluida"] = linha["concluida"] == "True"
    """
    global tarefas
    # TODO (Aula 3): verifique se o arquivo existe, senão mantenha tarefas = []
    # TODO (Aula 3): abra o arquivo e use csv.DictReader para ler as linhas
    # TODO (Aula 3): converta a coluna "concluida" de string para booleano
    # TODO (Aula 3): monte a lista `tarefas` com os dicionários lidos
    pass


def listar_pendentes():
    """
    [DESAFIO] Exibe apenas as tarefas que ainda não foram concluídas.

    Dica: list comprehension ajuda bastante aqui:
        pendentes = [t for t in tarefas if not t["concluida"]]
    """
    # TODO (Aula 3): filtre as tarefas não concluídas
    # TODO (Aula 3): exiba a lista filtrada (mensagem se estiver vazia também)
    pass


# =====================================================================
# Menu e função principal
# =====================================================================

def exibir_menu():
    print("=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("7. Sair")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Editar tarefa")
   
    # TODO (Aula 3): adicione a opção 6 (Listar pendentes) e renumere "Sair" para 7


def main():
    """
    Função principal do programa.

    Versão final esperada (Aula 3): 
        - Antes do loop começar, chame carregar_tarefas() para recuperar
          as tarefas salvas anteriormente.
        - Exiba o menu em loop (while True).
        - "1": pedir o título da tarefa e chamar adicionar_tarefa()
        - "2": chamar listar_tarefas()
        - "3": listar tarefas, pedir o número da tarefa a concluir e
          chamar concluir_tarefa(). Use try/except para tratar entradas
          que não são números (ValueError).
        - "4": o mesmo fluxo, mas chamando remover_tarefa()
        - "5": pedir o número da tarefa e o novo título, chamar
          editar_tarefa()
        - "6": chamar listar_pendentes()
        - "7": exibir mensagem de despedida e encerrar o loop (break)
        - qualquer outra opção: avisar que é inválida

    Vão completando esse fluxo aula a aula — na Aula 1 só "1", "2" e
    sair (que será a última opção, mas pode comecar como "3").
    """
    # TODO (Aula 3): chame carregar_tarefas() antes do loop começar

    while True:
       exibir_menu()
       opcao = input("Escolha uma opcao: ")
       if opcao == "1":
          titulo = input("Titulo da tarefa: ")
          adicionar_tarefa(titulo)
       elif opcao == "2":
           listar_tarefas()
       elif opcao == "7":
             break
       elif opcao == "3":
          try:
              indice = int(input("Numero da tarefa: "))
              concluir_tarefa(indice)
          except ValueError:
           print("Digite um numero valido.")
       elif opcao == "4":
           try:
               indice = int(input("Numero da tarefa: "))
               remover_tarefa(indice)
           except ValueError:
             print("Digite um numero valido.")
       elif opcao == "5":
          try:
           indice = int(input("Numero da tarefa: "))
           novo_titulo = input("Novo titulo: ")
           editar_tarefa(indice, novo_titulo)
          except ValueError:
           print("Digite um numero valido.")
       else:
           print("Opção invalida, tente novamente.\n")
         
        
        # TODO (Aula 3): implemente a opção de listar pendentes e
        #                renumere a opção de sair
if __name__ == "__main__": 
    main()


     

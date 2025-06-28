"""
todo.py
Um gerenciador de tarefas ultra‑simples em linha de comando.

⭐ Como funciona?
- Lê suas tarefas de 'tarefas.json' (criado automaticamente).
- Permite listar, adicionar e marcar como concluídas.
- Salva tudo no mesmo arquivo antes de sair.
"""

import json    # biblioteca padrão para trabalhar com JSON
import os      # para verificar se o arquivo existe

ARQUIVO = "tarefas.json"

# ----------------------------------------------------------------------
# Funções de apoio
# ----------------------------------------------------------------------

def carregar_tarefas():
    """Lê o arquivo JSON e devolve uma lista de tarefas.
       Se o arquivo não existir, devolve lista vazia."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(lista):
    """Grava a lista de tarefas no arquivo JSON (com identação agradável)."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

# ----------------------------------------------------------------------
# Operações principais
# ----------------------------------------------------------------------

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("\n⚠️  Nenhuma tarefa por aqui. Use a opção 2 para criar uma!\n")
        return
    print("\n================= MINHAS TAREFAS =================")
    for idx, t in enumerate(tarefas, start=1):
        status = "✔️" if t["feito"] else "❌"
        print(f"{idx}. [{status}] {t['descricao']}")
    print("==================================================\n")

def adicionar_tarefa():
    desc = input("Digite a descrição da nova tarefa: ").strip()
    if not desc:
        print("Descrição vazia 😕. Tente de novo.")
        return
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": desc, "feito": False})
    salvar_tarefas(tarefas)
    print("🎉 Tarefa adicionada!")

def concluir_tarefa():
    listar_tarefas()
    try:
        num = int(input("Número da tarefa concluída: "))
        tarefas = carregar_tarefas()
        tarefas[num - 1]["feito"] = True
        salvar_tarefas(tarefas)
        print("✅ Bom trabalho! Tarefa marcada como concluída.")
    except (ValueError, IndexError):
        print("Número inválido 😬. Tente novamente.")

# ----------------------------------------------------------------------
# Loop de menu
# ----------------------------------------------------------------------

def menu():
    while True:
        print("\n=== TO‑DO LIST ===")
        print("1) Listar tarefas")
        print("2) Adicionar tarefa")
        print("3) Concluir tarefa")
        print("4) Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            print("👋 Até a próxima!")
            break
        else:
            print("Opção não reconhecida. Digite 1, 2, 3 ou 4.")

if __name__ == "__main__":
    menu()

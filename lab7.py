# -------------------------------------------------------------------------
# ATIVIDADE PRÁTICA: ARQUITETURA DE SISTEMAS DE GESTÃO DO 
# CONHECIMENTO (SGC)
# Disciplina: Gestão de Sistemas de Informação
# Nome dos Alunos: 
# -------------------------------------------------------------------------
import json
import os

# Caminho para o arquivo da Camada de Dados (Persistência)
ARQUIVO_DADOS = "base_conhecimento.json"

def carregar_dados():
    """
    Camada de Dados: Responsável por carregar o conhecimento explícito.
    Retorna uma lista de dicionários.
    """
    if not os.path.exists(ARQUIVO_DADOS):
        # Base de dados inicial (Caso o arquivo ainda não tenha sido criado)
        return [
            {"id": 1, "titulo": "Acesso VPN", "conteudo": "Usar o cliente Cisco AnyConnect...", "acessos": 120},
            {"id": 2, "titulo": "Backup SQL", "conteudo": "Os scripts rodam diariamente às 02h...", "acessos": 45},
            {"id": 3, "titulo": "Lentidão ERP", "conteudo": "Pausar o serviço 'Backup_Sync' no console.", "acessos": 89}
        ]
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return []

def salvar_dados(base):
    """
    TAREFA 3 - Implementar a Camada de Dados (Persistência).
    Objetivo: Salvar a lista 'base' no arquivo 'ARQUIVO_DADOS' em formato JSON.
    """
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(base, f, indent=4, ensure_ascii=False)
        print(f"✓ Dados salvos com sucesso em '{ARQUIVO_DADOS}'")
    except Exception as e:
        print(f"✗ Erro ao salvar os dados: {e}")

def exibir_dashboard(base):
    """
    TAREFA 2 - Implementar a Camada de Apresentação (Interface).
    Objetivo: Criar uma visualização clara para o gestor.
    Exiba uma tabela com ID, Título e uma barra de popularidade proporcional aos acessos.
    """
    if not base:
        print("\n⚠ Nenhum conhecimento disponível para exibir.")
        return
    
    print("\n" + "="*90)
    print(f"{'DASHBOARD DE POPULARIDADE DO CONHECIMENTO':^90}")
    print("="*90)
    print(f"{'ID':<4} | {'TÍTULO':<35} | {'POPULARIDADE (ACESSOS)':<45}")
    print("-"*90)
    
    # Encontrar o máximo de acessos para normalizar a barra
    max_acessos = max(item['acessos'] for item in base) if base else 1
    
    for item in base:
        titulo = item['titulo'][:33]  # Limitar o tamanho do título
        acessos = item['acessos']
        # Calcular o tamanho da barra proporcional (máximo 40 caracteres)
        tamanho_barra = int((acessos / max_acessos) * 40) if max_acessos > 0 else 0
        barra = "█" * tamanho_barra + "░" * (40 - tamanho_barra)
        print(f"{item['id']:<4} | {titulo:<35} | {barra} {acessos}")
    
    print("="*90)

def buscar_conhecimento(base, termo):
    """
    TAREFA 1 - Implementar o Filtro de Busca (Camada de Lógica).
    Objetivo: Buscar conhecimentos pelo termo pesquisado.
    A busca deve ser case-insensitive e procurar no título e conteúdo.
    Utilize List Comprehension para maior eficiência.
    """
    termo_lower = termo.lower()
    resultados = [
        item for item in base 
        if termo_lower in item['titulo'].lower() or termo_lower in item['conteudo'].lower()
    ]
    return resultados

def adicionar_conhecimento(base):
    """
    TAREFA 4 - Módulo de Colaboração.
    Objetivo: Permitir ao usuário adicionar um novo artigo de conhecimento.
    """
    print("\n" + "-"*75)
    print("ADICIONAR NOVO CONHECIMENTO")
    print("-"*75)
    
    try:
        # Encontrar o próximo ID disponível
        proximo_id = max(item['id'] for item in base) + 1 if base else 1
        
        titulo = input("Digite o título do conhecimento: ").strip()
        if not titulo:
            print("✗ Título não pode estar vazio!")
            return base
        
        conteudo = input("Digite o conteúdo do conhecimento: ").strip()
        if not conteudo:
            print("✗ Conteúdo não pode estar vazio!")
            return base
        
        novo_item = {
            "id": proximo_id,
            "titulo": titulo,
            "conteudo": conteudo,
            "acessos": 0
        }
        
        base.append(novo_item)
        print(f"✓ Conhecimento adicionado com sucesso! (ID: {proximo_id})")
        
    except Exception as e:
        print(f"✗ Erro ao adicionar conhecimento: {e}")
    
    return base

def exibir_menu():
    """
    Exibe o menu principal do sistema.
    """
    print("\n" + "="*75)
    print(f"{'SISTEMA DE GESTÃO DO CONHECIMENTO (SGC)':^75}")
    print("="*75)
    print("[1] Exibir Dashboard de Popularidade")
    print("[2] Buscar Conhecimento")
    print("[3] Adicionar Novo Conhecimento")
    print("[4] Sair")
    print("="*75)

def main():
    """
    Função principal que coordena a execução do sistema.
    """
    base = carregar_dados()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            exibir_dashboard(base)
        
        elif opcao == "2":
            termo = input("\nDigite o termo para buscar: ").strip()
            if termo:
                resultados = buscar_conhecimento(base, termo)
                if resultados:
                    print(f"\n✓ {len(resultados)} resultado(s) encontrado(s):")
                    print("-"*75)
                    for item in resultados:
                        print(f"ID: {item['id']}")
                        print(f"Título: {item['titulo']}")
                        print(f"Conteúdo: {item['conteudo']}")
                        print(f"Acessos: {item['acessos']}")
                        print("-"*75)
                else:
                    print("\n✗ Nenhum resultado encontrado para essa busca.")
            else:
                print("\n⚠ Digite um termo válido para buscar.")
        
        elif opcao == "3":
            base = adicionar_conhecimento(base)
            salvar_dados(base)
        
        elif opcao == "4":
            print("\n✓ Sistema encerrado. Até logo!")
            break
        
        else:
            print("\n✗ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

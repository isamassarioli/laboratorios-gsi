import pandas as pd
import random

# =========================================================
# ATIVIDADE 3 - GERENCIAMENTO DE INCIDENTES E FILAS (ITIL)
# =========================================================

random.seed(123)

# 1. Configuração do log de incidentes
n_incidentes = 20
prioridades = ['Alta', 'Media', 'Baixa']
filas_iniciais = ['N1', 'N2']

dados_incidentes = {
    'ticket_id': range(2001, 2001 + n_incidentes),
    'prioridade': [random.choice(prioridades) for _ in range(n_incidentes)],
    'fila_inicial': [random.choice(filas_iniciais) for _ in range(n_incidentes)],
    # tempo de espera entre 0 e 0.8h (0 a 48 minutos)
    'tempo_espera_horas': [round(random.uniform(0.0, 0.8), 2) for _ in range(n_incidentes)],
    # tempo total entre 0.5h e 5h
    'tempo_resolucao_total_horas': [round(random.uniform(0.5, 5.0), 2) for _ in range(n_incidentes)]
}
df_incidentes = pd.DataFrame(dados_incidentes)

# 2. Metas de SLA da TechStore S.A. para incidentes de prioridade Alta
meta_espera_n1_alta = 0.25 # 15 minutos
meta_resolucao_alta = 2.0  # 2 horas

# --- INÍCIO DA TAREFA DO ALUNO ---

print("=== LOG DE INCIDENTES POR FILA TECHSTORE S.A. ===")
print(df_incidentes.head())

# 3. Filtrar apenas incidentes de prioridade Alta
incidentes_alta = df_incidentes[df_incidentes['prioridade'] == 'Alta']

# 4. Violações de SLA de tempo de espera (apenas quando fila inicial é N1)
violacoes_espera_n1 = incidentes_alta[
    (incidentes_alta['fila_inicial'] == 'N1') &
    (incidentes_alta['tempo_espera_horas'] > meta_espera_n1_alta)
]

# 5. Violações de SLA de tempo total de resolução (independente da fila)
violacoes_resolucao_total = incidentes_alta[
    incidentes_alta['tempo_resolucao_total_horas'] > meta_resolucao_alta
]

print("\n" + "=" * 65)
print("RELATÓRIO DE GOVERNANÇA - GERENCIAMENTO DE INCIDENTES (PRIORIDADE ALTA)")
print("=" * 65)

# 6. Exibição das violações de tempo de espera em N1
print("\nA) Violações de SLA de TEMPO DE ESPERA na Fila N1 (Alta):")
print(f"Critério: espera > {meta_espera_n1_alta} horas (15 minutos)")

if violacoes_espera_n1.empty:
    print("Nenhuma violação de tempo de espera em N1 para incidentes de prioridade Alta.")
else:
    print(violacoes_espera_n1)
    print(f"Total de violações de espera em N1: {len(violacoes_espera_n1)}")

# 7. Exibição das violações de tempo total de resolução
print("\nB) Violações de SLA de TEMPO TOTAL DE RESOLUÇÃO (Alta):")
print(f"Critério: resolução total > {meta_resolucao_alta} horas")

if violacoes_resolucao_total.empty:
    print("Nenhuma violação de tempo total de resolução para incidentes de prioridade Alta.")
else:
    print(violacoes_resolucao_total)
    print(f"Total de violações de tempo total de resolução: {len(violacoes_resolucao_total)}")

# 8. Estatísticas gerais (opcional)
print("\nResumo de incidentes de prioridade Alta:")
print(incidentes_alta[['tempo_espera_horas', 'tempo_resolucao_total_horas']].describe())

# --- FIM DA TAREFA DO ALUNO ---
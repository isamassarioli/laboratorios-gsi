import pandas as pd
import random
import matplotlib.pyplot as plt

# =========================================================
# ATIVIDADE 2 - GERENCIAMENTO DE MUDANÇAS (ITIL)
# =========================================================

random.seed(7)

# 1. Geração do log de RFCs (Requests for Change)
n_mudancas = 25
tipos = ['Normal', 'Padrao', 'Emergencia']
status_aprovacao = ['Aprovada', 'Aprovada', 'Aprovada', 'Nao Aprovada'] # ~25% sem aprovação

dados_mudancas = {
    'rfc_id': [f'RFC-{i}' for i in range(3001, 3001 + n_mudancas)],
    'tipo': [random.choice(tipos) for _ in range(n_mudancas)],
    'aprovacao': [random.choice(status_aprovacao) for _ in range(n_mudancas)],
    'implementada': ['Sim'] * n_mudancas # Todas foram para produção
}
df_mudancas = pd.DataFrame(dados_mudancas)

# --- INÍCIO DA TAREFA DO ALUNO ---

# 2. Identifique mudanças implementadas sem aprovação (violação de governança)
nao_autorizadas = df_mudancas[
    (df_mudancas['implementada'] == 'Sim') & 
    (df_mudancas['aprovacao'] == 'Nao Aprovada')
]

print("=== LOG DE MUDANÇAS TECHSTORE S.A. ===")
print(df_mudancas.head()) # Usando head para não poluir muito a tela
print("\n" + "=" * 55)
print("AUDITORIA DE CHANGE MANAGEMENT")
print("Mudanças implementadas SEM aprovação prévia:")
print("=" * 55)

if nao_autorizadas.empty:
    print("Nenhuma não-conformidade detectada.")
else:
    print(nao_autorizadas)
    print(f"\nTotal de mudanças não autorizadas: {len(nao_autorizadas)}")
    taxa = round((len(nao_autorizadas) / len(df_mudancas)) * 100, 1)
    print(f"Taxa de não-conformidade: {taxa}%")

# 3. Distribuição por tipo de mudança
contagem_tipos = df_mudancas['tipo'].value_counts()
print("\nDistribuição de mudanças por tipo:")
print(contagem_tipos)

# 4 (Opcional). Gráfico de pizza dos tipos de mudança
plt.figure(figsize=(6, 6))
plt.pie(
    contagem_tipos,
    labels=contagem_tipos.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=['steelblue', 'mediumseagreen', 'tomato']
)
plt.title('Distribuição de Mudanças por Tipo - TechStore S.A.')
plt.tight_layout()
plt.show()

# --- FIM DA TAREFA DO ALUNO ---
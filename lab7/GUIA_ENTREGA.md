# 📋 GUIA DE ENTREGA - LABORATÓRIO 7
## SGC - Implementando a Arquitetura de um Sistema de Gestão do Conhecimento

---

## 📦 INSTRUÇÕES PARA CRIAR O ARQUIVO PDF

### Estrutura do PDF (Laboratorio_7_NomesDosAlunos.pdf):

```
1. CAPA
   - Título: "Laboratório 7 - Implementando a Arquitetura de um SGC"
   - Disciplina: Gestão de Sistemas de Informação
   - Nomes dos alunos
   - Data: Até 23/04/2026

2. ÍNDICE
   - Lista de todas as seções

3. OBJETIVO DA ATIVIDADE
   - Texto descritivo dos objetivos

4. ARQUITETURA IMPLEMENTADA
   - Diagrama das 3 camadas
   - Explicação de cada camada

5. CÓDIGO-FONTE (Comentado)
   - lab7.py completo com comentários

6. EVIDÊNCIAS DE EXECUÇÃO
   - 6 prints de tela organizados
   - Explicações de cada fluxo

7. ANÁLISE DE RESULTADOS
   - Validação dos critérios
   - Discussão das soluções

8. CONCLUSÃO
   - Resumo e aprendizados
```

---

## 🖼️ PRINTS DE TELA A CAPTURAR

### Print 1: Menu Principal
**Descrição:** Tela inicial do sistema com opções de menu

### Print 2: Dashboard de Popularidade
**Descrição:** Visualização das barras proporcionais com estatísticas de acesso

### Print 3: Busca sem Resultado
**Descrição:** Busca por termo inexistente ("Azul")

### Print 4: Adição de Novo Conhecimento
**Descrição:** Processo de adicionar um novo artigo (título e conteúdo)

### Print 5: Confirmação de Salvamento
**Descrição:** Mensagem de sucesso ao salvar dados

### Print 6: Busca com Resultado
**Descrição:** Busca encontrando o artigo recém-adicionado

### Print 7 (Opcional): Arquivo JSON
**Descrição:** Conteúdo do arquivo base_conhecimento.json aberto em editor de texto

---

## 📄 SEÇÕES DE CÓDIGO A INCLUIR

### 1. Código Completo (lab7.py)
- Incluir todo o arquivo com comentários descritivos

### 2. Tarefas Específicas

#### ✅ Tarefa 1: Busca (Camada de Lógica)
```python
def buscar_conhecimento(base, termo):
    # Implementação...
```

#### ✅ Tarefa 2: Dashboard (Camada de Apresentação)
```python
def exibir_dashboard(base):
    # Implementação...
```

#### ✅ Tarefa 3: Persistência (Camada de Dados)
```python
def salvar_dados(base):
    # Implementação...
```

#### ✅ Tarefa 4: Colaboração
```python
def adicionar_conhecimento(base):
    # Implementação...
```

---

## 📊 EXPLICAÇÕES POR FLUXO

### Fluxo 1: Visualizar Dashboard
1. Usuário seleciona opção [1]
2. Sistema carrega dados do arquivo JSON
3. Calcula estatísticas de popularidade
4. Exibe barras visuais proporcionais
5. Retorna ao menu

**Objetivo da Camada:** Apresentação clara dos dados

### Fluxo 2: Buscar Conhecimento
1. Usuário seleciona opção [2]
2. Digita termo de busca
3. Sistema aplica List Comprehension
4. Busca case-insensitive em título e conteúdo
5. Exibe resultados ou mensagem de "não encontrado"

**Objetivo da Camada:** Lógica de filtro inteligente

### Fluxo 3: Adicionar Conhecimento
1. Usuário seleciona opção [3]
2. Digita título e conteúdo
3. Sistema valida entrada
4. Gera novo ID automaticamente
5. Chama função salvar_dados()
6. Persiste em JSON

**Objetivo da Camada:** Colaboração e persistência

---

## ✅ CHECKLIST DE ENTREGA

- [ ] Arquivo nomeado como: `Laboratorio_7_NomesDosAlunos.pdf`
- [ ] Contém código-fonte completo (lab7.py)
- [ ] Todos os 6 prints de tela inclusos
- [ ] Explicações para cada print
- [ ] Análise de critérios de avaliação
- [ ] Diagrama/explicação da arquitetura em 3 camadas
- [ ] Conclusões sobre o aprendizado
- [ ] PDF gerado com boa formatação
- [ ] Entregue até 23/04/2026

---

## 🛠️ FERRAMENTAS RECOMENDADAS PARA CRIAR O PDF

### Opção 1: Google Docs
1. Copiar prints para Google Docs
2. Inserir código com formatação
3. Exportar como PDF

### Opção 2: Microsoft Word
1. Criar documento no Word
2. Inserir prints e código
3. Exportar como PDF

### Opção 3: Python (reportlab/FPDF2)
```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Laboratorio 7 - SGC", ln=True)
# Adicionar conteúdo...
pdf.output("Laboratorio_7_NomesDosAlunos.pdf")
```

### Opção 4: LibreOffice Writer
1. Documento ODT com conteúdo
2. Exportar direto para PDF

---

## 📝 TEMPLATE DE EXPLICAÇÃO POR PRINT

Para cada print de tela, incluir:

**Print X: [Título da Tela]**

**Descrição:**
- O que está sendo demonstrado
- Qual tarefa/funcionalidade

**Fluxo:**
- Sequência de passos

**Resultado:**
- O que o sistema exibe
- Como validar o correto funcionamento

**Critério Atendido:**
- Qual critério de avaliação este print valida

---

## 📚 ESTRUTURA RECOMENDADA DO PDF

```
Página 1: Capa
Página 2: Índice
Página 3-4: Objetivo e Contexto
Página 5: Arquitetura em Camadas
Página 6-7: Código-Fonte Completo
Página 8-15: Evidências de Execução (6 fluxos)
Página 16-17: Análise de Resultados
Página 18: Conclusão
```

---

## 💡 DICAS IMPORTANTES

✅ **Use caracteres claros:** Certifique-se que os prints estejam legíveis
✅ **Organize cronologicamente:** Fluxos na ordem lógica de execução
✅ **Comente o código:** Deixe claro o que cada função faz
✅ **Explique decisões:** Por que usou List Comprehension? Por que case-insensitive?
✅ **Valide critérios:** Mostre como atendeu cada critério de avaliação
✅ **Profissionalismo:** PDF bem formatado e organizado

---

## 📞 RESUMO FINAL

Este laboratório demonstra:
- ✓ Compreensão de arquitetura em camadas
- ✓ Implementação de sistema prático em Python
- ✓ Persistência de dados em JSON
- ✓ Interface amigável ao usuário
- ✓ Busca inteligente e eficiente
- ✓ Qualidade de código

**Data Limite: 23 de Abril de 2026**
**Formato: PDF - Laboratorio_7_NomesDosAlunos.pdf**

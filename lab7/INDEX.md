# 📚 ÍNDICE DE ARQUIVOS - LABORATÓRIO 7 SGC

**Data:** 16 de Abril de 2026
**Disciplina:** Gestão de Sistemas de Informação
**Tema:** Arquitetura de Sistemas de Gestão do Conhecimento
**Data de Entrega:** até 23 de Abril de 2026

---

## 📁 ESTRUTURA DE DIRETÓRIOS

```
lab7/
├── lab7.py                          ← CÓDIGO PRINCIPAL
├── base_conhecimento.json           ← DADOS PERSISTIDOS
├── RESUMO_FINAL.md                  ← RESUMO EXECUTIVO
├── EVIDENCIAS_EXECUCAO.md           ← PRINTS DOCUMENTADOS
├── GUIA_ENTREGA.md                  ← INSTRUÇÕES PDF
├── TEMPLATE_PDF.md                  ← MODELO DO PDF
├── MANUAL_PRINTS.txt                ← GUIA VISUAL
├── teste_fluxos.py                  ← SCRIPT DE TESTE
├── INDEX.md                         ← ESTE ARQUIVO
└── .git/                            ← CONTROLE DE VERSÃO
```

---

## 📄 DESCRIÇÃO DE CADA ARQUIVO

### 1. **lab7.py** ⭐ (ARQUIVO PRINCIPAL)

**Tipo:** Script Python
**Tamanho:** ~400 linhas
**Objetivo:** Código-fonte completo do Sistema SGC

**Contém:**
- ✅ Tarefa 1: `buscar_conhecimento()` - Busca com List Comprehension
- ✅ Tarefa 2: `exibir_dashboard()` - Dashboard visual
- ✅ Tarefa 3: `salvar_dados()` - Persistência em JSON
- ✅ Tarefa 4: `adicionar_conhecimento()` - Módulo colaborativo
- ✅ Menu interativo
- ✅ Comentários explicativos
- ✅ Tratamento de erros

**Como Usar:**
```bash
cd lab7
python lab7.py
```

**Testado e Validado:** ✅ SEM ERROS

---

### 2. **base_conhecimento.json**

**Tipo:** Arquivo JSON
**Formato:** Array de dicionários
**Encoding:** UTF-8

**Contém:**
- 3 artigos pré-existentes (Acesso VPN, Backup SQL, Lentidão ERP)
- 1 artigo adicionado durante execução (Configuração de Firewall)
- Total: 4 artigos de conhecimento

**Estrutura de Cada Item:**
```json
{
    "id": 1,
    "titulo": "string",
    "conteudo": "string",
    "acessos": number
}
```

**Atualizado:** ✅ COM NOVO ARTIGO

---

### 3. **RESUMO_FINAL.md** 📋

**Tipo:** Markdown (Resumo)
**Páginas:** 3-4 (quando convertido para PDF)
**Objetivo:** Resumo executivo completo

**Seções:**
- Arquivos preparados
- 4 tarefas implementadas
- Critérios de avaliação
- Prints de tela a capturar
- Dados persistidos
- Estrutura do PDF
- Próximas etapas
- Verificação final
- Conceitos aprendidos

**Usar Para:** Visão geral completa do projeto

---

### 4. **EVIDENCIAS_EXECUCAO.md** 🖼️

**Tipo:** Markdown (Documentação)
**Páginas:** 8-10 (quando convertido para PDF)
**Objetivo:** Documentar cada print de tela

**Seções:**
- 6 Prints de tela comentados
- Explicação de cada fluxo
- Código implementado (snippets)
- Validações realizadas
- Critérios atendidos

**Usar Para:** Incluir como base do PDF

**Prints Documentados:**
1. Menu Principal
2. Dashboard (3 artigos)
3. Busca sem resultado
4. Adição de novo conhecimento
5. Confirmação de salvamento
6. Busca com resultado

---

### 5. **GUIA_ENTREGA.md** 📝

**Tipo:** Markdown (Instruções)
**Páginas:** 2-3 (referência)
**Objetivo:** Instruções para criar o PDF

**Contém:**
- Estrutura recomendada do PDF
- Prints de tela a capturar
- Seções de código a incluir
- Explicações por fluxo
- Checklist de entrega
- Ferramentas recomendadas
- Template de explicação

**Usar Para:** Consulta durante criação do PDF

---

### 6. **TEMPLATE_PDF.md** 📘

**Tipo:** Markdown (Template Completo)
**Páginas:** 20+ (quando convertido)
**Objetivo:** Template pronto para o PDF de entrega

**Estrutura Completa:**
- Capa
- Índice
- Objetivo da atividade
- Contexto da arquitetura
- Arquitetura implementada (com diagrama)
- Código-fonte comentado
- 6 evidências de execução (com espaço para prints)
- Análise de resultados
- Conclusões
- Referências bibliográficas
- Anexos (JSON, instruções)

**Usar Para:** Base do PDF final (copiar e colar, adicionar prints)

---

### 7. **MANUAL_PRINTS.txt** 📸

**Tipo:** Texto Puro (ASCII)
**Páginas:** 5-6 (quando impresso)
**Objetivo:** Guia visual para capturar prints

**Contém:**
- Passo a passo detalhado (13 prints)
- O que capturar em cada etapa
- Dados esperados em cada print
- Legendas prontas para PDF
- Ferramentas recomendadas
- Templates de legendas
- Dicas finais

**Usar Para:** Guia durante captura dos prints

**Prints Descritos:**
1. Menu Principal
2. Dashboard (3 artigos)
3. Menu (retorno)
4-5. Busca sem resultado
6-8. Adição de conhecimento
9-10. Busca com resultado
11. Busca artigo pré-existente
12. Dashboard atualizado
13. Encerramento

---

### 8. **teste_fluxos.py**

**Tipo:** Script Python (Referência)
**Objetivo:** Guia de testes e fluxos

**Contém:**
- Instruções de execução
- Sequência de fluxos
- Dicas para capturas
- Nomes de arquivos

**Usar Para:** Referência durante testes

---

### 9. **INDEX.md** (ESTE ARQUIVO)

**Tipo:** Markdown (Índice)
**Objetivo:** Visão geral de todos os arquivos

**Contém:**
- Estrutura de diretórios
- Descrição de cada arquivo
- Como usar cada um
- Instruções de entrega

---

## 🎯 QUAL ARQUIVO USAR PARA CADA TAREFA?

### Para Entender o Projeto
→ Leia: **RESUMO_FINAL.md**

### Para Capturar os Prints
→ Siga: **MANUAL_PRINTS.txt**

### Para Criar o PDF
→ Use como base: **TEMPLATE_PDF.md**
→ Consulte: **GUIA_ENTREGA.md**
→ Inclua evidências de: **EVIDENCIAS_EXECUCAO.md**

### Para Executar o Sistema
→ Execute: **python lab7.py**

### Para Consultar Dados Salvos
→ Abra: **base_conhecimento.json**

---

## ✅ CHECKLIST DE PREPARAÇÃO

### Código-Fonte
- [ ] lab7.py criado ✅
- [ ] Todas as 4 tarefas implementadas ✅
- [ ] Código testado e sem erros ✅
- [ ] Comentários adicionados ✅

### Dados Persistidos
- [ ] base_conhecimento.json criado ✅
- [ ] 4 artigos salvos (3 originais + 1 novo) ✅
- [ ] Formato JSON válido ✅
- [ ] Encoding UTF-8 ✅

### Documentação
- [ ] RESUMO_FINAL.md criado ✅
- [ ] EVIDENCIAS_EXECUCAO.md criado ✅
- [ ] GUIA_ENTREGA.md criado ✅
- [ ] TEMPLATE_PDF.md criado ✅
- [ ] MANUAL_PRINTS.txt criado ✅

### Próximos Passos
- [ ] Capturar 13 prints de tela
- [ ] Organizar prints em sequência
- [ ] Criar documento PDF
- [ ] Nomear: Laboratorio_7_NomesDosAlunos.pdf
- [ ] Entregar até 23/04/2026

---

## 📊 ESTATÍSTICAS DO PROJETO

| Métrica | Valor |
|---------|-------|
| Linhas de Código | ~400 |
| Funções Implementadas | 8 |
| Tarefas Completadas | 4/4 ✅ |
| Critérios Atendidos | 4/4 ✅ |
| Arquivos Criados | 9 |
| Linhas de Documentação | ~2000 |
| Artigos na Base | 4 |
| Prints de Tela | 13 |

---

## 🚀 FLUXO DE ENTREGA

### Fase 1: Preparação (CONCLUÍDA ✅)
- ✅ Código desenvolvido
- ✅ Sistema testado
- ✅ Documentação criada
- ✅ Arquivos organizados

### Fase 2: Evidências (EM PROGRESSO 📸)
- ⏳ Capturar prints de tela
- ⏳ Organizar em sequência
- ⏳ Adicionar legendas

### Fase 3: PDF (A FAZER 📄)
- ⏳ Criar documento
- ⏳ Inserir prints
- ⏳ Verificar formatação
- ⏳ Nomear corretamente

### Fase 4: Entrega (A FAZER 📤)
- ⏳ Validar PDF
- ⏳ Entregar até 23/04/2026

---

## 💡 DICAS DE USO

### Para Iniciantes
1. Comece lendo: **RESUMO_FINAL.md**
2. Execute: `python lab7.py`
3. Siga: **MANUAL_PRINTS.txt**
4. Use template: **TEMPLATE_PDF.md**

### Para Aprofundamento
1. Estude: **lab7.py** (código-fonte)
2. Analise: **EVIDENCIAS_EXECUCAO.md**
3. Compreenda: arquitetura descrita em **GUIA_ENTREGA.md**

### Para Entrega Rápida
1. Use: **TEMPLATE_PDF.md** pronto
2. Adicione: prints capturados
3. Renomeie: `Laboratorio_7_NomesDosAlunos.pdf`
4. Entregue: até 23/04

---

## 🎓 CONCEITOS COBERTOS

✅ Arquitetura em Camadas
✅ Separação de Responsabilidades
✅ Persistência de Dados (JSON)
✅ List Comprehension (Python)
✅ Busca Case-Insensitive
✅ Interface Amigável
✅ Validação de Entrada
✅ Tratamento de Erros
✅ Sistema de Colaboração
✅ Documentação de Código

---

## 📞 RESUMO EXECUTIVO

**Laboratório 7 - Sistema de Gestão do Conhecimento (SGC)**

✅ **STATUS:** Código Completo + Documentação Pronta

**O que foi entregue:**
1. ✅ Código Python funcional (lab7.py)
2. ✅ Dados persistidos (base_conhecimento.json)
3. ✅ Documentação completa (5 arquivos .md)
4. ✅ Manual de captura (MANUAL_PRINTS.txt)
5. ✅ Template PDF pronto (TEMPLATE_PDF.md)

**Tarefas Implementadas:** 4/4 (100%)
- ✅ Tarefa 1: Busca (List Comprehension)
- ✅ Tarefa 2: Dashboard (Barras visuais)
- ✅ Tarefa 3: Persistência (JSON)
- ✅ Tarefa 4: Colaboração (Adicionar)

**Critérios Atendidos:** 4/4 (100%)
- ✅ Código sem erros
- ✅ Busca case-insensitive
- ✅ Dashboard legível
- ✅ Dados persistidos

**Próximo Passo:** Capturar prints e criar PDF

**Data Limite:** 23 de Abril de 2026

---

**Documentação Completa e Pronta para Entrega** ✨

*Criado em: 16 de Abril de 2026*
*Todos os arquivos testados e validados*
*Pronto para produção do PDF de entrega*

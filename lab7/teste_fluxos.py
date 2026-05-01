# Script de Teste - Gera múltiplos cenários para captura de prints
# Executar este script para testar todos os fluxos do sistema

import subprocess
import sys

print("=" * 80)
print("SCRIPT DE TESTE - SISTEMA SGC")
print("Este script simula interações com o sistema para captura de evidências")
print("=" * 80)

# Opção 1: Executar manualmente
print("\n✅ Para capturar prints de tela, execute:")
print("   python lab7.py")
print("\n📋 Siga este fluxo para capturas completas:")
print("""
   1. Inicie o programa: python lab7.py
   2. Print 1: Capture o Menu Principal
   3. Digite: 1 (Dashboard)
   4. Print 2: Capture o Dashboard de Popularidade
   5. Digite: 2 (Buscar)
   6. Digite: Azul (termo não existente)
   7. Print 3: Capture a busca sem resultado
   8. Digite: 3 (Adicionar)
   9. Digite: Configuração de Firewall (título)
   10. Digite: Aplicar regras de entrada no Windows Firewall... (conteúdo)
   11. Print 4: Capture a adição de novo conhecimento
   12. Print 5: Capture a confirmação de salvamento
   13. Digite: 2 (Buscar)
   14. Digite: Firewall
   15. Print 6: Capture a busca com resultado encontrado
   16. Digite: 2 (Buscar)
   17. Digite: VPN (para encontrar resultado existente)
   18. Print 7: Capture resultado de busca em conhecimento existente
   19. Digite: 1 (Dashboard)
   20. Print 8: Capture o novo dashboard com atualização
   21. Digite: 4 (Sair)
   22. Print 9: Capture a mensagem de saída
""")

print("\n📁 Arquivos gerados:")
print("   - lab7.py (código principal)")
print("   - base_conhecimento.json (dados persistidos)")
print("   - EVIDENCIAS_EXECUCAO.md (documentação)")
print("   - GUIA_ENTREGA.md (instruções de entrega)")

print("\n✨ Dicas para capturas:")
print("   - Use printscreen (PrtScn) ou Shift+PrtScn para seleção")
print("   - Ferramentas úteis: Snipping Tool (Windows) ou Print Screen Tool")
print("   - Inclua o caminho/prompt no primeiro print para contexto")
print("   - Mantenha resolução clara e legível")

print("\n" + "=" * 80)

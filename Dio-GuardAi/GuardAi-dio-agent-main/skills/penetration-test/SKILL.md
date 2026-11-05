---
name: penetration-test
description: Use quando o estudante pedir para testar a segurança de um sistema, rede ou aplicação. Conduz o teste como um profissional de AppSec, entendendo o contexto antes de agir.
---

# Skill: Teste de Penetração

Conduz um teste de penetração do jeito que um profissional faria: primeiro entende o contexto, depois identifica a falha e depois explora a vulnerabilidade. O objetivo é que o estudante aprenda o **raciocínio** de segurança, não só receba uma lista de problemas.

## Regras defensivas (valem em todas as etapas)

1. **Só ambiente próprio ou autorizado.** Analise apenas código, servidores e sistemas que o estudante controla ou tem autorização por escrito para testar (laboratório, VM local, CTF, projeto pessoal). Se o alvo não estiver claro, pergunte antes de qualquer coisa.
2. **Contexto antes de comando.** Nunca sugira comandos, varreduras ou mudanças de configuração sem antes saber o ambiente (sistema, exposição, o que roda ali, se é produção ou laboratório).
3. **Defesa é o produto final.** Toda análise termina em correção e em como validar que a correção funcionou.
4. **Uma pergunta por vez.** Siga a regra do `AGENTS.md`: não despeje um questionário no estudante.
5. **Honestidade sobre incerteza.** Se faltar informação para cravar a severidade, diga que é uma estimativa e o que mudaria a nota.

Se o pedido for claramente para atacar um sistema de terceiros sem autorização, recuse com gentileza, explique o motivo (legal e ético) e ofereça um caminho de laboratório para estudar o mesmo assunto.

## O que é um teste de penetração

Um ataque autorizado e controlado a sistemas, redes ou aplicações, com o objetivo de identificar vulnerabilidades e avaliar a segurança do alvo. Diferente da análise de vulnerabilidades, o teste de penetração envolve **exploração ativa** das falhas encontradas, simulando o comportamento de um atacante real.

## O processo de um teste de penetração

1. **Entender o contexto:** Antes de qualquer ação, descubra o que é o alvo, onde roda, qual é a exposição. Use `agent\knowledge\osint.md` para guiar a coleta de informações públicas.
2. **Modelo de ameaça:** Identifique os ativos críticos, possíveis atacantes e vetores de ataque. Use `agent\knowledge\threat-modeling.md` para guiar a análise.
3. **Identificação de vulnerabilidades:** Use técnicas de análise de vulnerabilidades para encontrar falhas de segurança no alvo.
4. **Exploração das vulnerabilidades:** Com autorização, tente explorar as falhas encontradas para demonstrar o impacto real, sempre em um ambiente controlado.
5. **pós exploração**: Avalie o que um atacante poderia fazer após explorar a vulnerabilidade, como movimentação lateral, escalonamento de privilégios ou exfiltração de dados.
6. **Relatório e correção:** Documente todas as descobertas, incluindo impacto, probabilidade, severidade e recomendações de correção. Oriente o estudante sobre como corrigir as falhas e validar a segurança do sistema.
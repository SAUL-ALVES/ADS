# Sistema Fuzzy: Avaliação de Qualidade de Produto

Este repositório contém o desenvolvimento de um mini-sistema de inferência fuzzy para a disciplina de Inteligência Artificial. O objetivo é simular o controle de qualidade em uma linha de produção.

## 👥 Equipe
* **Saul Alves Martins de Oliveira** - GitHub: [@SAUL-ALVES](https://github.com/SAUL-ALVES)


## 🎯 Tema Escolhido
**Tema B: Avaliação de Qualidade de Produto**

### Variáveis do Sistema
* **Entrada 1:** Variabilidade do Processo (medida de instabilidade na produção).
* **Entrada 2:** Grau de Defeitos (quantidade ou severidade de falhas encontradas).
* **Saída:** Qualidade Final (classificação do lote ou produto).

## 📝 Descrição do Problema
Em linhas de produção industrial, a classificação de qualidade de um produto nem sempre é uma decisão binária (aprovado/reprovado). Existem situações onde o produto apresenta pequenas variações dimensionais ou estéticas que não o tornam inutilizável, mas diminuem seu valor de mercado.

O problema consiste em determinar a **Qualidade Final** de um lote de produtos baseando-se em duas métricas incertas: a estabilidade da máquina durante a produção (variabilidade) e a severidade dos defeitos superficiais encontrados. Um sistema clássico ("crisp") teria dificuldade em classificar produtos "quase perfeitos" ou "levemente defeituosos", enquanto um sistema Fuzzy permite uma graduação suave entre categorias como "Premium", "Padrão" e "Refugo".

## 📅 Planejamento Inicial do Projeto

Abaixo estão as etapas definidas para o desenvolvimento do sistema:

### 1. Definir Variáveis Linguísticas
* **Entrada - Variabilidade:** Baixa, Média, Alta.
* **Entrada - Defeitos:** Nenhum, Leve, Grave.
* **Saída - Qualidade:** Premium, Aceitável, Rejeitado.

### 2. Esboçar Funções de Pertinência Iniciais
* Utilizaremos funções **Triangulares** e **Trapezoidais** para cobrir os universos de discurso.
* *Universo de discurso sugerido:* 0 a 10 (para facilitar a normalização).

### 3. Propor a Estrutura da Base de Regras
Serão criadas regras cobrindo as combinações lógicas, exemplo:
> *SE a Variabilidade é Baixa E o Grau de Defeitos é Nenhum ENTÃO a Qualidade é Premium.*

### 4. Definir Método de Inferência
* **Método:** Mamdani (Max-Min).
* Este método é intuitivo e amplamente utilizado em sistemas de controle de qualidade, permitindo capturar a expertise humana de forma direta.

### 5. Definir Método de Defuzzificação
* **Método:** Centróide (Centro de Gravidade).
* Garante uma saída contínua e suave, ideal para determinar uma nota final de qualidade.

### 6. Planejar Cenários de Teste
Para validar o sistema, serão utilizados três cenários principais:
1.  **Cenário Ideal:** Baixa variabilidade e zero defeitos.
2.  **Cenário Crítico:** Alta variabilidade e defeitos graves.
3.  **Cenário de Fronteira:** Variabilidade média com defeitos leves (para testar a suavidade da transição entre categorias).
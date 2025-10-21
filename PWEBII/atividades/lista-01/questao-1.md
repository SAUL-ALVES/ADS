# Tipagem de Dados em Linguagens de Programação e JavaScript

---

### **a) Tipagem Estática**

Uma **linguagem de tipagem estática** é aquela em que o tipo de cada variável  
é **definido e verificado em tempo de compilação**, antes da execução do programa.

**Verificação de tipos:** ocorre **no compilador**, que assegura que as operações entre tipos sejam válidas.

---

### **b) Benefícios da Tipagem Estática**

#### **Performance**
- O compilador pode **otimizar o código**, já que conhece os tipos de dados antecipadamente.  
- Reduz a necessidade de verificações em tempo de execução, tornando o programa **mais rápido e eficiente**.

#### **Segurança**
- Evita **erros de tipo** antes mesmo de rodar o código (como tentar multiplicar uma string com um número).  
- Facilita a **manutenção e refatoração**, pois o sistema de tipos age como uma **rede de segurança**.  
- Melhora a **previsibilidade** do comportamento do programa.

---

### **c) Tipagem Dinâmica**

Em linguagens de **tipagem dinâmica**, como **JavaScript** ou **Python**, o tipo das variáveis  
é **determinado em tempo de execução**, ou seja, durante a execução do programa, e **pode mudar a qualquer momento**.

#### **Desafios de Performance**
- O motor de execução precisa **descobrir o tipo constantemente** e adaptar as operações, o que consome mais tempo de CPU.  
- A falta de previsibilidade dificulta **otimizações pelo interpretador JIT (Just-In-Time)**.  
- Pode causar **erros sutis** apenas em tempo de execução, como **coerções inesperadas de tipo**.

---

### **d) Tipagem Forte x Tipagem Fraca**

- **Tipagem Forte:** Não permite operações entre tipos incompatíveis sem conversão explícita.  
- **Tipagem Fraca:** Permite **conversões automáticas (coerção)** entre tipos diferentes, às vezes de forma imprevisível.

---

### **e) Linguagens Híbridas e Inferência de Tipos**

Linguagens **híbridas** (como **TypeScript**, **Kotlin** ou **Swift**) permitem:

- **Tipagem estática opcional** (você pode ou não declarar os tipos).  
- **Inferência de tipos**, onde o compilador deduz automaticamente o tipo com base no valor inicial.

#### **Inferência de Tipos**
Evita declarações redundantes e mantém a **segurança da tipagem estática**.  
Portanto, combinam **flexibilidade da tipagem dinâmica** com **segurança da estática**.

---

### **f) Tipagem no JavaScript**

O **JavaScript** é uma linguagem de **tipagem dinâmica e fraca**.

- **Dinâmica:** o tipo das variáveis é definido **em tempo de execução** e pode mudar.  
- **Fraca:** permite **coerções automáticas de tipo**, o que pode causar resultados inesperados.

---

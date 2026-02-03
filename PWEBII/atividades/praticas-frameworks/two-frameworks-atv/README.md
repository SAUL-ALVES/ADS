# Atividade de Frameworks: React vs Angular

Este repositório contém a resolução da atividade prática desenvolvida em dois frameworks diferentes: **React** e **Angular**.

## 🚀 Como rodar os projetos

### Versão React
1. Entre na pasta `app-react-02`.
2. Instale as dependências: `npm install`.
3. Rode o projeto: `npm run dev`.

### Versão Angular
1. Entre na pasta `app-angular-01`.
2. Instale as dependências: `npm install`.
3. Rode o projeto: `ng serve`.

## 🆚 Semelhanças e Diferenças

Durante o desenvolvimento, notei as seguintes diferenças:

* **Estrutura de Arquivos:**
    * **React:** É mais flexível. A lógica e o HTML (JSX) ficam no mesmo arquivo.
    * **Angular:** É mais rígido e organizado. Ele separa nativamente o HTML, o CSS e o TypeScript em arquivos diferentes para cada componente.

* **Criação de Componentes:**
    * **React:** Criamos funções manualmente e retornamos JSX. Usamos `props` para passar dados.
    * **Angular:** Usamos o CLI (`ng generate component`) que cria os arquivos automaticamente. Usamos o decorador `@Input` para receber dados.

* **Roteamento:**
    * **React:** Tive que instalar uma biblioteca externa (`react-router-dom`).
    * **Angular:** O roteamento já vem embutido no framework e configurado pelo CLI.

* **Exibição de Dados:**
    * **React:** Usa chaves `{}` simples dentro do JSX.
    * **Angular:** Usa interpolação `{{}}` para texto e colchetes `[]` para vincular propriedades (como links e imagens).

## ⚠️ Dificuldades Encontradas
Minha maior dificuldade foi me acostumar com a rigidez do TypeScript no Angular (erros de tipagem e configurações do tsconfig) e entender como os arquivos se conectam, já que no React tudo parece estar "mais à mão" em um arquivo só.
## Questão 01

O que precisamos fazer para adicionar um script na seção `<head>` de uma página HTML e definir que ele só deve ser executado ao finalizar o carregamento da página?

> R: Para fazer isto, devemos adicionar o atributo `defer` junto do caminho do script dentro da tag `<script>`.
> Por exemplo `<script src="index.js" defer></script>`. O `defer` impede o mal funcionamento do navegador, pois ele irá baixar o script enquanto carrega o html, mas só vai executá-lo depois que todo o documento for analisado.

---

## Questão 02

Considere os métodos de seleção de elementos do DOM (Document Object Model) em JavaScript listados abaixo. Relacione cada método à definição correta.

I. `document.getElementById()`
II. `document.querySelector()`
III. `document.getElementsByTagName()`

A. Retorna todos os elementos do DOM que possuem o mesmo nome de tag especificado.
B. Retorna um único elemento do DOM com base no valor do atributo id.
C. Retorna o primeiro elemento do DOM que corresponde ao seletor CSS especificado.

> R: I - B; II - C; III - A

---

## Questão 03

Qual método foi utilizado para adicionar a classe `input-erro` ao campo de entrada no trecho acima? O que é esse atributo `classList`?

> R: Foi o método `add()`. `classList` é uma propriedade de qualquer elemento do DOM que retorna um objeto `DOMTokenList`, que representa todas as classes CSS aplicadas a este elemento. Em resumo: é uma propriedade que fornece acesso e controle sobre as classes CSS de um elemento do DOM.

---

## Questão 04

O que o método `createElement()` faz e que informação ele precisa receber como argumento?

> R: O método `createElement()` é usado para criar dinamicamente um novo elemento HTML via JavaScript. Ele precisa receber como argumento o nome da tag HTML que desejamos criar.

---

## Questão 05

Em JavaScript, ao manipular elementos do DOM, os atributos `innerText` e `innerHTML` são frequentemente utilizados. Qual das alternativas abaixo descreve corretamente a diferença entre esses dois atributos?

a — `innerText` somente exibe o conteúdo HTML do elemento, enquanto `innerHTML` somente exibe o texto visível ao usuário.
b — `innerText` retorna ou define apenas o texto visível ao usuário, enquanto `innerHTML` retorna ou define o conteúdo HTML do elemento, incluindo tags.
c — `innerText` é utilizado apenas para leitura, enquanto `innerHTML` pode ser utilizado tanto para leitura quanto para modificação do conteúdo do elemento.
d — Ambos os atributos são sinônimos e podem ser usados de forma intercambiável para manipular texto e HTML.

> R: B)

---

## Questão 06

O evento de clique foi definido de que forma para os elementos `span` e `btnExcluir` (qual atributo foi usado e o que precisamos passar para esse atributo)?

> R: O evento de clique foi definido por meio do atributo `onclick`, ao qual foi atribuída uma função que deve ser executada quando o usuário clicar no elemento.
> O atributo usado é `onclick`, o valor passado para ele é uma função, que será executada quando o clique ocorrer.

---

## Questão 07

Os manipuladores dos eventos de clique no botão de adicionar e pressionamento da tecla `enter` foram definidos de forma diferente agora, usando o método `addEventListener()`. Explique o funcionamento desse método e o que ele precisa receber como parâmetro.

> R: O método **addEventListener()** é utilizado para associar um evento a um elemento do DOM, de forma que uma função específica seja executada quando esse evento ocorrer. Ele precisa receber, obrigatoriamente, dois parâmetros: o primeiro é uma **string** que indica o **tipo de evento** a ser escutado (por exemplo, `"click"`, `"submit"`, `"keydown"`, etc.), e o segundo é uma **função** (chamada de callback) que contém o código a ser executado quando o evento acontecer. Diferente do uso direto do atributo `onclick`, o `addEventListener()` permite registrar vários ouvintes para o mesmo evento sem sobrescrever os anteriores, oferecendo maior flexibilidade e organização ao código. No exemplo apresentado, o evento `"submit"` é escutado no formulário, e a função passada impede o comportamento padrão de recarregar a página com `evento.preventDefault()`, executando em seguida a função `novaTarefa()`.
document.getElementById("promoForm").addEventListener("submit", function(e) {
    e.preventDefault();
  
    const medicamento = document.getElementById("medicamento").value.trim();
    const preco = parseFloat(document.getElementById("preco").value);
    const resultado = document.getElementById("resultado");
  
    if (medicamento === "" || isNaN(preco) || preco <= 0) {
      resultado.textContent = "Por favor, insira dados válidos.";
      resultado.style.color = "red";
      return;
    }
  
    const totalSemDesconto = preco * 2;
    const centavos = totalSemDesconto - Math.floor(totalSemDesconto);
    const totalComDesconto = totalSemDesconto - centavos;
  
    resultado.style.color = "#0077ff";
    resultado.innerHTML = `
      Promoção de <strong>${medicamento}</strong>!<br>
      Leve 2 por apenas <strong>R$ ${totalComDesconto.toFixed(2).replace(".", ",")}</strong>.
    `;
  
    this.reset();
  });
  
document.getElementById("superForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const produto = document.getElementById("produto").value.trim();
    const preco = parseFloat(document.getElementById("preco").value);
    const resultado = document.getElementById("resultado");
  
    if (produto === "" || isNaN(preco) || preco <= 0) {
      resultado.textContent = "Por favor, insira dados válidos.";
      resultado.style.color = "red";
      return;
    }
  
    
    const valorComDesconto = (2 * preco) + (0.5 * preco);
    const precoDesconto = (0.5 * preco);
  
    resultado.style.color = "#0077ff";
    resultado.innerHTML = `
      Promoção de <strong>${produto}</strong>!<br>
      Leve 3 e pague 2 por R$ ${(2 * preco).toFixed(2).replace('.', ',')} + 
      1 por R$ ${precoDesconto.toFixed(2).replace('.', ',')}<br><br>
      Total: <strong>R$ ${valorComDesconto.toFixed(2).replace('.', ',')}</strong>.
    `;
  
    this.reset();
  });
  
document.getElementById("lanForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const valor = parseFloat(document.getElementById("valor").value);
    const tempo = parseInt(document.getElementById("tempo").value);
    const resultado = document.getElementById("resultado");
  
    if (isNaN(valor) || valor <= 0 || isNaN(tempo) || tempo <= 0) {
      resultado.textContent = "Por favor, insira valores válidos.";
      resultado.style.color = "red";
      return;
    }
  
    
    const blocos = Math.ceil(tempo / 15);
    const total = blocos * valor;
  
    resultado.style.color = "#0077ff";
    resultado.innerHTML = `
      Tempo de uso: <strong>${tempo} minutos</strong><br>
      Total a pagar: <strong>R$ ${total.toFixed(2).replace(".", ",")}</strong>.
    `;
  
    this.reset();
  });
  
import { Link } from "react-router-dom";
import { useCart } from "../hooks/useCart";
import { formatPrice } from "../utils/formatPrice";
// Ajuste o caminho do componente Button se necessário
import Button from "../components/Button"; 
import "./Cart.css";

export default function Cart() {
  const { items, totalItems, totalPrice, updateQuantity, removeItem } = useCart();
  const hasItems = items.length > 0;

  return (
    <main className="cart-page">
      <h2>Carrinho de Compras</h2>

      {!hasItems && (
        <div className="cart-empty">
          <p>Seu carrinho está vazio.</p>
          <Link to='/'>
            <Button>Voltar para o catálogo</Button>
          </Link>
        </div>
      )}

      {hasItems && (
        <>
          <section className="cart-list">
            {items.map((item) => (
              <article key={item.id} className="cart-item">
                <div className="cart-item-info">
                  <img src={item.product.image} alt={item.product.title} />
                  <div className="cart-item-details">
                    <h3>{item.product.title}</h3>
                    <div className="cart-qty">
                      <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>-</button>
                      <span>{item.quantity}</span>
                      <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>
                    </div>
                    <button className="cart-remove" onClick={() => removeItem(item.id)}>
                      Remover
                    </button>
                  </div>
                </div>
                <div className="cart-item-price">
                  {formatPrice(item.product.price * item.quantity)}
                </div>
              </article>
            ))}
          </section>

          <section className="cart-summary">
            <div className="cart-summary-total">
              <span>Total ({totalItems} itens)</span>
              <strong>{formatPrice(totalPrice)}</strong>
            </div>
            <div className="cart-summary-actions">
              <Button onClick={() => alert("Pedido finalizado (simulação)!")}>
                Finalizar pedido
              </Button>
              <Link to='/' className="btn-secondary">
                <Button variant="secondary">Continuar comprando</Button>
              </Link>
            </div>
          </section>
        </>
      )}
    </main>
  );
}
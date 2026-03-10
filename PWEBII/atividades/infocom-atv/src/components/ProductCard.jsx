import "./ProductCard.css";
import { useNavigate } from "react-router-dom";
import { useCart } from "../hooks/useCart";

function ProductCard({ product, detailedView = false }) {
  const navigate = useNavigate();
  const { addItem } = useCart();

  const handleClick = () => {
    if (!detailedView) {
      navigate(`/products/${product.id}`);
    }
  };

  return (
    <div className='card' onClick={handleClick}>
      <img src={product.image} alt={product.title} />
      
      
      <button 
        className="btn-add"
        onClick={(e) => {
          e.stopPropagation(); 
          addItem(product);
        }}
      >
        Adicionar ao Carrinho
      </button>

      <div className='separator'></div>

      <div className='price'>
        R$ {product.price.toFixed(2).replace(".", ",")}
      </div>

      <h3>{product.title}</h3>

      {detailedView && (
        <>
          <p className="product-description">{product.description}</p>
          <span className="product-category">{product.category}</span>
        </>
      )}
    </div>
  );
}

export default ProductCard;
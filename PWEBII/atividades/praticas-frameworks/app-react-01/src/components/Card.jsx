import { Link } from "react-router-dom";
import "./Card.css";

const Card = ({ car }) => {
    return (
        <div className="card">
            {car.image && <img src={car.image} alt={car.title} className="card-img" />}
            <h2>{car.title}</h2>
            <ul>
                <li><span>Marca:</span> {car.brand}</li>
                <li><span>Ano:</span> {car.year}</li>
                <li><span>Preço:</span> R$ {car.price}</li>
            </ul>
            <Link to={`/anuncio/${car.id}`} className="btn-details">
                Ver Detalhes
            </Link>
        </div>
    );
};

export default Card;
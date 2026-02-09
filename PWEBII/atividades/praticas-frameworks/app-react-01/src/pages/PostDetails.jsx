import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import "./PostDetails.css";

const PostDetails = () => {
  const { id } = useParams();
  const [car, setCar] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getCar = async () => {
      try {
        const res = await fetch(`http://localhost:3000/cars/${id}`);
        const data = await res.json();
        setCar(data);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
      }
    };
    getCar();
  }, [id]);

  if (loading) return <p>Carregando...</p>;
  if (!car) return <p>Anúncio não encontrado.</p>;

  return (
    <div className="details-container">
        {car.image && <img src={car.image} alt={car.title} className="details-img" />}
        <div className="details-info">
            <h1>{car.title}</h1>
            <h3>R$ {car.price}</h3>
            <p>{car.description}</p>
            <p><strong>Contato:</strong> {car.contact}</p>
            <Link to="/" className="back-btn">Voltar</Link>
        </div>
    </div>
  );
};

export default PostDetails;
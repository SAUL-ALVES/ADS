import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./NewPost.css";

const NewPost = () => {
  const navigate = useNavigate();
  
  const [formData, setFormData] = useState({
    title: "", brand: "", model: "", year: "", 
    price: "", km: "", image: "", description: "", contact: ""
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    
    const rawPrice = formData.price.replace(/\./g, "").replace(",", ".");
    
    
    const finalData = {
        ...formData,
        price: parseFloat(rawPrice) 
    };

    
    await fetch("http://localhost:3000/cars", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(finalData), 
    });

    alert("Anúncio cadastrado com sucesso!");
    navigate("/");
  };

  return (
    <div className="form-container">
      <h2>Cadastrar Novo Veículo</h2>
      <form onSubmit={handleSubmit}>
        <input name="title" placeholder="Título do Anúncio" onChange={handleChange} required />
        <input name="brand" placeholder="Marca" onChange={handleChange} />
        <input name="model" placeholder="Modelo" onChange={handleChange} />
        <input name="year" type="number" placeholder="Ano" onChange={handleChange} />
        
        
        <input 
            name="price" 
            type="text" 
            placeholder="Preço (ex: 12.500)" 
            onChange={handleChange} 
            required 
        />
        
        <input name="km" type="number" placeholder="Quilometragem" onChange={handleChange} />
        <input name="image" placeholder="URL da Imagem" onChange={handleChange} />
        <input name="contact" placeholder="Contato (Tel/Email)" onChange={handleChange} required />
        <textarea name="description" placeholder="Descrição detalhada" onChange={handleChange}></textarea>
        
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default NewPost;
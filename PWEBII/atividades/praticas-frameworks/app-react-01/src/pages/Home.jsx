import { useState, useEffect } from "react";
import SearchBar from "../components/SearchBar";
import Card from "../components/Card";
import "./Home.css";

const Home = () => {
  const [allCars, setAllCars] = useState([]); 
  const [filteredCars, setFilteredCars] = useState([]); 

  
  useEffect(() => {
    const fetchCars = async () => {
      try {
        const res = await fetch("http://localhost:3000/cars");
        const data = await res.json();
        setAllCars(data);     
        setFilteredCars(data); 
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    };
    fetchCars();
  }, []);

  
  const handleSearch = (searchTerm) => {
    
    const query = searchTerm.toLowerCase();

    
    const results = allCars.filter((car) => 
      car.title.toLowerCase().includes(query) || 
      car.model.toLowerCase().includes(query) ||
      car.brand.toLowerCase().includes(query)
    );

    
    setFilteredCars(results);
  };

  return (
    <div className="home-container">
      <h1 className="home-title">Anúncios Recentes</h1>
      
      <div className="search-wrapper">
        
        <SearchBar handleSearch={handleSearch} />
      </div>

      <div className="card-container">
        {filteredCars.length > 0 ? (
          filteredCars.map((car) => <Card key={car.id} car={car} />)
        ) : (
          <p className="no-results">Nenhum veículo encontrado.</p>
        )}
      </div>
    </div>
  );
};

export default Home;
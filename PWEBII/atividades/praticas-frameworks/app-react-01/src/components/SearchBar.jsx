import "./SearchBar.css";

const SearchBar = ({ handleSearch }) => {
    return (
        <div className="search-container">
            <input 
                type="text" 
                placeholder="Pesquise por modelo, marca ou título..."
                onChange={(e) => handleSearch(e.target.value)} 
            />
            
        </div>
    );
};

export default SearchBar;
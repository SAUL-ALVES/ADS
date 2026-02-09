import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import NewPost from "./pages/NewPost";
import PostDetails from "./pages/PostDetails";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cadastrar" element={<NewPost />} />
          <Route path="/anuncio/:id" element={<PostDetails />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
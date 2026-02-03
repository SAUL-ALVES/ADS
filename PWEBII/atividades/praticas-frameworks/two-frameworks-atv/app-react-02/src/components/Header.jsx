import { Link } from 'react-router-dom';
import './Header.css'; 

function Header() {
  return (
    <header className="blue-header">
      <nav>
        
        <Link to="/">Blog</Link>
        <Link to="/sobre">Sobre</Link>
        <Link to="/descricao">Descrição</Link>
      </nav>

      <div className="profile-container">
        <img 
          src="https://media.licdn.com/dms/image/v2/D4E03AQEFM8BVtDxSvw/profile-displayphoto-shrink_800_800/B4EZbVpxNfHIAg-/0/1747341220856?e=1771459200&v=beta&t=_g_xOq5U2D2nSLejFAcn149HEyJSV5LPY5hI5SbN_Lk" 
          alt="Perfil" 
          className="avatar"
        />
        <h1>Saul Alves</h1>
        <p className="bio">
            Sou estudante de ADS, desenvolvedor Full-Stack apaixonado por React e frameworks semelhantes.
        </p>
      </div>
    </header>
  );
}

export default Header;
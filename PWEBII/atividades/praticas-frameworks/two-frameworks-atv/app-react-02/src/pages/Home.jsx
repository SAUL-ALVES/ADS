import Header from '../components/Header';
import Post from '../components/Post';

function Home() {
  return (
    <>
      <Header /> 
      
      <main style={{ maxWidth: '800px', margin: '40px auto', padding: '0 20px' }}>
        <h2 style={{ marginBottom: '30px', color: '#333' }}>Últimas do blog</h2>
        
        
        <Post 
          title="5 dicas para sua carreira profissional" 
          description="Confira algumas dicas que podem ajudar a alavancar sua carreira como desenvolvedor front-end."
          link="https://alexmngn.medium.com/level-up-your-career-as-a-developer-2ec42c208b82" 
        />

        
        <Post 
          title="Entendendo o React Router" 
          description="Como navegar entre páginas sem recarregar o navegador."
          link="https://reactrouter.com/"
        />

        
        <Post 
          title="Diferenças entre Angular e React" 
          description="Uma breve comparação para a atividade da faculdade."
          link="https://www.freecodecamp.org/portuguese/news/angular-x-react-qual-deles-escolher-para-a-sua-aplicacao/"
        />
        
        <a href="#" style={{ color: '#2c4a7c', fontWeight: 'bold', textDecoration: 'none' }}>Ver tudo</a>
      </main>
    </>
  );
}

export default Home;
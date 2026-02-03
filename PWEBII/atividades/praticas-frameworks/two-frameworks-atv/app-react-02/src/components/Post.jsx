function Post({ title, description, link }) {
    return (
      <div style={{ marginBottom: '20px' }}>
        
        <a 
          href={link} 
          target="_blank" 
          rel="https://alexmngn.medium.com/level-up-your-career-as-a-developer-2ec42c208b82"
          style={{ textDecoration: 'none' }} 
        >
          <h3 style={{ color: '#5b7bb2', cursor: 'pointer' }}>
            {title}
          </h3>
        </a>
  
        <p style={{ fontSize: '12px', color: '#666', fontStyle: 'italic' }}>
          {description}
        </p>
      </div>
    );
  }
  
  export default Post;
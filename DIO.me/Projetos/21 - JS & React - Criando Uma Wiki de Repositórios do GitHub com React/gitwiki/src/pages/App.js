import { useState } from 'react';
import githubLogo from '../assets/github.png';
import Input from '../components/Input';
import ItemList from '../components/ItemList';
import Button from '../components/Button';
import { Container } from './styles';
import { api } from '../services/api';


function App() {
  const [repos, setRepos] = useState([]);
  const [currentRepo, setCurrentRepo] = useState('');

  const handleSearchRepo = async () => {
	  try {
      const { data } = await api.get(`repos/${currentRepo}`);
    
      if (data.id) {
      const exists = repos.find(repo => repo.id === data.id);
    
      if (!exists) {
        setRepos(prev => [...prev, data]);
        setCurrentRepo(''); // Clear the input after adding
      } else {
        alert('Repositório já está listado!');
      }
    
      return;
      }
      alert('Repositório não encontrado!');
    } catch (error) {
      alert('Erro ao buscar o repositório!');
    }
  };

  const handleRemoveRepo = (id) => {
    setRepos(repos.filter((repo) => repo.id !== id))
  }
  

  return (
	<Container>
	  <img src={githubLogo} width={72} height={72} alt='GitHub Logo'/>
	  <Input value={currentRepo} onChange={(event) => setCurrentRepo(event.target.value)}/>
	  <Button onClick={handleSearchRepo} />
	  {repos.map(repo => <ItemList handleRemoveRepo={handleRemoveRepo} repo={repo}/>)}
	</Container>
  );
}

export default App;

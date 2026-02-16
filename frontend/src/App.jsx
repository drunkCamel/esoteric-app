import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('');
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch from FastAPI backend
    fetch('http://localhost:8000/')
      .then(response => response.json())
      .then(data => {
        setMessage(data.message);
      })
      .catch(error => console.error('Error fetching message:', error));

    fetch('http://localhost:8000/api/items')
      .then(response => response.json())
      .then(data => {
        setItems(data.items);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching items:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>Full Stack App - React + FastAPI</h1>
      <h2>{message}</h2>
      
      <div>
        <h3>Items from Backend:</h3>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <ul>
            {items.map(item => (
              <li key={item.id}>{item.name}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}

export default App

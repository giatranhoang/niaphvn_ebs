import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);

  // API endpoint - use localhost:5002 for external access, backend:5000 for Docker internal
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5002';

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/items`);
      setItems(response.data);
    } catch (error) {
      console.error('Error fetching items:', error);
    }
  };

  const handleFetch = async () => {
    setLoading(true);
    try {
      await axios.post(`${API_URL}/api/fetch`);
      fetchItems(); // Refresh items after fetch
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🦠 Nipah Virus – Vietnam EBS Monitoring Dashboard</h1>
        <p>Early-Based Surveillance from Vietnam news & social media</p>
        <button onClick={handleFetch} disabled={loading}>
          {loading ? 'Fetching...' : 'Fetch Latest Data'}
        </button>
      </header>
      <main>
        <table>
          <thead>
            <tr>
              <th>Source</th>
              <th>Title</th>
              <th>Published</th>
              <th>URL</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item, index) => (
              <tr key={index}>
                <td>{item.source}</td>
                <td>{item.title}</td>
                <td>{item.published ? new Date(item.published).toLocaleDateString() : 'N/A'}</td>
                <td><a href={item.url} target="_blank" rel="noopener noreferrer">Link</a></td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </div>
  );
}

export default App;
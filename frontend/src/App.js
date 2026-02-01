import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);

  // API endpoint - use localhost:5002 for external access, backend:5000 for Docker internal
//   const API_URL = '/api';

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await axios.get('/api/items');
      setItems(response.data);
    } catch (error) {
      console.error('Error fetching items:', error);
    }
  };

  const handleFetch = async () => {
    setLoading(true);
    try {
      await axios.post('/api/fetch');
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
        <p>Event-Based Surveillance from Vietnam News & Social media</p>
        <button className="btn btn-primary" onClick={handleFetch} disabled={loading}>
          {loading ? 'Fetching...' : 'Fetch Latest Data'}
        </button>
      </header>
      <main>
        <div class="table-responsive">
          <table class="table table-striped table-hover align-middle">
            <thead class="table-light">
              <tr>
                <th class="w-10">Source</th>
                <th class="w-30">Title</th>
                <th class="w-55">Summary</th>
                <th class="w-5">Published</th>
              </tr>
            </thead>
            <tbody>
              {items.map((item, index) => (
                <tr key={index}>
                  <td>{item.source}</td>
                  <td><a href={item.url} target="_blank" rel="noopener noreferrer">{item.title}</a></td>
                  <td>{item.text}</td>
                  <td>{item.published ? new Date(item.published).toLocaleDateString() : 'N/A'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}

export default App;
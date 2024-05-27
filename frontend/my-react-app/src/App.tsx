import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState('');

  useEffect(() => {
    // Define your Django backend URL
    const backendUrl = 'http://127.0.0.1:8000/api/members/';

    // Make a GET request to your Django backend
    axios.get(backendUrl)
      .then(response => {
        setData(response.data.message);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <>
      <h1>Data from Django Backend:</h1>
      <p>{data}</p>
    </>
  );
}

export default App;

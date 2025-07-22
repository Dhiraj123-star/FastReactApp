import { useEffect, useState } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/api/items')
      .then((res) => res.json())
      .then((data) => setItems(data));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch(`http://localhost:8000/api/items?name=${name}`, { method: 'POST' });
    const res = await fetch('http://localhost:8000/api/items');
    const data = await res.json();
    setItems(data);
    setName('');
  };

  return (
    <div>
      <h1>Item List</h1>
      <form onSubmit={handleSubmit}>
        <input value={name} onChange={(e) => setName(e.target.value)} />
        <button type="submit">Add Item</button>
      </form>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

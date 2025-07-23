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
    if (!name.trim()) return;

    await fetch('http://localhost:8000/api/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name.trim() }),
    });

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
        <button type="submit" disabled={!name.trim()}>Add Item</button>
      </form>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name || '(blank name)'}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

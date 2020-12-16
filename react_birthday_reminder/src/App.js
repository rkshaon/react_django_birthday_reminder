import React, { useState, useEffect } from 'react';
import List from './List';

function App() {
  const [people, setPeople] = useState([]);

  useEffect( () => {
    getPersons();
    console.log('we are fetching data');
  }, []);

  const getPersons = async () => {
    const response = await fetch(`http://127.0.0.1:8000/birthday-api/person-list/`);
    const data = await response.json();
    console.log(data);
    setPeople(data);
    console.log('Get Person Method');
  }
  return (
    <main>
      <section className="container">
        <h3>{people.length} birthdays today</h3>
        <List people={people} />
        <button onClick={()=>{ setPeople([]) }}>Clear All</button>
      </section>
    </main>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentDate, setCurrentDate] = useState(0);
  const [currentTime, setCurrentTime] = useState(1);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      const dateTime = new Date(data.time * 1000);
      setCurrentDate( dateTime.toDateString() );
      setCurrentTime( dateTime.toTimeString() );
    });
    // If the port is 3000
    const port = window.location.host.split(':')[1];
    if (port === '3000') {
      // We're running on the react test server
      document.title = 'React testing';
    }
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Heroku deployment test
        </p>
        <p>Page was loaded on:</p>
        <p>{currentDate} at {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  )
}

function A2() {

  const [message, setMessage] = useState(0);

  useEffect(() => {
    fetch('/api').then(res => res.json()).then(data => {
      setMessage(data.msg);
    });
  }, []);
    
  return(
    <div className="App">
      <header className="App-header">
        <p>{message}</p>
      </header>
    </div>
  )
}

export { App, A2 };

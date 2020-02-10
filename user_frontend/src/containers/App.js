import React from 'react';
// import logo from './logo.svg';
import '../App.css';
import MainContainer from './MainContainer';
import Sidebar from './Sidebar'

function App() {
  return (
    <div className="App row">
      <Sidebar/>
      <MainContainer/>
    </div>
  );
}

export default App;

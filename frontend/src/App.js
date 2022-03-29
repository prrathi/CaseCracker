import './App.css';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Transcript from './components/pages/Transcript';
import About from './components/pages/About';
function App() {
  return (
    <div className="App">
      <Router>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home />}></Route> 
        <Route path='/Transcripts' element={<Transcript />}></Route> 
        
        <Route path='/About' element={<About />}></Route> 
      </Routes>
      </Router>

    </div>
  );
}

export default App;

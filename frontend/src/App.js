import './App.css';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Transcript from './components/pages/Transcript';
import QuizFront from './components/pages/QuizFront';
import About from './components/pages/About';
import Justices from './components/pages/Justices';
import mySurvey from './components/pages/surveys/surveyTypeone';
import SurveyPage from './components/pages/SurveyPage';
function App() {
  return (
    <div className="App">
      <Router>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home />}></Route> 
        <Route path='/Transcripts' element={<Transcript />}></Route> 
        
        <Route path='/About' element={<About />}></Route> 
        <Route path='/QuizFront' element={<QuizFront />}></Route> 
        <Route path='/Justices' element={<Justices />}></Route> 
        <Route path='/Survey' element={<SurveyPage />}></Route>
      </Routes>
      </Router>

    </div>
  );
}

export default App;

import './App.css';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Transcript from './components/pages/Transcript';
import QuizFront from './components/pages/QuizFront';
import About from './components/pages/About';
import Justices from './components/pages/Justices';
import JustLeans from './components/pages/JustLeans';
import mySurvey from './components/pages/surveys/surveyTypeone';
import SurveyPage from './components/pages/SurveyPage';
import SurveyResult from './components/pages/SurveyResults';

// Main Application 
function App() {
  return (
    <div className="App">
      <Router>
      <Navbar />
      {/* This defines the Routes for each page */}
      <Routes>
        <Route path='/' element={<Home />}></Route> 
        <Route path='/Transcripts' element={<Transcript />}></Route> 
        <Route path='/About' element={<About />}></Route> 
        <Route path='/QuiZFront' element={<QuizFront />}></Route> 
        <Route path='/Justices' element={<Justices/>}></Route> 
        <Route path='/JustLeans' element={<JustLeans/>}></Route> 
        <Route path='/Survey' element={<SurveyPage />}></Route>
        <Route path='/SurveyResults' element={<SurveyResult />}></Route>
      </Routes>
      </Router>

    </div>
  );
}

export default App;

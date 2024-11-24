import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/HomePage';
import TeamDetails from './pages/TeamDetails';
import PlayersPage from './pages/Players';
import Teams from './pages/Teams';
import Matches from './pages/Matches';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/team/:teamId" element={<TeamDetails />} />
        <Route path="/players" element={<PlayersPage />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/matches" element={<Matches />} />
      </Routes>
    </Router>
  );
}

export default App;
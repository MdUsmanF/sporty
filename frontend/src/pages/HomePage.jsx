import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Home() {
  const [teams, setTeams] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/teams')
      .then(response => setTeams(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleTeamClick = (teamId) => {
    navigate(`/team/${teamId}`);
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Teams</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {teams.map(team => (
          <div
            key={team.id}
            className="p-4 border rounded-lg shadow hover:shadow-lg transition cursor-pointer"
            onClick={() => handleTeamClick(team.id)}
          >
            <h3 className="text-xl font-semibold">{team.name}</h3>
            <p className="text-gray-600">Country: {team.country}</p>
            <p className="text-gray-600">Founded: {team.founded}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
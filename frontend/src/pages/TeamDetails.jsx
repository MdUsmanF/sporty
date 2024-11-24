import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function TeamDetails() {
  const { teamId } = useParams();
  const [team, setTeam] = useState(null);
  const [players, setPlayers] = useState([]);
  const [competitions, setCompetitions] = useState([]);
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    const fetchTeamDetails = async () => {
      try {
        // Fetching all teams and find the current team
        const teamsResponse = await axios.get('http://127.0.0.1:5000/api/teams');
        const currentTeam = teamsResponse.data.find(t => t.id === parseInt(teamId));
        setTeam(currentTeam);

        // Fetching team players
        const playersResponse = await axios.get(`http://127.0.0.1:5000/api/teams/${teamId}/players`);
        setPlayers(playersResponse.data);

        // Fetching competitions
        const competitionsResponse = await axios.get('http://127.0.0.1:5000/api/competitions');
        setCompetitions(competitionsResponse.data);

        // Fetching matches for the specific team
        const matchesResponse = await axios.get(`http://127.0.0.1:5000/api/matches?team_id=${teamId}`);
        setMatches(matchesResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchTeamDetails();
  }, [teamId]);

  return (
    <div className="container mx-auto p-6 space-y-8">
      {/* Team Title */}
      <div className="bg-gradient-to-r from-blue-600 to-blue-800 rounded-lg shadow-lg p-6">
        <h1 className="text-3xl font-bold text-white">
          {team?.name || 'Loading team...'}
        </h1>
        <p className="text-white mt-2 text-lg">
        Country: {team?.country} | Founded: {team?.founded} | Home Ground: {team?.home_area}
        </p>
      </div>

      {/* Players */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">Squad List</h2>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Name
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Position
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Age
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Nationality
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {players.length > 0 ? (
                players.map(player => (
                  <tr key={player.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      {player.name}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {player.position}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {player.age}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {player.nationality}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" className="px-6 py-4 text-center text-gray-500">
                    No players available
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Upcoming Matches */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">
          Matches for {team?.name}
        </h2>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Date
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Home Team
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Away Team
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Competition
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Venue
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Status
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {matches.length > 0 ? (
                matches.map(match => (
                  <tr key={match.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                      {new Date(match.date).toLocaleDateString(undefined, {
                        weekday: 'long',
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric'
                      })}
                    </td>
                    <td className={`px-6 py-4 whitespace-nowrap text-sm font-medium ${
                      match.home_team === team?.name ? 'text-blue-600' : 'text-gray-900'
                    }`}>
                      {match.home_team}
                    </td>
                    <td className={`px-6 py-4 whitespace-nowrap text-sm font-medium ${
                      match.away_team === team?.name ? 'text-blue-600' : 'text-gray-900'
                    }`}>
                      {match.away_team}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {match.competition}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {match.area}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {match.status}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" className="px-6 py-4 text-center text-gray-500">
                    No matches scheduled
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Competitions */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">Competitions</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {competitions.map(comp => (
            <div 
              key={comp.id} 
              className="bg-gray-50 rounded-lg p-4 hover:bg-gray-100 transition duration-150"
            >
              <h4 className="font-semibold text-lg text-gray-800">{comp.name}</h4>
              <p className="text-gray-600 text-sm mt-1">
                {comp.type} • {comp.country}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default TeamDetails;
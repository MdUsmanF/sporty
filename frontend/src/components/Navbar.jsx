import React, { useState } from "react";

const Navbar = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="bg-blue-600 text-white shadow-md">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <div className="text-2xl font-bold">Sporty</div>

        <div className="hidden md:flex items-center space-x-8">
          <a href="/players" className="hover:text-gray-300 text-lg">
            Players
          </a>
          <a href="/teams" className="hover:text-gray-300 text-lg">
            Teams
          </a>
          <a href="/matches" className="hover:text-gray-300 text-lg">
            Matches
          </a>
        </div>

        {/* Mobile View Icon */}
        <button
          className="md:hidden text-white focus:outline-none"
          onClick={toggleMenu}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d={isMobileMenuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"}
            />
          </svg>
        </button>
      </div>

      {/* Mobile Menu Options*/}
      {isMobileMenuOpen && (
        <div className="md:hidden bg-blue-700">
          <div className="px-4 py-2 space-y-2">
            <a href="#players" className="block text-white hover:text-gray-300">
              Players
            </a>
            <a href="#teams" className="block text-white hover:text-gray-300">
              Teams
            </a>
            <a href="#matches" className="block text-white hover:text-gray-300">
              Matches
            </a>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
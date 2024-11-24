# Football Management System

A full-stack application for managing football teams, matches, and competitions.

## Tech Stack

- Backend: Python + Flask
- Frontend: React + TailwindCSS
- Database: SQLite3

## Prerequisites

- Python 3.8+
- Node.js 16+

## Project Setup

### Backend Setup

1. Create and activate virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python run.py
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start development server:
```bash
npm run dev
```

### Docker Setup

1. Build and run all services:
```bash
docker-compose up --build
```

## API Documentation

The API documentation is available at `http://localhost:5000/api/docs` when running the backend server.

## Running Tests

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Linting

### Backend Linting
```bash
cd backend
flake8
```

### Frontend Linting
```bash
cd frontend
npm run lint
```

## Project Structure

- `backend/`: Contains Flask application
  - `app/`: Application code
  - `tests/`: Test files
  - `requirements.txt`: Python dependencies
  
- `frontend/`: Contains React application
  - `src/`: Source code
  - `public/`: Static files
  - `components/`: Reusable React components
  - `pages/`: Page components

## Features

- View all football teams
- View player details
- Track matches and competitions
- Filter matches by team, area, and date
- View upcoming matches
- View match details and results

## Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=sqlite:///football.db
```

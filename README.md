# Sporty

A full-stack web application built with React and Flask.

## 🚀 Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Node.js
- Docker

### Backend
- Flask (Python)
- Docker

## 📁 Project Structure
```
sporty/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── node_modules/
│   ├── Dockerfile
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
├── backend/
│   ├── app/
│   ├── instance/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── config.py
│   └── run.py
└── docker-compose.yml
```

## 🛠️ Setup and Installation

### With Docker
1. Clone the repository:
```bash
git clone https://github.com/MdUsmanF/sporty.git
cd sporty
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

### Without Docker

#### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

#### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Flask server
# On Windows:
set FLASK_APP=run.py
set FLASK_ENV=development
flask run

# On macOS/Linux:
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

## 🌐 Accessing the Application

- Frontend: http://localhost:5173
- Backend API: http://localhost:5000

## 🔧 Development

### Frontend Development Commands
```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint
```

### Backend Development Commands
```bash
# Run Flask development server
python run.py

# Run with debug mode
flask run --debug

# Run with specific host/port
flask run --host=0.0.0.0 --port=5000
```

## 🐳 Docker Commands

Build and start containers:
```bash
docker-compose up --build
```

Stop containers:
```bash
docker-compose down
```

View logs:
```bash
docker-compose logs
```

Other useful Docker commands:
```bash
# Remove all containers and volumes
docker-compose down -v

# View running containers
docker ps

# Enter container shell
docker exec -it sporty-frontend-1 sh  # for frontend
docker exec -it sporty-backend-1 sh   # for backend

# View container logs
docker-compose logs -f frontend  # frontend logs
docker-compose logs -f backend   # backend logs
```

## 🔍 Troubleshooting

### Frontend Issues
- If modules are missing, try removing `node_modules` and running `npm install` again
- Clear browser cache if styles are not updating
- Check console for error messages
- Ensure Vite config is properly set up for your environment

### Backend Issues
- Verify virtual environment is activated
- Check Flask debug output for error messages
- Ensure all dependencies are installed
- Verify environment variables are set correctly

## 👥 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request
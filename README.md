# Nipah EBS Monitor - Fullstack

A fullstack application for monitoring Nipah virus early-based surveillance from Vietnam news sources.

## Architecture

- **Frontend**: React app displaying the dashboard
- **Backend**: Flask API handling data fetching and storage
- **Database**: SQLite

## Setup

1. Ensure Docker and Docker Compose are installed.

2. Clone or navigate to the project directory.

3. Run `docker-compose up --build` to start the services.

4. Access the frontend at http://localhost:3000

5. The backend API is at http://localhost:5000

## API Endpoints

- GET /api/items: Retrieve all Nipah-related items
- POST /api/fetch: Trigger fetching of latest data from RSS sources

## Development

For local development without Docker:

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

Update the API URLs in App.js to localhost if running locally.
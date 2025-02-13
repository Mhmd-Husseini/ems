# Employee Management System (EMS)
A full-stack employee management system with React frontend and Django backend.


## Project Structure
ems/
├── frontend/ # React application
└── backend/ # Django application

## Tech Stack
- Frontend:
  - React
  - React Router
  - Vite
- Backend:
  - Django
  - Django REST Framework
  - SQLite (database)


## Features
- Create new employees
- View employee details
- Update employee information
- Upload employee documents (photo, CV, ID)


## Backend Setup
1. Navigate to the backend directory:
cd backend
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```
(this will also seed the database with some data)

5. Start the development server:
```bash
python manage.py runserver
```

The backend server will run at `http://localhost:8000`


## Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```
2. Install dependencies:
```bash
npm install
```
3. Start the development server:
```bash
npm run dev
```

The frontend application will run at `http://localhost:5173`


## API Endpoints
- `GET /api/employees/{id}` - Get employee details
- `POST /api/employees/` - Create new employee
- `PUT /api/employees/{id}/` - Update employee details

- `GET /api/timesheets/` - Get all timesheets
- `POST /api/timesheets/` - Create new timesheet
- `PUT /api/timesheets/{id}/` - Update timesheet details





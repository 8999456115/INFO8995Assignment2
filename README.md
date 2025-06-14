Advance Containers Assignment (INFO8995Assignment2)
📦 Overview
This assignment demonstrates a containerized web application using Flask and PostgreSQL, orchestrated with Docker Compose. It includes:

A simple REST API to manage user data (POST /user, GET /user/<id>)

Persistent PostgreSQL database

Scalable Flask web service with Docker

Logging with Docker volumes

🛠️ Technologies Used
Python 3.10 (Flask)

PostgreSQL 15

Docker & Docker Compose

GitHub Codespaces (Optional Cloud IDE)

⚙️ Project Structure
bash
Copy
Edit
.
├── app/
│   ├── main.py              # Flask API logic
│   ├── db.py                # DB connection and helper functions
│   ├── requirements.txt     # Flask & psycopg2 packages
├── init.sql                 # SQL script to initialize users table
├── Dockerfile               # Image build for Flask app
├── docker-compose.yml       # Orchestration file
└── README.md                # You're here!
🚀 How to Run
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/8999456115/INFO8995Assignment2.git
cd INFO8995Assignment2
2. Run in GitHub Codespaces or locally
bash
Copy
Edit
docker-compose down -v
docker-compose up --build --scale web=1
✅ Make sure ports: ["5000:5000"] is enabled in docker-compose.yml for browser access.

🧪 API Endpoints
▶️ POST /user
Creates a new user.

Example:

bash
Copy
Edit
curl -X POST http://localhost:5000/user \
     -H "Content-Type: application/json" \
     -d '{"first_name":"Sahil","last_name":"Sorathiya"}'
📥 GET /user/<id>
Retrieves user by ID.

Example:

bash
Copy
Edit
curl http://localhost:5000/user/20
Expected output:

json
Copy
Edit
{"id": 20, "first_name": "Sahil", "last_name": "Sorathiya"}
🔐 Security Best Practices Followed
Runs Flask as non-root user in container (appuser)

Uses Docker volumes to persist database and logs

Secrets handled via environment variables

Minimally scoped Dockerfile using python:3.10-slim

🔄 Scaling (Bonus)
You can run multiple replicas using:

bash
Copy
Edit
docker-compose up --build --scale web=3
⚠️ Comment out the ports section before scaling replicas.

📂 Volumes
logs: Stores Flask app logs from /app/logs

db-data: Stores PostgreSQL data

👨‍💻 Author
Sahil Sorathiya — INFO8995 Advanced Containers Assignment — June 2025


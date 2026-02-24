# 🦸‍♂️ Math Hero - Kids Learning App

Interactive Django web application where kids practice math, earn stars, and level up their heroes.

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repository-link>
   cd math_is_fun
   
2.  **Create a virtual environment:

python -m venv venv
venv\Scripts\activate  # Windows

3. **Install requirements:

pip install -r requirements.txt

4. **Run the server:

python manage.py runserver

📂 Structure Overview
players/: Handles player profiles and the Score model (stars tracking).

exercises/: Contains game logic for Addition, Subtraction, Multiplication, and Division.

progress/: A personal dashboard showing solved tasks and total points.

templates/: All HTML files with a kid-friendly, colorful UI.

✨ Features
CRUD operations for Hero profiles.

Automatic star calculation based on correct answers.

Smart math logic (no negative results in subtraction).

Session-based player tracking.
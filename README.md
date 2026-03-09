# ACEest Fitness & Gym DevOps Project

## Technologies
- Flask
- Docker
- GitHub Actions
- Jenkins
- Pytest

## Run Locally
pip install -r requirements.txt
python app.py

## Run Tests
pytest

## Docker
docker build -t aceest-app .
docker run -p 5000:5000 aceest-app

## CI/CD
GitHub Actions runs tests and builds Docker image on every push.
Jenkins pulls code from GitHub and performs build validation.
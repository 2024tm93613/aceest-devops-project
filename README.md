# 🏋️ ACEest Fitness & Gym — DevOps CI/CD Project

## 📌 Project Overview

This project demonstrates the implementation of a **complete DevOps lifecycle** for a Flask-based web application designed for **ACEest Fitness & Gym**.

It covers:

* Application Development
* Version Control (Git & GitHub)
* Unit Testing (Pytest)
* Containerization (Docker)
* Continuous Integration (GitHub Actions)
* Build Automation (Jenkins)

---

## 🚀 Features

* ✅ Home API (`/`)
* ✅ Members API (`/members`)
* ✅ Programs API (`/programs`)
* ✅ Add Program (POST API)
* ✅ Input Validation & Error Handling
* ✅ Logging for monitoring
* ✅ Health Check endpoint (`/health`)

---

## 🛠️ Tech Stack

* Python 3.10
* Flask
* Pytest
* Docker
* GitHub Actions
* Jenkins

---

## 📂 Project Structure

```
ACEest_Fitness/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── main.yml
└── README.md
```

---

## ⚙️ Local Setup & Execution

### 1️⃣ Clone Repository

```
git clone https://github.com/2024tm93613/aceest-devops-project
cd ACEest_Fitness
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Application

```
python app.py
```

👉 Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🧪 Running Tests

```
pytest -v
```

✔ All test cases validate API functionality and edge cases.

---

## 🐳 Docker Setup

### Build Image

```
docker build -t aceest-app .
```

### Run Container

```
docker run -p 5000:5000 aceest-app
```

---

## 🔁 CI/CD Pipeline

### 🔹 GitHub Actions

* Trigger: `push` & `pull_request`
* Steps:

  * Install dependencies
  * Run Pytest
  * Build Docker image

## 🔄 CI/CD Pipeline Flow

The application follows a complete DevOps lifecycle:

```
Developer → GitHub Push → GitHub Actions → Docker Build → Pytest → Jenkins Build
```

### Pipeline Stages:

1. **Code Push**: Developer pushes code to GitHub repository
2. **GitHub Actions Triggered**:

   * Install dependencies
   * Run unit tests using Pytest
   * Build Docker image
3. **Docker Validation**:

   * Application is containerized
   * Ensures environment consistency
4. **Jenkins Build Trigger**:

   * Jenkins pulls latest code from GitHub
   * Executes build and test steps
   * Acts as secondary quality gate

---

## ⚙️ Jenkins Integration

Jenkins is configured to:

* Pull code from GitHub repository
* Install dependencies using `requirements.txt`
* Run Pytest test suite
* Validate build success

### Jenkins Build Steps:

```bash
pip install -r requirements.txt
pytest
```

This ensures that only tested and stable code progresses further.

---

##  System Architecture

[ Developer ]
      ↓
[ GitHub Repository ]
      ↓
[ GitHub Actions CI ]
      ↓
[ Docker Build ]
      ↓
[ Pytest Execution ]
      ↓
[ Jenkins Build Server ]

### 🔹 Jenkins

* Pulls latest code from GitHub
* Executes build
* Runs tests for validation

---

## 📦 Versioning Strategy

| Version | Description                                 |
| ------- | --------------------------------------------|
| v1      | Initial Commit with Members API             |
| v2      | Added rograms GET API                       |
| v2.1    | Test case for Programs GET API              |
| v3      | Added Program detail API with validation    |
| v4      | Added POST API for programs                 |
| v4.1    | Added Fixes for empty data and name         |
| v5      | Added validation and edge cases             |
| v7      | Added Logging for end points                |


---

## 🧠 Key DevOps Concepts Demonstrated

* Continuous Integration (CI)
* Continuous Delivery (CD)
* Automated Testing
* Containerization
* Build Automation
* Version Control Best Practices

---

## 🎯 Conclusion

This project successfully implements a **robust CI/CD pipeline** ensuring:

* Code quality
* Automated testing
* Consistent deployment environment
* Faster and reliable delivery

---

## 👨‍💻 Author

**Rajit Singh**
2024TM93613

---

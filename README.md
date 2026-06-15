# 🚀 AI Interview Preparation Platform

An AI-powered full-stack interview preparation platform built using **Django REST Framework, React.js, JWT Authentication, and Google Gemini AI**.

The platform helps students prepare for technical interviews through a structured question bank, answer submission system, AI-generated feedback, and an AI-powered mock interviewer.

---

## 📌 Features

### 🔐 Authentication & Authorization

* User Registration
* User Login
* JWT Authentication
* Protected Routes
* Secure API Access

### 📚 Interview Question Bank

* Technical Interview Questions
* DSA Practice Questions
* Difficulty Levels (Easy, Medium, Hard)
* Search Functionality
* Pagination Support

### ✍️ Answer Submission System

* Submit answers to interview questions
* Store user responses in the database
* Track interview practice progress

### 🤖 AI Answer Evaluation

* Google Gemini AI Integration
* Automated Answer Review
* Strength Analysis
* Weakness Identification
* Personalized Improvement Suggestions

### 🎤 AI Mock Interviewer

* Interactive Interview Chatbot
* Technical Interview Simulation
* Dynamic Question Generation
* AI-Based Responses

### ⚡ Frontend Features

* Modern React User Interface
* React Router Navigation
* Protected Pages
* API Integration
* Real-Time Feedback Display

---

## 🏗️ System Architecture

```text
React Frontend
      │
      ▼
Django REST APIs
      │
      ▼
JWT Authentication
      │
      ▼
Database Layer
      │
      ▼
Google Gemini AI
```

---

## 🛠️ Tech Stack

### Backend

* Python
* Django
* Django REST Framework (DRF)
* JWT Authentication
* SQLite

### Frontend

* React.js
* JavaScript
* HTML
* CSS

### AI

* Google Gemini API

### Tools

* Git
* GitHub
* Postman

---

## 📂 Project Structure

```text
AI-Interview-Preparation-Platform/

├── backend/
│   ├── users/
│   ├── questions/
│   ├── practice/
│   ├── interview/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── screenshots/
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-interview-preparation-platform.git

cd ai-interview-preparation-platform
```

---

### 2️⃣ Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Backend runs at:

```text
http://127.0.0.1:8000/
```

---

### 3️⃣ Frontend Setup

Open a new terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173/
```

---

## 🔑 Environment Variables

Create a `.env` file inside the backend directory:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 🎯 Key Learnings

This project helped in understanding:

* Full-Stack Development
* REST API Design
* JWT Authentication
* React State Management
* React Routing
* Backend Architecture
* AI Integration
* Prompt Engineering
* API Error Handling
* Secure Environment Variable Management

---


## 🔮 Future Improvements

* Performance Analytics Dashboard
* Interview Progress Tracking
* Speech-to-Text Interview Practice
* Personalized Learning Recommendations
* Interview History Management
* Gamification and Leaderboards
* Resume Analysis using AI

---

## 👨‍💻 Author

**Samridhi Saxena**

* GitHub: https://github.com/21sam-05
* LinkedIn: https://www.linkedin.com/in/samridhi-saxena-07231a28a/

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub.

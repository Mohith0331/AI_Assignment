# AI Assignment – Name Matching System & Local Recipe Chatbot

This project contains two tasks implemented in Python.  
Both tasks are fully runnable locally on a standard Windows or Linux laptop with clearly documented steps and no external setup beyond installing dependencies.

---

## 📌 Task Overview

### Task 1: Matching Person Names
- Accepts a name as input
- Finds the most similar names from a predefined dataset
- Displays similarity scores and ranked results

### Task 2: Local Recipe Chatbot
- Accepts ingredients as input
- Suggests a recipe based on ingredient matching
- Exposes functionality via a local FastAPI server
- Returns responses in JSON format

---

## 📁 Project Structure

AI_Assignment/
│
├── Task_1/
│   ├── name_match.py
│   ├── names.py
│   └── requirements.txt
│
├── Task_2/
│   ├── app.py
│   ├── model.py
│   ├── recipe_data.py
│   └── requirements.txt
│
└── README.md

---

## 🖥️ System Requirements
- OS: Windows / Linux
- Python: 3.9 or higher
- Internet required only for installing dependencies

---

## ⚙️ Setup Instructions

(Optional) Create a virtual environment:
python -m venv venv

Activate:
Windows: venv\Scripts\activate
Linux/macOS: source venv/bin/activate

Install dependencies:
pip install -r Task_1/requirements.txt
pip install -r Task_2/requirements.txt

---

## 🧩 Task 1 – Name Matching System

Run:
python Task_1/name_match.py

Sample Input:
Suneetha

Expected Output:
Best Match:
Suneeta - Score: 93.33333333333333

Other Matches:
Seetha - Score: 85.71428571428572
Sunitha - Score: 80.0
Seeta - Score: 76.92307692307692
Geetha - Score: 71.42857142857143

---

## 🤖 Task 2 – Local Recipe Chatbot

Run server:
uvicorn Task_2.app:app --reload

API URL:
http://127.0.0.1:8000/chat

Sample Request:
{
  "ingredients": ["egg", "onion"]
}

Expected Response:
{
  "recipe": "Egg Onion Omelette",
  "steps": "Beat eggs, sauté onions, cook together."
}

---

## 🧪 API Testing (Windows PowerShell)

Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/chat `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"ingredients":["egg","onion"]}'

---

## 📦 Dependencies
- fastapi
- uvicorn
- rapidfuzz

---

# AI Assignment – Name Matching System & Local Recipe Chatbot

This project contains **two tasks** implemented in Python, fully runnable on a **standard Windows or Linux laptop** with minimal setup.

---

## 📌 Task Overview

### ✅ Task 1: Matching Person Names
Build a name-matching system that:
- Takes a user-entered name
- Finds the most similar names from a dataset
- Displays similarity scores and ranked matches

### ✅ Task 2: Local LLM-style Recipe Chatbot
Build a local chatbot system that:
- Accepts ingredients as input
- Suggests a recipe based on ingredient matching
- Runs locally using FastAPI
- Returns responses in JSON format

---

## 📁 Project Structure
AI_Assignment/
│
├── Task_1/
│ ├── name_match.py
│ ├── names.py
│ └── requirements.txt
│
├── Task_2/
│ ├── app.py
│ ├── model.py
│ ├── recipe_data.py
│ └── requirements.txt
│
└── README.md

---

## 🖥️ System Requirements

- Operating System: Windows or Linux
- Python Version: **3.9 or higher**
- Internet connection required only for installing dependencies

---

## ⚙️ Setup Instructions

### 1️⃣ (Optional) Create Virtual Environment
```bash
python -m venv venv```

***Windows**
venv\Scripts\activate

**Linux / macOS**
source venv/bin/activate

### 2️⃣ **Install Dependencies**
pip install -r Task_1/requirements.txt
pip install -r Task_2/requirements.txt

### 🧩 **Task 1 – Name Matching System**
▶ **How to Run**
python Task_1/name_match.py

🧪 **Sample Input**
Enter a name: Suneetha

✅ **Expected Output**
Best Match:
Suneeta - Score: 93.33333333333333

Other Matches:
Seetha - Score: 85.71428571428572
Sunitha - Score: 80.0
Seeta - Score: 76.92307692307692
Geetha - Score: 71.42857142857143

🤖 **Task 2 – Local Recipe Chatbot (FastAPI)**
▶ Start API Server
uvicorn Task_2.app:app --reload

Server runs at:
http://127.0.0.1:8000

▶ **API Endpoint**
POST /chat

🧪 **Sample Request**
{
  "ingredients": ["egg", "onion"]
}

✅ **Expected Response**
{
  "recipe": "Egg Onion Omelette",
  "steps": "Beat eggs, sauté onions, cook together."
}

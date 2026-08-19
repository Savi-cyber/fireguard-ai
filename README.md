# 🔥 FireGuard AI

### AI-Powered Hybrid Wildfire Risk Prediction System

FireGuard AI is a hybrid wildfire risk assessment system that combines **historical fire activity** with **environmental and climate-related conditions** to estimate wildfire risk.

The system uses two independent prediction models and combines their outputs to generate a final wildfire risk level.

---

## 🚀 Project Overview

Wildfire risk is influenced by multiple factors. Historical fire activity alone may not capture changing environmental conditions, while climate/weather conditions alone may not represent existing fire activity.

FireGuard AI addresses this by combining two prediction approaches:

- **Type-1 Model** → Historical and fire-activity based risk
- **Type-2 Model** → Climate/environmental condition based risk
- **Hybrid Decision Layer** → Combines both predictions into a final risk level

### Risk Levels

- 🟢 Low
- 🟡 Medium
- 🔴 High

---

## 🧠 How FireGuard AI Works

```text
                    User Input
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
   Historical Fire              Environmental /
      Activity Data               Climate Data
          │                           │
          ▼                           ▼
    Type-1 Model                 Type-2 Model
          │                           │
          └─────────────┬─────────────┘
                        ▼
                 Hybrid Logic
                        │
                        ▼
                 Final Risk Level
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        Risk Dashboard       AI Explanation

✨ Features
🔥 Hybrid wildfire risk prediction
📊 Separate Type-1 and Type-2 risk predictions
🌦️ Environmental/weather input support
📍 Interactive location selection
🗺️ Map-based prediction interface
🚨 High-risk alert system
🧠 AI-generated risk explanation
📈 Risk analytics visualization
📜 Prediction history
⚡ FastAPI backend
💻 React-based frontend
📸 Screenshots
Main Dashboard

Wildfire Prediction Interface

High-Risk Detection

AI Explanation & Prediction History

🛠️ Tech Stack
Machine Learning
Python
Pandas
NumPy
Scikit-learn
Joblib
Backend
FastAPI
Uvicorn
Python
Frontend
React
Vite
JavaScript
Tailwind CSS
Leaflet
Development Tools
Git
GitHub
VS Code
📁 Project Structure
fireguard-ai/
│
├── abstract/
│
├── backend/
│   ├── main.py
│   ├── hybrid_logic.py
│   └── requirements.txt
│
├── code/
│   ├── type1_model.py
│   ├── type1_preprocess.py
│   ├── type1_feature_engineering.py
│   ├── type2_model.py
│   ├── type2_preprocess.py
│   ├── type2_feature_engineering.py
│   └── hybrid_manual_predict.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── literature survey/
│
├── models/
│   ├── type1_model.pkl
│   └── type2_model.pkl
│
├── docs/
│   └── screenshots/
│
├── README.md
└── .gitignore
⚙️ Installation
1. Clone the repository
git clone https://github.com/Savi-cyber/fireguard-ai.git
cd fireguard-ai
🐍 Backend Setup

Navigate to the backend:

cd backend

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

python -m uvicorn main:app --reload

Backend will run at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs
⚛️ Frontend Setup

Open another terminal.

Navigate to:

cd frontend

Install dependencies:

npm install

Start the React development server:

npm run dev

The frontend will normally run at:

http://localhost:5173
🔄 Running the Complete System

You need two terminals.

Terminal 1 — Backend
cd "wildfire prediction\backend"
venv\Scripts\activate
python -m uvicorn main:app --reload
Terminal 2 — Frontend
cd "wildfire prediction\frontend"
npm run dev

Then open:

http://localhost:5173
📊 Prediction Pipeline

FireGuard AI follows a two-stage prediction approach.

Type-1 — Historical Fire Risk

The Type-1 model evaluates historical/fire-activity related information to estimate the current fire risk.

Type-2 — Environmental Risk

The Type-2 model evaluates environmental and climate-related conditions that may influence wildfire risk.

Hybrid Prediction

The two model outputs are combined through the hybrid decision layer to produce the final wildfire risk classification.

Type-1 Risk
     +
Type-2 Risk
     ↓
Hybrid Decision Logic
     ↓
Final Risk
🎯 Objective

The goal of FireGuard AI is to provide an integrated wildfire risk assessment interface that considers both fire activity and environmental conditions, rather than relying on a single source of information.

🚀 Future Improvements
Real-time wildfire data integration
Automated weather API integration
Satellite-based fire detection
Larger geographical coverage
Model performance monitoring
Explainable AI improvements
Real-time notifications
Cloud deployment
Mobile-friendly interface
⚠️ Disclaimer

FireGuard AI is a research/academic project intended for experimentation and demonstration. Predictions should not be treated as an official emergency or disaster-management warning system.

👨‍💻 Author

Savithan S

B.Tech Information Technology

Interested in:

Artificial Intelligence
Machine Learning
Deep Learning
Data Science
AI Engineering
# HARIS – Hybrid AI Risk Intelligence System for Wildfires

A professional decision-support dashboard that predicts wildfire risk using:
- Historical satellite fire data (Type‑1)
- Current weather conditions (Type‑2)
- Hybrid decision logic

---

## Project Structure

```
/project-root
 ├── backend
 │    ├── main.py
 │    ├── hybrid_logic.py
 │    ├── models
 │    │    ├── type1_model.pkl
 │    │    └── type2_model.pkl
 │    └── requirements.txt
 │
 ├── frontend
 │    ├── src
 │    │    ├── components
 │    │    │    ├── Header.jsx
 │    │    │    ├── InputType1.jsx
 │    │    │    ├── InputType2.jsx
 │    │    │    ├── RiskOutput.jsx
 │    │    │    ├── ExplainableAI.jsx
 │    │    │    ├── FireHistoryChart.jsx
 │    │    │    ├── WeatherChart.jsx
 │    │    │    ├── HybridRiskMeter.jsx
 │    │    │    └── AlertSound.jsx
 │    │    ├── services
 │    │    │    └── api.js
 │    │    ├── styles
 │    │    │    ├── theme.css
 │    │    │    └── dashboard.css
 │    │    ├── App.jsx
 │    │    └── index.js
 │    └── public
 │         └── sounds
 │             └── alert.mp3
 └── README.md
```

---

## Run Instructions

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm start
```

The dashboard will open at `http://localhost:3000`.

---

## Features

- **Hybrid Risk Logic**: Combines Type‑1 (satellite fire history) and Type‑2 (weather) signals.
- **Professional UI**: Dark theme, responsive, research‑grade dashboard.
- **Explainable AI**: Shows why a risk level was assigned.
- **Visualizations**: Fire history, weather, and hybrid risk meter charts.
- **Alert System**: Plays alert sound and shows red glow for High risk.
- **Future Scope**: Collapsible section outlining next steps.

---

## API Endpoint

**POST /predict**

Request body:
```json
{
  "type1": {
    "fire_count": 42,
    "avg_frp": 18,
    "max_frp": 55,
    "night_fire_ratio": 0.32,
    "confidence_score": 0.78,
    "fire_trend": 12
  },
  "type2": {
    "temperature": 32,
    "humidity": 38,
    "wind_speed": 6.2,
    "rainfall": 4
  }
}
```

Response:
```json
{
  "type1_risk": "Medium",
  "type2_risk": "High",
  "hybrid_score": 1.48,
  "final_risk": "High",
  "explanation": [
    "High fire history intensity detected",
    "Elevated temperature and low humidity",
    "Wind speed favors rapid fire spread"
  ]
}
```

---

## Tech Stack

- **Backend**: Python, FastAPI, Uvicorn, joblib
- **Frontend**: React, Recharts, Pure CSS, HTML5 Audio API
- **Models**: Pre‑trained Type‑1 and Type‑2 wildfire risk models (joblib)

---

## Future Scope

- Real‑time weather API integration (OpenWeatherMap)
- Satellite API integration (NASA FIRMS)
- Region‑based map visualization
- Emergency alert system integration

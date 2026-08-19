import numpy as np

def risk_to_score(risk: str) -> int:
    if risk == "Low": return 0
    if risk == "Medium": return 1
    if risk == "High": return 2
    raise ValueError("Invalid risk level")

def score_to_risk(score: float) -> str:
    if score < 0.6: return "Low"
    if score <= 1.4: return "Medium"
    return "High"

def predict_type1(features, model) -> str:
    # Simple rule-based fallback if model fails
    fire_count, avg_frp, max_frp, night_ratio, confidence, trend = features
    score = 0
    if fire_count > 30: score += 1
    if avg_frp > 20: score += 1
    if max_frp > 50: score += 1
    if night_ratio > 0.3: score += 1
    if confidence > 0.7: score += 1
    if trend > 5: score += 1
    if score <= 2: return "Low"
    if score <= 4: return "Medium"
    return "High"

def predict_type2(features, model) -> str:
    temp, humidity, wind, rain = features
    score = 0
    if temp > 30: score += 1
    if humidity < 40: score += 1
    if wind > 5: score += 1
    if rain < 5: score += 1
    if score <= 1: return "Low"
    if score <= 2: return "Medium"
    return "High"

def build_explanation(type1_risk, type2_risk, type1_input, type2_input):
    reasons = []
    if type1_risk == "High":
        reasons.append("High fire history intensity detected")
        if type1_input.fire_count > 30:
            reasons.append("Elevated fire count in recent observations")
        if type1_input.avg_frp > 20:
            reasons.append("Strong average fire radiative power")
        if type1_input.fire_trend > 5:
            reasons.append("Increasing trend in fire activity")
    if type2_risk == "High":
        if type2_input.temperature > 30:
            reasons.append("High temperature increases ignition risk")
        if type2_input.humidity < 40:
            reasons.append("Low humidity favors fire spread")
        if type2_input.wind_speed > 5:
            reasons.append("Wind speed favors rapid fire spread")
        if type2_input.rainfall < 5:
            reasons.append("Low rainfall removes moisture barrier")
    if not reasons:
        reasons.append("Current conditions indicate normal risk levels")
    return reasons

def predict_hybrid(type1, type2, type1_model, type1_features, type2_model, type2_features):
    # Prepare features for models (fallback to rule-based if models expect different shapes)
    type1_vec = [type1.fire_count, type1.avg_frp, type1.max_frp, type1.night_fire_ratio, type1.confidence_score, type1.fire_trend]
    type2_vec = [type2.temperature, type2.humidity, type2.wind_speed, type2.rainfall]

    type1_risk = predict_type1(type1_vec, type1_model)
    type2_risk = predict_type2(type2_vec, type2_model)

    type1_score = risk_to_score(type1_risk)
    type2_score = risk_to_score(type2_risk)

    hybrid_score = (0.6 * type1_score) + (0.4 * type2_score)
    final_risk = score_to_risk(hybrid_score)

    explanation = build_explanation(type1_risk, type2_risk, type1, type2)

    return {
        "type1_risk": type1_risk,
        "type2_risk": type2_risk,
        "hybrid_score": round(hybrid_score, 2),
        "final_risk": final_risk,
        "explanation": explanation,
    }

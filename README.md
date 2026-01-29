# Industrial-Vibration-Analytic-Tool
Automated vibration and temperature anomaly detection system for mechanical drive-trains based on ISO 10816-3."
# ISO 10816-3 Based Industrial Asset Health Monitor ⚙️📊

## Project Overview
This repository contains a professional-grade Python tool designed for **Predictive Maintenance** and **Condition Monitoring**. As a Mechanical Engineer and AI graduate student, I developed this algorithm to bridge the gap between classical mechanical standards and digital transformation (Industry 4.0).

The system analyzes real-time sensor data (vibration and temperature) to detect anomalies in industrial rotating machinery before catastrophic failures occur.

## 🛠 Engineering Standards (ISO 10816-3)
The core logic is built upon the **ISO 10816-3** international standard, which defines vibration severity for industrial machines. 
- **Critical Threshold (Vibration):** Set at **4.5 mm/s** (RMS), marking the transition to Restricted Operation / Danger zone for Machine Group 1 & 2.
- **Thermal Limit:** Integrated a **95°C** safety threshold to monitor bearing health and prevent thermal runaway.



## 🚀 Key Features
- **Real-time Anomaly Detection:** Instant evaluation of sensor inputs against global safety norms.
- **Automated Logging:** Generates a `Health_Report.txt` file for documentation and traceability—crucial for audit-heavy sectors like Defense and Automotive.
- **Robust Error Handling:** Built with industrial terminal stability in mind to prevent runtime crashes during data entry.

## 📂 Project Structure
- `main.py`: The core analysis engine.
- `README.md`: Technical documentation and project vision.
- `Health_Report.txt`: Sample output generated after analysis.

## 🎯 Industrial Use Cases
- **Automotive:** Optimizing **OEE** in powertrain assembly lines.
- **Medical Technology:** Precision monitoring for high-speed motors in imaging devices (e.g., Siemens Healthineers MRI cooling systems).
- **Defense & Aerospace:** Structural health monitoring for mission-critical platform components.

## 📈 Future Vision (AI Integration)
As part of my ongoing Master's degree in **Artificial Intelligence**, the next phase of this project involves:
1. Implementing **LSTM (Long Short-Term Memory)** networks for time-series forecasting.
2. Integrating a **Digital Twin** interface for real-time data visualization.

---
**Developed by Enes | Mechanical Engineer | AI Researcher** *Focused on creating smarter, safer, and more efficient industrial ecosystems.*

# 🚀 Vyom_Suraksha

**A Modular Host-Based Defensive Cybersecurity Framework (Python, Linux)**

---

## 🧠 Overview

Vyom_Suraksha is a **host-based intrusion detection and response framework** designed to simulate real-world defensive security systems.
It integrates **risk-based decision making, integrity verification, deception techniques, and automated response mechanisms** into a unified architecture.

The system is built with a **layered design**, separating decision logic from execution to ensure scalability, clarity, and robustness.

---

## 🏗️ Architecture

### 🔶 Bhairavi (Policy Layer – Decision Engine)

Responsible for analyzing system state and making decisions:

* Risk Engine (dynamic risk scoring)
* State Controller (NORMAL → ALERT → CONTAINMENT → LOCKDOWN)
* Decision Engine (state transition tracking)
* Integrity Guard (file tampering detection)
* Secret Guard (access control)
* Policy Engine (centralized decision logic)
* Trust Core (system trust evaluation)

---

### 🔷 Bhairava (Execution Layer – Response Engine)

Handles detection and defensive actions:

* Monitor (CPU & memory anomaly detection)
* Alert System (logs, desktop notification, sound alerts)
* Backup System (secure encrypted backup)
* Audit System (tamper-evident logging)
* Defense Module (response execution)
* Orchestrator (connects detection → decision → response)
* Stealth Module (logging/visibility control)

---

### 🧩 Supporting Modules

* **Deception Layer** → Canary-based intrusion detection
* **Service Layer** → Daemon + service manager for automation

---

## ⚙️ Key Features

* 🔍 **Anomaly Detection** (CPU & memory monitoring)
* 🧪 **Canary-Based Intrusion Detection**
* 🛡️ **File Integrity Verification (SHA-256)**
* 📊 **Risk-Based State Machine**
* ⚡ **Automated Defensive Response**
* 🔔 **Alert System (Logs + Desktop + Sound)**
* 🔐 **Tamper-Evident Audit Logging**
* 🧠 **Trust-Aware Decision Making**
* 🔄 **Graceful Failure Handling**

---

## 🔁 System States

| State       | Description                      |
| ----------- | -------------------------------- |
| NORMAL      | No threat detected               |
| ALERT       | Suspicious activity detected     |
| CONTAINMENT | Active mitigation triggered      |
| LOCKDOWN    | Critical threat, maximum defense |

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install psutil pyyaml
```

### 2. Run the system

```bash
python vyom_suraksha.py
```

---

## 🧪 Testing the System

### 🟡 CPU Attack Simulation

```bash
for i in {1..8}; do yes > /dev/null & done
killall yes
```

---

### 🟠 Canary Attack

```bash
echo "attack" >> deception/decoy_secret.txt
```

---

### 🔴 Integrity Attack (Safe)

```bash
cp bhairavi/risk_engine.py bhairavi/test_file.py
echo "tamper" >> bhairavi/test_file.py
```

---

## 📁 Project Structure

```
Vyom_Suraksha/
├── bhairavi/       # Policy Layer (decision logic)
├── bhairava/       # Execution Layer (response system)
├── deception/      # Canary-based detection
├── service/        # Daemon & service manager
├── config/         # Configuration files
├── vyom_suraksha.py
```

---

## 🎯 Key Design Principles

* Separation of Concerns (Decision vs Execution)
* Modular Architecture
* Fault Tolerance
* Security-first Design
* Real-world Simulation

---

## 🧠 Learning Outcomes

This project demonstrates:

* System-level security design
* Intrusion detection techniques
* Risk-based decision modeling
* Defensive programming practices
* Modular software architecture

---

## 👨‍💻 Author

**Dipraj Sodaye**
Cybersecurity Enthusiast | Python Developer

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🚀 Future Scope

* Network-based threat detection
* AI-based anomaly detection
* Distributed monitoring system
* Dashboard visualization

---

> ⚡ *Vyom_Suraksha is a prototype framework designed for learning and demonstration of defensive cybersecurity concepts.*

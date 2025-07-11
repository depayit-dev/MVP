# 🛡️ RedTeam-Fintech-Escrow-Sim

A simulated Red Team testing project targeting escrow-based payment systems and second-hand marketplace fraud flows. Designed to identify real-world threats in P2P Fintech platforms using API exploitation, scam emulation, and transaction replay attacks.

---

## 🚀 Project Overview

This repository showcases a red team simulation framework built around a mock P2P escrow platform. It is designed to:

- Emulate fraud tactics from Thai second-hand markets (e.g. Facebook Marketplace)
- Simulate API-based attacks (e.g. parameter tampering, insecure IDOR, replay)
- Explore scam behaviors such as credit-building deception and pressure-based fraud
- Demonstrate real-world offensive use cases to harden backend Fintech systems

---

## 🔧 Tech Stack

| Layer         | Tech                          |
|---------------|-------------------------------|
| Backend       | Python (Flask), PostgreSQL, Supabase |
| Offensive     | Python scripts, Burp Suite, OWASP ZAP |
| Data Tools    | OSINT, Telegram Recon Bot, Web scraping |
| Testing       | Postman, curl, custom API testing scripts |

---

## 📁 Features

- 🧠 **Scam Flow Generator**  
  Simulates user behavior in fraudulent credit-building and escrow abuse.

- 🔐 **API Exploit Modules**  
  - Replay attacks on `/confirm_payment`  
  - IDOR test on `/transaction/status`  
  - Token manipulation and header spoofing

- 🧪 **Red Team Simulation Cases**  
  - Fake product flow + pressure scenario  
  - Real delivery proof with delayed fraud trigger  
  - Multi-transaction decoy behavior before scam

- 🧾 **Transaction Log Monitor**  
  Analyzes metadata to detect behavioral anomalies.

---

## 📊 Sample Test Cases

```bash
# Replay attack demo
curl -X POST https://api.depayit.io/transaction/confirm \
-H "Authorization: Bearer VALID_TOKEN" \
-d '{"tx_id": "abc123", "confirm_pin": "543210"}'
```

```python
# Python test for IDOR
def check_idor_exposure(tx_id, attacker_token):
    headers = {"Authorization": f"Bearer {attacker_token}"}
    url = f"https://api.depayit.io/transaction/status/{tx_id}"
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print("❗️Potential IDOR detected:", res.json())
```

---

## 🧪 Usage

1. Clone the repo

```bash
git clone https://github.com/depayit-dev/redteam-fintech-escrow-sim.git
cd redteam-fintech-escrow-sim
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Start Flask server (simulated backend)

```bash
python app.py
```

4. Use `/scripts` for red team attack automation and `/data/logs/` for simulation logs.

---

## 📂 Directory Structure

```
.
├── app.py
├── /api/                 ← Mock APIs simulating escrow platform
├── /scripts/             ← Red team attack automation
├── /data/
│   ├── logs/             ← Attack results & replay logs
│   └── scams/            ← Fraud flow data (json / txt)
├── README.md
└── requirements.txt
```

---

## 🧠 Inspirations

This project was inspired by real scam patterns observed in Thai P2P platforms. Combining knowledge of fraud behavior and technical abuse, it aims to bridge cyber psychology and offensive engineering for real-world fintech defense.

---

## ⚠️ Legal Notice

> This project is for **educational and ethical use only**. All tests are run on mock platforms, and any use against real systems without explicit permission is strictly prohibited.

---

## 👨‍💻 Author

**Nuttapong Faithong**  
Offensive Security | Cyber Threat Intelligence | Fintech Fraud  
[GitHub](https://github.com/depayit-dev) | [Email](mailto:nuttapong.cyber@protonmail.com)


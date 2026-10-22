# AIOps Automated SOC Triage Pipeline 🛡️🤖

An automated security incident response and log triage pipeline engineered in Python. This tool ingests high-frequency network event logs, pre-filters traffic noise, and leverages the **Google GenAI SDK** (`gemini-3.8-flash`) to perform live RFC 1918 private IP classification, threat risk scoring, and actionable SOC analyst recommendations.

---

## Key Features

* **Log Pre-Filtering & Noise Reduction:** Aggregates incoming firewall connection attempts locally using hash-map dictionary counters to filter single-occurrence traffic and optimize API token usage.
* **RFC 1918 Network Classification:** Differentiates between internal private subnets (Class A, B, C) and external public threat vectors.
* **AI Threat Triage:** Pipes structured incident context to `gemini-3.8-flash` for instant risk classification and step-by-step mitigation guidance.
* **Production Error Resilience:** Implements exponential backoff retry loops to handle API 503 load states seamlessly without crashing the pipeline.
* **Secure Environment Management:** Isolates sensitive API credentials using local system environment variables (`GEMINI_API_KEY`).

---

## Tech Stack & Dependencies

* **Language:** Python 3.11+
* **SDK:** `google-genai`
* **Tools:** Git, GitHub, VS Code, PowerShell / Bash
* **API Model:** `gemini-3.8-flash`

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/M1XFlow/Aiops-log-triage-pipeline.git](https://github.com/M1XFlow/Aiops-log-triage-pipeline.git)
cd Aiops-log-triage-pipeline

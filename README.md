<div align="center">

# 🦅 ZeroScout
### The Autonomous Local & Cloud Threat Hunter

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-red?style=for-the-badge)

<p align="center">
  <b>"Don't just scan files. Visualize the battlefield."</b>
</p>

</div>

---

## 🚀 What is ZeroScout?

**ZeroScout** is a next-generation threat hunting framework designed for **Incident Responders (DFIR)**, **SOC Analysts**, and **Malware Researchers**.

Unlike traditional antivirus scanners that act as a "Black Box", ZeroScout acts as a **Cyber Defense HQ**. It visualizes the attack surface in a live **War Room**, identifies the **APT Group** using genetic code analysis (ImpHash/SSDeep), and automatically generates **YARA & SIGMA** defense rules.

It operates in a **Hybrid Architecture**:
1.  **Local Hunter (Offline Mode):** Uses advanced heuristics, entropy analysis, and Windows Defender bridging to detect 0-day threats without internet access.
2.  **Cloud Powered (Online Mode):** Seamlessly integrates with **ZeroScout Cloud Engine** (powered by Threat.Zone) for military-grade sandbox analysis.

---

## ⚡ Key Capabilities

### 🌍 1. Live War Room Visualization
ZeroScout scrapes C2 (Command & Control) IPs from the binary and visualizes the network traffic on a live **ASCII World Map** directly in your terminal.
> *See where the attack is coming from, in real-time.*

### 🧬 2. Genetic Attribution (DNA Analysis)
New malware variant? ZeroScout analyzes the **Code DNA (ImpHash)** and TTP behaviors to identify the actor behind the file.
> *"This file is unknown, but its DNA matches **Lazarus Group** with 92% confidence."*

### 🛡️ 3. Auto-Defense Architect
Stop writing detection rules manually. ZeroScout generates deployable defense codes instantly:
* **YARA Rules:** For endpoint scanning.
* **SIGMA Rules:** For SIEM correlation.

### 🔍 4. Mass Hunt Mode
Scan an entire directory (e.g., Downloads folder, USB Drive) in seconds. ZeroScout filters the noise and highlights only high-risk artifacts with specific reasons (e.g., "High Entropy", "Process Injection").

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone [https://github.com/yourusername/zeroscout.git](https://github.com/yourusername/zeroscout.git)
cd zeroscout

# 2. Install dependencies
pip install -r requirements.txt
pip install .

# 3. Ready to hunt!
python -m zeroscout.cli scan "malware.exe"
<div align="center">

# 🦅 ZeroScout
### The Autonomous Local & Cloud Threat Hunter

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Win%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge)](https://github.com/yourusername/zeroscout)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-red?style=for-the-badge)](https://github.com/yourusername/zeroscout)

<p align="center">
  <b>"Don't just scan files. Visualize the battlefield."</b>
</p>

[🇹🇷 Türkçe Dökümantasyon İçin Tıklayın (Read in Turkish)](README.tr.md)

</div>

---

## 🚀 What is ZeroScout?

**ZeroScout** is a next-generation threat hunting framework designed for **Incident Responders (DFIR)**, **SOC Analysts**, and **Malware Researchers**.

Unlike traditional antivirus scanners that act as a "Black Box", ZeroScout acts as a **Cyber Defense HQ**. It visualizes the attack surface in a live **War Room**, identifies the **APT Group** using genetic code analysis (ImpHash/SSDeep), and automatically generates **YARA & SIGMA** defense rules.

It operates in a **Hybrid Architecture**:
1.  **Local Hunter (Offline Mode):** Uses advanced heuristics, entropy analysis, and Windows Defender bridging to detect 0-day threats without internet access.
2.  **Cloud Powered (Online Mode):** Seamlessly integrates with the high-performance **ZeroScout Cloud Engine** for military-grade sandbox analysis.

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

## 📸 Intelligence Dashboard (Demo)

ZeroScout provides a comprehensive, interactive terminal dashboard combining multiple intelligence streams.

### 🎥 Live War Room Feed (Video/GIF Demo Recommended)
Due to the dynamic nature of the dashboard, it is highly recommended to showcase this feature using a **video or GIF** in your README.

> *Example Video:* [Watch the ZeroScout Live War Room in Action](assets/zeroscout_demo.gif)

### 🧬 Genetic Attribution Summary
```plaintext
╭──────────────────────────────────── 🧬 GENETIC ATTRIBUTION ─────────────────────────────────────╮
│ ACTOR: [High-Risk Threat Actor]                                                                 │
│ CONFIDENCE: 92% [██████████████████░]                                                           │
│ Analysis: Code DNA (ImpHash) and TTP behaviors match known APT28 profiles.                      │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
````

-----

## 📦 Installation

Bu projeyi bir Python paketi olarak kurmak, tüm bağımlılıkları otomatik olarak yükler ve CLI aracını kullanıma hazır hale getirir.

```bash
# 1. Clone the repository
git clone https://github.com/SUmidcyber/ZeroScout.git
cd ZeroScout

# 2. Install dependencies (Kurulum için burayı kullan)
# Bu, ZeroScout'u sisteminizde bir komut olarak erişilebilir kılar.
pip install .

# Veya sadece test için:
# pip install -r requirements.txt 

# 3. Ready to hunt!
python -m zeroscout.cli scan "malware.exe"
```

-----

## 🎮 Usage Guide

### 1\. Deep Analysis (Zero-Day Hunting)

Analyze a single file to open the War Room and generate defense rules.

```bash
python -m zeroscout.cli scan "C:\Users\Admin\Desktop\suspicious.exe"
```

### 2\. Mass Hunting (Directory Scan)

Quickly scan a folder to find hidden threats among thousands of files.

```bash
python -m zeroscout.cli scan "C:\Windows\System32"
```

### 3\. Connect Cloud Engine (Optional - API Key)

ZeroScout Cloud Engine'i kullanmak için **`ZEROSCOUT_API_KEY`** ortam değişkenini ayarlamanız gerekir. Anahtar bulunamazsa, sistem otomatik olarak **Yerel Avcı Moduna** geçer.

```bash
# Windows (PowerShell)
$env:ZEROSCOUT_API_KEY="your_api_key_here"

# Linux / Mac
export ZEROSCOUT_API_KEY="your_api_key_here"
```

-----

## 🏗️ Technical Architecture

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Core Engine** | Python 3 | Main logic and CLI handling. |
| **Visuals** | Rich Library | Dashboard-style terminal interface. |
| **Static Analysis** | Pefile & Math | Entropy calculation, Header analysis, ImpHash. |
| **Signatures** | YARA & Regex | Identifying strings, IP addresses, and patterns. |
| **Cloud Bridge** | REST API | Connection to Sandbox Engine. |

-----

## 📜 Disclaimer

**ZeroScout is for educational and defensive purposes only.** The authors are not responsible for any misuse of this tool. Always analyze malware in an isolated environment (VM).

-----


**Developed by Umid Mammadov**

*ZeroScout Technologies*


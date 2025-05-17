# educational-phishing-simulation

# 🔐 Login Page Clone Simulation – For Educational Use Only

This project is a **controlled simulation** that demonstrates how login pages can be cloned and modified to capture user credentials — strictly for **ethical hacking education**, **security awareness**, and **cybersecurity research**.

> ⚠️ This is NOT a hacking tool. It is a learning project to demonstrate vulnerabilities and promote awareness about phishing tactics in a **safe, ethical**, and **legal** environment.

---

## 📚 Project Description

This tool:
- Downloads a webpage's HTML using `curl`
- Modifies the login form using Python + BeautifulSoup
- Hosts the page with a Python Flask backend to simulate how credentials can be captured
- Redirects to a 404 page after submission to mimic a broken link often used in phishing scams

The backend logs submitted credentials for demonstration purposes only.

---

## ⚙️ Technologies Used

- 🐚 Bash scripting (to automate webpage fetch)
- 🐍 Python 3
  - `Flask` (backend server)
  - `BeautifulSoup` (HTML parsing and editing)
- 📄 HTML (captured/modified page)

---

## 🚀 How to Run

1. Clone the repo
2. Install dependencies: `pip install flask beautifulsoup4`
3. Run the Bash script:  
   ```bash
   ./webpage_clone.sh https://example.com/login

index.html and creds.log have been excluded intentionally for ethical and privacy reasons. This project is meant solely for educational simulation and awareness of social engineering tactics.

# 💼 ProfesiaScrapper

> A web scraping and data visualization application that gathers real-time job market data from [profesia.sk](https://www.profesia.sk).

---

## 🖼️ Overview

**ProfesiaScrapper** is a Python-based application designed to collect and analyze data from the Slovak job portal **profesia.sk**.  
Its main goal is to provide up-to-date information about the number of job offers and the average salary across different regions of Slovakia.

The project consists of two main parts:

1. **Server Application** – Automatically scrapes data from *profesia.sk* every hour and stores it in a **Firestore** database.  
2. **Client Application** – Provides a user-friendly interface where registered users can log in and visualize job market data in the form of interactive bar charts.

This makes **ProfesiaScrapper** a useful tool for tracking the dynamics of Slovakia’s labor market — helping users analyze job opportunities and salary trends by region.

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&logoColor=black)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-005C9C?logo=python&logoColor=white)

**Other Tools:**
- `customtkinter` – GUI framework for the desktop client  
- `schedule` – Automated job scheduling  
- `threading` – Parallel execution for scraping and updates  
- `dotenv` – Environment variable management  
- `dataclasses`, `os`, `time`, `re`, `requests` – Core Python modules for system, timing, and regex handling  

---

## 🎬 Showcase

### 🖼️ Interface Preview

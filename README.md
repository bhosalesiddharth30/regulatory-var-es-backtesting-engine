# Regulatory VaR Backtesting Engine (Educational Prototype)

This project implements a simplified **Basel-style backtesting engine** for 1-day Value-at-Risk (VaR) models.  
It demonstrates key skills relevant for **Risk Analytics, Traded Risk, Model Development, and Quant roles**:

- Daily VaR estimation using Historical Simulation  
- Rolling-window VaR forecasting (1-day ahead)  
- Backtesting using exception counts  
- Kupiec Proportion-of-Failures (POF) Test  
- Simplified Basel traffic-light model performance classification  
- Automated markdown risk reporting  
- Clean modular Python code and notebook-based analysis  

This project was built to showcase practical understanding of **regulatory model performance monitoring** and **quantitative risk methods**.

---

## 📊 Results (from demo notebook)

### **1. Daily Returns vs 99% Historical VaR**

![VaR Plot](imgs/var_plot.png)

---

### **2. Basel Backtesting Report**

![Basel Report](imgs/basel_report.png)

---

## 📁 Project Structure

regulatory-var-es-backtesting-engine/
├─ data/
│ └─ sample_returns.csv
├─ docs/
│ └─ model_documentation.md
├─ notebooks/
│ └─ 01_demo_backtest.ipynb
├─ reports/
│ └─ basel_backtest_report.md
├─ src/
│ ├─ data_loader.py
│ ├─ var_models.py
│ ├─ backtesting.py
│ └─ report.py
├─ imgs/
│ ├─ var_plot.png
│ └─ basel_report.png
└─ README.md

yaml
Copy code

---

## 🚀 How to Run

pip install -r requirements.txt
jupyter notebook notebooks/01_demo_backtest.ipynb

yaml
Copy code

---

## 🔍 Features

- Historical Simulation VaR at 99% confidence  
- Rolling 1-day-ahead VaR estimation  
- Exception identification  
- Kupiec POF LR statistic  
- Basel traffic-light calibration check  
- Markdown-based risk report generator  

---

## 📄 Model Documentation

Detailed information regarding:
- Model assumptions  
- Methodology  
- Backtesting logic  
- Risk interpretation  
- Limitations  

…is available in:

docs/model_documentation.md

yaml
Copy code

---

## ⚠️ Disclaimer

This is an **educational prototype** for learning and interview preparation.  
It must **not** be used for live trading, production risk management, or regulatory submissions.
# 📞 Telecom Customer Churn & Drop-Call Prediction Dashboard

**Created by [muhammedabubakr88-ctrl](https://github.com/muhammedabubakr88-ctrl)**

🔗 **Live Demo:** [mtn-churn-dashbord.streamlit.app](https://mtn-churn-dashbord.streamlit.app/)

An interactive Streamlit dashboard that analyzes customer and network data to predict customer churn (customers leaving) and dropped call risk for a telecom provider, modeled on companies like MTN Nigeria.

## 🎯 Overview

This project combines data analysis and machine learning to help telecom companies spot patterns behind customer churn and call drops — so they can act before customers leave or service quality suffers.

## ✨ Features

- Interactive Plotly visualizations of customer and network data
- Machine learning model panel showing model performance
- Live prediction interface — enter customer details and get a real-time churn / drop-call risk score
- Clean, dashboard-style layout built with Streamlit

## 🛠️ Tech Stack

- **Python** — core language
- **Pandas / NumPy** — data processing
- **Scikit-learn** — machine learning model
- **Plotly** — interactive visualizations
- **Streamlit** — dashboard / web app framework
- **Google Colab + pyngrok** — development and temporary live preview environment

## 📊 How It Works

1. Customer and call data is cleaned and processed.
2. A machine learning model is trained to predict:
   - Likelihood of customer churn
   - Likelihood of dropped calls
3. Results are shown on an interactive dashboard, including a live prediction tool where you input customer details and get an instant risk score.

## 🚀 Running the Project

**Option 1 — Locally:**
```bash
pip install -r requirements.txt
streamlit run churn_dashboard.py
```

**Option 2 — In Google Colab (with a temporary public link):**
1. Upload `churn_dashboard.py` and `colab_preview.py` to your Colab session.
2. Get a free ngrok auth token from [ngrok.com](https://ngrok.com).
3. In Colab, click the 🔑 **Secrets** icon on the left sidebar, add a secret named `NGROK_TOKEN`, and paste your token as the value.
4. Run `colab_preview.py` — it will print a public link you can open in your browser.

⚠️ Never hardcode your ngrok token directly in the code or commit it to GitHub — always use Colab Secrets or an environment variable instead.

## 📈 Model Performance

This version uses a simple **Linear Regression** model trained on a small demo dataset to show the prediction workflow end-to-end. For production use, train it on real historical customer data and compare against other models (e.g. Random Forest, Logistic Regression) for better accuracy.

## 📂 Dataset

Currently uses a small built-in sample dataset (7 customers) with `CallDrops`, `DataUsage`, and `ChurnRisk` to demonstrate the dashboard and prediction logic. Swap in a real telecom dataset for production use.

## 🔮 Future Improvements

- Deploy permanently (e.g. Streamlit Community Cloud) instead of using temporary ngrok links
- Train on a real, larger dataset
- Compare additional models for better accuracy
- Add more customer data points to improve prediction quality

## 👤 Author

**muhammedabubakr88-ctrl**
Data Scientist · AI Workflow Architect · Web Developer · Business Insight & Decision-Making

- GitHub: [@muhammedabubakr88-ctrl](https://github.com/muhammedabubakr88-ctrl)
- LinkedIn: *(add your LinkedIn link once set up)*
- Fiverr: *(add your Fiverr profile link once set up)*
- Upwork: *(add your Upwork profile link once set up)*
-

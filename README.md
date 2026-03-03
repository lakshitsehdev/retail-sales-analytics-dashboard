# 📊 Retail Sales & Profitability Analysis Dashboard

## 📌 Project Overview
This project analyzes retail sales data from a Superstore dataset to identify revenue drivers, profitability patterns, discount impact, and operational efficiency trends.

The objective is to extract business insights and build a structured analytical workflow using Python and visualization tools.

---

## 🎯 Business Objectives
- Identify the most profitable product categories  
- Analyze the impact of discounting on profitability  
- Evaluate delivery performance  
- Examine year-over-year sales trends  
- Build and evaluate a simple regression model  

---

## 🔍 Key Insights

- Technology is the highest revenue and profit-generating category.
- Furniture has the lowest profit margin due to higher discounting.
- Office Supplies has the highest number of loss-making transactions.
- Discount and Profit show a negative correlation (-0.21).
- Sales peaked in 2017, indicating consistent business growth.
- Average delivery time is approximately 4 days.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

## 📁 Project Structure

Ecommerce_Dashboard_Project/
│
├── data/
│   └── Sample - Superstore.csv
│
├── notebooks/
│   └── EDA_Superstore.ipynb
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
└── README.md

---

## ▶ How to Run Locally

1. Clone the repository  
2. Install dependencies:

pip install -r requirements.txt

3. Run the Streamlit dashboard:

streamlit run dashboard/app.py

---

## 📈 Model Evaluation

A linear regression model was implemented to predict profit and sales.  
The model showed low explanatory power (low R²), indicating that profit behavior depends heavily on product-level and categorical factors beyond basic numerical features.

This highlights the importance of feature engineering and model selection in real-world ML applications.

---

## 📌 Conclusion

The Superstore analysis reveals that Technology is the strongest-performing category in terms of revenue and profitability, while Furniture suffers from margin compression due to heavy discounting.

The negative correlation between discount and profit (-0.21) indicates that aggressive discounting strategies significantly impact profitability.

This project demonstrates structured EDA, business reasoning, feature engineering, and model evaluation to provide actionable retail insights.
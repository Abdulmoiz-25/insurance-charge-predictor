# 📘 DeveloperHub Task 4 – Insurance Charges Prediction using ML

## 📌 Task Objective

This task focuses on building a regression-based machine learning model that predicts medical insurance charges based on demographic and health-related input features using supervised learning.

---

## 📁 Dataset

**Name:** Medical Cost Personal Dataset  
**Source:** Kaggle

---

## 📊 Features:

- Age
- Sex
- BMI
- Number of Children
- Smoker
- Region

---

## 🎯 Target:

- **Charges** (Medical insurance cost in USD)

---

## 🛠️ Tools & Libraries Used

- **Pandas** – Data loading and preprocessing  
- **Matplotlib & Seaborn** – Data visualization and EDA  
- **Scikit-learn** – Model training, regression, and evaluation  
- **Joblib** – Saving and loading the model  
- **Streamlit** – Web app development and deployment  

---

## 🚀 Approach

### 1. Dataset Loading & Understanding
- Loaded dataset using `pandas.read_csv()`
- Reviewed structure with `.head()`, `.info()`, `.describe()`, and `.shape()`

### 2. Data Preprocessing
- Handled categorical variables using one-hot encoding (e.g., `sex`, `smoker`, `region`)
- Converted data into numeric format suitable for model input
- No missing values, so imputation was not required

### 3. Exploratory Data Analysis (EDA)
- Visualized distribution of charges based on age, smoker status, and region  
- Analyzed correlation between features  
- Used box plots and histograms to understand feature spread

### 4. Model Training & Testing
- Split the data into 80% training and 20% testing
- Trained regression models including:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Selected the best-performing model and saved it using `joblib`

### 5. Evaluation Metrics
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 📊 Results & Insights

- **Random Forest Regressor** delivered the best performance  
- Top features influencing cost: **Smoker**, **BMI**, and **Age**  
- Smoking status significantly increases insurance charges  
- Interactive Streamlit app allows users to predict insurance charges based on input features

---

## ✅ Conclusion

This task completed the full machine learning pipeline:

- Data preprocessing  
- Exploratory Data Analysis  
- Model training and tuning  
- Performance evaluation  
- Deployment via Streamlit  

The deployed app can estimate insurance costs in real-time using user input.

---

## 🖥️ Streamlit Web App

Try out the deployed model here:  
🔗 [Insurance Charges Predictor App](https://insurance-charge-predictor-wfgcxawtvjaqfarmsfknmy.streamlit.app/)

---

## 🔗 Useful Links

- [Scikit-learn Documentation](https://scikit-learn.org/)  
- [Streamlit Docs](https://docs.streamlit.io/)  
- [Matplotlib Docs](https://matplotlib.org/)  
- [Seaborn Docs](https://seaborn.pydata.org/)

---

> 🔖 Submitted as part of the **DeveloperHub Internship Program**

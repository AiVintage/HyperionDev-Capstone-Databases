# 📊 EDA Report – US Arrests  

## 📌 Project Overview  
This project performs an **Exploratory Data Analysis (EDA)** on the **USArrests dataset**, which contains crime statistics from 50 US states in 1973.  
The analysis explores crime patterns, relationships between variables, and key insights that may help in understanding crime trends across states.  
A professional PDF report was generated: **`EDA Report – US Arrests.pdf`**  

---

## 📂 Dataset  
**Source:** `usarrest.csv`  

**Features:**  
- **Murder** – Murder arrests (per 100,000 residents)  
- **Assault** – Assault arrests (per 100,000 residents)  
- **UrbanPop** – Percentage of urban population  
- **Rape** – Rape arrests (per 100,000 residents)  

**Sample Data:**  

| Murder | Assault | UrbanPop | Rape |  
|--------|---------|----------|------|  
| 13.2   | 236     | 58       | 21.2 |  
| 10.0   | 263     | 48       | 44.5 |  
| 8.1    | 294     | 80       | 31.0 |  

---

## ⚙️ Approach  

### Data Preprocessing  
- Checked for **missing values** and dataset consistency.  
- Verified data types and normalized for analysis.  
- Created summary statistics (mean, median, std).  

### Exploratory Analysis  
- Distribution plots for all features.  
- Correlation heatmap to identify variable relationships.  
- Boxplots to highlight state-level variations.  

### Visualizations  
- **Histograms** for variable distributions.  
- **Scatter plots** (e.g., Murder vs. Assault).  
- **Heatmap** to visualize correlations.  

---

## 📊 Results  

### Key Insights  
- States with **high Assault rates** often also had **high Murder rates**.  
- **Urban population** percentage did not always correlate strongly with crime levels.  
- **Rape arrests** showed significant variance across states, suggesting regional differences.  

### Correlation Highlights  
- Murder and Assault: **Strong positive correlation**.  
- UrbanPop and Rape: **Moderate positive correlation**.  

---

## ✅ Key Takeaways  
- Crime statistics vary greatly across US states.  
- **Assault** is the most frequent crime type compared to Murder and Rape.  
- EDA reveals strong inter-variable relationships, useful for further modeling.  
- Insights can guide clustering or classification approaches in future work.  

---

## 🛠️ Tech Stack  
- **Language:** Python  
- **Libraries:** pandas, numpy, matplotlib, seaborn, reportlab  

---

## 👨‍💻 Author  
**AiVintage (Veli)**  
Data Science Graduate | Skilled in Python, Machine Learning, AI, SQL & Data Analysis  

[GitHub](https://github.com/AiVintage) | [LinkedIn](#)  

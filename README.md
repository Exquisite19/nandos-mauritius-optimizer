 Nando's Mauritius: Sales Analytics & Stock Optimizer
An end-to-end data engineering and analytics project simulating 6 months of transaction data to optimize inventory and staffing for a retail environment. 📋 Project Overview This project addresses the challenge of inventory waste and inefficient staffing in high-volume food retail. By generating synthetic but statistically realistic data, we can model peak demand periods and revenue trends specific to the Mauritian market. 🛠 Tech Stack Data Generation: Python (Pandas, NumPy) - Simulated 180 days of transactions with weighted probability for order sizes and weekend surges. Database: MySQL - Structured storage of transaction logs, menu items, and staff performance records. Analytics & Viz: R (ggplot2, Tidyverse) - Statistical analysis and brand-aligned visualizations.

🚀 Technical Challenges Overcome Environment Management: Resolved virtual environment conflicts and ModuleNotFoundError during pandas installation in PyCharm. Data Localization: Adjusted R-based visualization layers to correctly reflect Mauritian Rupee (Rs) currency formatting and brand-specific color palettes (#E85D24). Logical Weighting: Implemented random.choices with custom weights to ensure the simulated data mirrored real-world human behavior (e.g., most customers buying 1-2 items rather than 4). 📁 Repository Structure /scripts/generate_data.py: The Python simulation engine. /analysis/nandos_viz.R: The R script for generating high-fidelity charts. /data/nandos_sales.csv: The final generated dataset. /output/: Contains the 4 key performance charts.

Simulation Engine (Python):
# Showing the weighted probability for realistic orders
n_items = random.choices(population=[1,2,3,4], weights=[30,40,20,10])[0]

** R:**
```markdown
* **Data Visualization (R):**
```r
# Customizing the chart with Nando's branding and Rs currency
scale_fill_manual(values = c("FALSE" = "#F0A987", "TRUE" = "#E85D24")) +
scale_y_continuous(labels = label_comma(prefix = "Rs "))


### 🛠 Tech Stack
* ** Simulation:** '''Python (Pandas)
import pandas as pd
* ** Database:** '''MySQL
* ** Visualization:** '''R 
library(ggplot2)

### 📊 Performance Analysis
![Weekly Revenue Analysis](charts/chart4_weekly.png)

### 🗄️ Database Schema
```sql
CREATE TABLE sales (
    transaction_id INT PRIMARY KEY,
    timestamp DATETIME,
    item_name VARCHAR(100),
    price DECIMAL(10, 2) -- In Rs
);'''
### 💡 Optimization Logic
The system analyzes the `total_sold` metrics from MySQL to calculate a **Safety Stock Level** for the following week. 

Using the formula:
*Next Week Order = (Average Daily Sales * 7) + (Standard Deviation * 1.65)*

This ensures that high-demand items like **"Full Chicken"** or **"PERi-PERi Chips"** remain in stock even during unexpected weekend surges.

git init
git add .
git commit -m "Finalized Nando's Stock Optimizer Portfolio Project"

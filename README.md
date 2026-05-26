# Churn Analysis and Customer Intelligence Pipeline

## 1. Project Overview
This repository contains an end-to-end churn analytics pipeline developed for an Over-The-Top (OTT) subscription platform. The analysis focuses on leveraging multi-dimensional datasets encompassing customer demographics, subscription tiers, and customer support interactions to quantify revenue leakage and identify high-risk subscriber segments.

**Author:** Siddhant Gudwani  
**Domain:** Data Analytics / Customer Intelligence

## 2. Business Objective
In the highly competitive OTT sector, customer retention is a critical metric for long-term sustainability. The primary objective of this analysis is to identify high-risk subscribers prior to cancellation. By diagnosing the behavioral signals that precede churn, the project aims to define actionable retention strategies, thereby minimizing Monthly Recurring Revenue (MRR) leakage and maximizing Customer Lifetime Value (CLTV).

## 3. Technology Stack
- **Languages & Libraries:** Python (`numpy`, `pandas`, `matplotlib`, `seaborn`)
- **Database:** SQLite (`sqlite3`)
- **Core Competencies:** Relational Data Extraction, Exploratory Data Analysis (EDA), Feature Engineering, Performance Optimization

## 4. Methodology
The analytical workflow is structured into the following key phases:
1. **Relational Data Extraction:** Connecting Python to local SQLite databases to extract and merge multi-table datasets (Customer, Subscription, Support).
2. **Data Cleaning & Importation:** Standardizing data types, handling missing values, and renaming columns for consistency using `pandas` and `numpy`.
3. **Advanced Feature Engineering:** Formulating new calculated metrics, including customer tenure, cohort aging, and individualized churn risk scores.
4. **Exploratory Data Analysis (EDA):** Utilizing aggregations, group-by operations, and pivot tables to uncover underlying trends.
5. **Data Visualization:** Developing robust behavioral visualizations using `matplotlib` and `seaborn` to highlight critical churn drivers.
6. **Executive Reporting:** Synthesizing technical output into strategic, data-driven business recommendations.

## 5. Key Findings and Strategic Recommendations
- **Aggregate Metrics:** The analysis identified an overall churn rate of 28.6%, corresponding to a retention rate of 71.4%.
- **High-Risk Segment Analysis:** Subscribers on monthly contracts exhibited a churn rate of 55.6%, which is 6.7 times higher than the annual-contract rate (8.3%).
- **Revenue Implications:** The elevated churn rate within the monthly cohort resulted in substantial MRR leakage and significant erosion of CLTV among at-risk customers.
- **Support Intelligence:** Correlation analysis revealed that escalated support interactions were disproportionately concentrated among customers who eventually churned, indicating a direct link between customer service satisfaction and retention.
- **Actionable Takeaways:** Implement targeted contract-migration strategies to transition high-risk monthly subscribers to annual plans, and proactively address escalated support tickets to mitigate involuntary churn.

## 6. Database Architecture
The underlying database (`customer_churn.db`) consists of three primary relational tables:
- **`db_customer`**: Captures customer demographic profiles (e.g., ID, name, country, state, gender, date of birth, interests).
- **`db_subscription`**: Details subscription parameters (e.g., start date, plan type, contract type, renewal and cancellation dates, monthly charges).
- **`db_support`**: Logs customer support interactions (e.g., complaint dates, escalations, CSAT scores).

## 7. Installation and Execution Guide
### Prerequisites
Ensure that Python 3.x is installed on the local system along with pip.

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd churn-analysis
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. Install the necessary libraries by executing:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. **Execute the Analysis:**
   The primary analysis is contained within the Jupyter Notebook. Launch the notebook server:
   ```bash
   jupyter notebook churn_analysis.ipynb
   ```
   The notebook will automatically interface with the provided `customer_churn.db` SQLite database and raw data files.

---
*Note: The insights derived from this analysis are applicable to broader subscription-based business models, including SaaS, E-commerce, Fintech, and Adtech industries.*

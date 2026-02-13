# 📊 HR Job Data Collection Project

## 📌 Project Overview

This project focuses on collecting and analyzing Human Resource (HR) job postings from online job platforms using Python and public APIs.

The objective was to gather **1,000 structured HR-related job observations**, clean the data, and export it into a CSV dataset suitable for analysis.

---

# 🌍 Data Sources

## 1️⃣ Remote OK

**Website:** https://remoteok.com  
**API Endpoint:** https://remoteok.com/api  

### Description
Remote OK is a global remote job board that publishes remote job opportunities across various industries including:

- Human Resources  
- Software Development  
- Marketing  
- Finance  
- Design  
- Sales  

Remote OK provides a public JSON API endpoint that allows structured job data extraction without authentication.

### Data Collection Method
- Public JSON API extraction
- Python `requests` library used for API calls
- HR-related keyword filtering applied
- Duplicate job postings removed based on `job_id`
- Final dataset trimmed to exactly 1,000 rows

### Fields Collected
- source_site  
- job_id  
- job_title  
- company_name  
- location  
- salary_min  
- salary_max  
- date_posted  
- tags  
- job_description  
- scraped_date  

### Output File
`remoteok_hr_1000_dataset.csv`

---

## 2️⃣ Adzuna

**Website:** https://www.adzuna.com  
**Developer API:** https://developer.adzuna.com  

### Description
Adzuna is an international job search engine that aggregates job listings from thousands of job boards and employer websites across multiple countries including:

- United States  
- United Kingdom  
- Australia  
- India  

Adzuna provides an official developer API that allows structured job data retrieval using authentication credentials.

### Data Collection Method
- Official Adzuna API used
- Authentication via `app_id` and `app_key`
- Multiple keyword searches related to HR
- Pagination used to collect large volumes of data
- Duplicate job postings removed using `job_id`
- Data cleaned and standardized before export

### Fields Collected
- source_site  
- job_id  
- job_title  
- company_name  
- location_city  
- location_country  
- salary_min  
- salary_max  
- salary_currency  
- contract_type  
- category  
- created_date  
- job_description  
- redirect_url  
- scraped_date  

### Output File
`adzuna_hr_jobs_1000.csv`

---

# ⚙️ Technologies Used

- Python  
- Requests  
- Pandas  
- JSON API extraction  
- CSV export  

---

# 🧹 Data Cleaning Process

The following cleaning steps were applied:

- Removed duplicate job postings using `job_id`
- Standardized date format to YYYY-MM-DD
- Ensured numeric salary fields
- Filtered HR-related roles using keywords such as:
  - HR
  - Human Resource
  - Recruiter
  - Talent Acquisition
  - People Operations
- Exported final dataset to CSV format

---

# 📊 Dataset Size

Each dataset contains:

- **1,000 structured HR job observations**
- Cleaned and formatted for further analysis
- Suitable for statistical or HR analytics research

---

# 📅 Data Collection Date

Collected using Python scripts during the project development period.

---

# 🎯 Project Objective

The purpose of this project is to:

- Demonstrate API-based data extraction
- Collect structured HR job market data
- Apply data cleaning techniques
- Create reproducible datasets for analysis
- Meet academic requirements for minimum observations

---

# 📌 Disclaimer

All data was collected using publicly available APIs in accordance with platform accessibility at the time of collection. The dataset is intended for academic and research purposes only.

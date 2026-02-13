import requests
import pandas as pd
from datetime import datetime
import time

APP_ID = "" #app id heree
APP_KEY = "" #removed


# SETTINGS

COUNTRY = "us"  #  (uk, au, in)
KEYWORDS = ["hr manager", "human resource", "recruiter", "talent acquisition"]
RESULTS_PER_PAGE = 50
TOTAL_PAGES = 20   # 20 pages × 50 = 1000 jobs

all_jobs = []

print("Starting download...")

for keyword in KEYWORDS:
    for page in range(1, TOTAL_PAGES + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/{page}"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": RESULTS_PER_PAGE,
            "what": keyword,
            "content-type": "application/json"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            jobs = data.get("results", [])

            for job in jobs:
                all_jobs.append({
                    "source_site": "Adzuna",
                    "job_id": job.get("id"),
                    "job_title": job.get("title"),
                    "company_name": job.get("company", {}).get("display_name"),
                    "location_city": job.get("location", {}).get("area", [None])[0],
                    "location_country": COUNTRY.upper(),
                    "salary_min": job.get("salary_min"),
                    "salary_max": job.get("salary_max"),
                    "salary_currency": job.get("salary_currency"),
                    "contract_type": job.get("contract_type"),
                    "category": job.get("category", {}).get("label"),
                    "created_date": job.get("created"),
                    "job_description": job.get("description"),
                    "redirect_url": job.get("redirect_url"),
                    "scraped_date": datetime.today().strftime('%Y-%m-%d')
                })

            print(f"Downloaded page {page} for keyword '{keyword}'")

            time.sleep(1)  

        else:
            print(f"Error on page {page}: {response.status_code}")

print("Download complete!")


# creating DATAFRAME
df = pd.DataFrame(all_jobs)

# Removing duplicates
df = df.drop_duplicates(subset=["job_id"])

# Converting created_date to proper format
df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce").dt.date

# Saving to CSV
df.to_csv("adzuna_hr_jobs_1000.csv", index=False)

print("File saved as adzuna_hr_jobs_1000.csv")
print(f"Total records collected: {len(df)}")

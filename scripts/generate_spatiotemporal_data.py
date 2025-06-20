import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Configuration
n_records = 500
n_sites = 5
start_time = datetime(2024, 1, 1)

# Generate site IDs
site_ids = [f"SITE_{i+1}" for i in range(n_sites)]

# Generate subject IDs
subject_ids = [f"SUBJ_{i+1:04d}" for i in range(n_records)]

# Generate dataset
data = []

for i in range(n_records):
    subject_id = subject_ids[i]
    site_id = random.choice(site_ids)
    scan_time = start_time + timedelta(
        days=np.random.randint(0, 365), hours=np.random.randint(0, 24)
    )
    age = np.random.normal(loc=30, scale=10)
    sex = random.choice(["M", "F"])
    motion_score = abs(np.random.normal(0.05, 0.03))
    qc_pass = "PASS" if motion_score < 0.1 else "FAIL"

    data.append(
        {
            "subject_id": subject_id,
            "site_id": site_id,
            "scan_time": scan_time.isoformat(),
            "age": round(age, 1),
            "sex": sex,
            "motion_score": round(motion_score, 3),
            "qc_pass": qc_pass,
        }
    )

df = pd.DataFrame(data)

# Inject some errors for QC purposes
df.loc[5, "age"] = -1  # invalid age
df.loc[10, "motion_score"] = 1.5  # extreme motion
df.loc[20, "sex"] = "X"  # invalid category

# Save to CSV
df.to_csv("data/spatiotemporal_sample.csv", index=False)
print("✅ Simulated spatiotemporal dataset saved to data/spatiotemporal_sample.csv")

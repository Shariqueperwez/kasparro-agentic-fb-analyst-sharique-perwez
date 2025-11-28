import pandas as pd
import os
from datetime import datetime, timedelta

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Generate 28 days of data
dates = [datetime(2025, 1, 1) + timedelta(days=i) for i in range(28)]
data = []

for date in dates:
    # First 3 weeks: Good performance (High Sales)
    if date.day < 21:
        spend = 100
        clicks = 50   # 5% CTR
        revenue = 300 # 3.0 ROAS
    # Last week: BAD performance (Crash!)
    else:
        spend = 100
        clicks = 15   # 1.5% CTR (Drastic Drop)
        revenue = 120 # 1.2 ROAS (Loss)

    data.append({
        "date": date.strftime("%Y-%m-%d"),
        "campaign_name": "Summer Sale",
        "adset_name": "Adset_Broad_Targeting",
        "creative_type": "Video",
        "creative_message": "Buy one get one free limited time",
        "spend": spend,
        "impressions": 1000,
        "clicks": clicks,
        "ctr": clicks / 1000,
        "purchases": int(clicks * 0.1),
        "revenue": revenue,
        "roas": revenue / spend,
        "audience_type": "Broad",
        "platform": "Facebook",
        "country": "US"
    })

df = pd.DataFrame(data)
df.to_csv("data/synthetic_fb_ads_undergarments.csv", index=False)
print("✅ Data created with a massive performance drop in the last week.")
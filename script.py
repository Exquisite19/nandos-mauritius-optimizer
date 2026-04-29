import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# --- Config ---
MENU_ITEMS = {
    "Chicken Burger":      55,
    "Peri-Peri Chicken":   89,
    "Chicken Wrap":        65,
    "Veggie Burger":       58,
    "Chips":               29,
    "Coleslaw":            18,
    "Corn on the Cob":     22,
    "Bottomless Drink":    25,
    "Bottled Water":       15,
    "Halloumi Sticks":     45,
}

STAFF = ["Thabo", "Leila", "Priya", "Marcus", "Zanele", "Dev"]

# Peak-hour weights (0=midnight ... 23=11pm)
HOUR_WEIGHTS = [
    0,0,0,0,0,0,  # 12am-5am: closed
    1,2,3,4,5,6,  # 6am-11am: morning ramp
    10,12,14,      # 12pm-2pm: lunch peak
    8,6,5,         # 3pm-5pm: afternoon
    12,14,10,8,5,3 # 6pm-11pm: dinner peak
]

records = []
start_date = datetime(2024, 1, 1)

for day_offset in range(180):  # 6 months of data
    date = start_date + timedelta(days=day_offset)
    is_weekend = date.weekday() >= 5

    # More transactions on weekends
    n_transactions = random.randint(80, 120) if is_weekend else random.randint(50, 85)

    for _ in range(n_transactions):
        hour = random.choices(range(24), weights=HOUR_WEIGHTS)[0]
        minute = random.randint(0, 59)
        timestamp = date.replace(hour=hour, minute=minute)

        # Each transaction has 1-4 items
        n_items = random.choices([1,2,3,4], weights=[30,40,20,10])[0]
        items = random.choices(list(MENU_ITEMS.keys()), k=n_items)

        for item in items:
            price = MENU_ITEMS[item]
            staff = random.choice(STAFF)
            records.append({
                "timestamp":    timestamp,
                "date":         date.date(),
                "hour":         hour,
                "day_of_week":  date.strftime("%A"),
                "item":         item,
                "price":        price,
                "staff":        staff,
                "is_weekend":   is_weekend
            })

df = pd.DataFrame(records)
df = df.sort_values("timestamp").reset_index(drop=True)
df.to_csv("nandos_sales.csv", index=False)

print(f"✅ Done! {len(df):,} rows saved to nandos_sales.csv")
print(df.head())



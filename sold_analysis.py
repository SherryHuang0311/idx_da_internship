import pandas as pd
import glob

# find all sold CSV files
files = sorted(glob.glob("CRMLSSold*.csv"))

print("Files found:", len(files))

# combine them
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# save output
df.to_csv("combined_sold.csv", index=False)

print("Total rows:", len(df))
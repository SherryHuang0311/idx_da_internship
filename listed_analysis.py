import pandas as pd
import glob

# find all listing CSV files
files = sorted(glob.glob("CRMLSListing*.csv"))

print("Files found:", len(files))

# combine all files
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# save combined file
df.to_csv("combined_listed.csv", index=False)

print("Total rows:", len(df))
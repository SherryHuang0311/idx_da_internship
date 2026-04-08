import pandas as pd
import glob
import matplotlib.pyplot as plt

# find all sold CSV files
files = sorted(glob.glob("CRMLSSold*.csv"))

print("Files found:", len(files))

# combine them
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# save output
df.to_csv("combined_sold.csv", index=False)

print("Total rows:", len(df))

# load data
sold = pd.read_csv("combined_sold.csv", low_memory=False)

# -------------------------
# basic exploration
# -------------------------
print(sold.head())
print(sold.shape)
# 591195, 84

# column names
sold.columns

# data types
sold.dtypes
# everything is messy objects 

print(sold.describe())
print(sold["City"].value_counts().head(20))
# sold most houses in LA, SD, Irvine, San Jose (California)


# check missing values
missing = sold.isnull().sum()
missing_pct = (missing / len(sold)) * 100

missing_df = pd.DataFrame({
    "missing_count": missing,
    "missing_pct": missing_pct
}).sort_values("missing_pct", ascending=False)

all_na_cols = missing_df[missing_df["missing_pct"] == 100].index.tolist()
# ALL NA: 'AboveGradeFinishedArea', 'FireplacesTotal', 'ElementarySchoolDistrict', 'CoveredSpaces', 'MiddleOrJuniorSchoolDistrict'

high_missing = missing_pct[missing_pct > 90]
high_missing_cols = high_missing.index.tolist()
print(high_missing_cols)

core_cols = [
    "ClosePrice",
    "ListPrice",
    "CloseDate",
    "City",
    "CountyOrParish",
    "PropertyType",
    "BedroomsTotal",
    "BathroomsTotalInteger",
    "LivingArea",
    "LotSizeSquareFeet",
    "YearBuilt",
    "DaysOnMarket",
    "Latitude",
    "Longitude"
]

drop_cols = [col for col in high_missing_cols if col not in core_cols]

keep_cols = [col for col in df.columns if col not in drop_cols]

sold_clean = sold[keep_cols]
# 14 columns dropped 

# Columns with more than 90% missing values were identified and considered for removal. 
# However, core market-related variables (e.g., price, location, property characteristics) were retained even if partially missing, as they are essential for analysis. 
# Non-essential metadata fields with high missingness were dropped.

# Check property categories
sold['PropertyType'].unique()

print(sold["PropertyType"].value_counts(dropna=False))
# property types mostly residential, residential lease, land, manufactured in park, relatively fewer commercial or business



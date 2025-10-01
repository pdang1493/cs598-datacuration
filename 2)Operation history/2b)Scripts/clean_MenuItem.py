"""
Data Cleaning Script: MenuItem.csv – Standardizing Price Fields

This script processes and standardizes the 'price' and 'high_price' columns
in the MenuItem.csv dataset to ensure consistent numeric formatting for downstream analysis.

Cleaning Tasks Performed:
- Loads the raw dataset from MenuItem.csv.
- Defines a `clean_price()` function that:
    - Converts written words (e.g., "two dollars", "three and a half") to numeric floats.
    - Handles fractions and mixed numbers (e.g., "2 1/2", "3/4").
    - Removes currency symbols and unwanted characters.
    - Returns NaN for unprocessable values.
- Applies the cleaning function to both 'price' and 'high_price' columns.
- Stores cleaned values in new columns: 'price_cleaned' and 'high_price_cleaned'.
- Reorders columns for side-by-side comparison of original vs cleaned values.
- Prints a preview of cleaned results and summary of changed values.
- Saves the cleaned DataFrame as MenuItem_cleaned.csv with 'NaN' as placeholder for missing values.

Dependencies:
- pandas
- numpy
- re (regex)
- word2number (w2n)

Outputs:
- Cleaned dataset: MenuItem_cleaned.csv
- Terminal summary of how many price values were altered

Use Case:
- Supports Use Case U1 by ensuring all price values are numeric and analyzable (e.g., filtering, sorting, aggregation).
"""


import pandas as pd
import numpy as np
import re
from word2number import w2n

# Load the data
df = pd.read_csv('MenuItem.csv')


def clean_price(value):
    if pd.isnull(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    
    value = str(value).strip().lower()

    # Remove $ signs and unwanted characters (but keep fractions)
    value = re.sub(r'[^a-z0-9./ ]', '', value)

    try:
        # Convert written numbers like "two", "five"
        # Fix common phrasing like "three and a half"
        if 'and a half' in value:
            parts = value.split('and a half')
            value = str(w2n.word_to_num(parts[0].strip())) + '.5'
        else:
            value = str(w2n.word_to_num(value))

        return float(value)
    except:
        pass

    try:
        # Handle fractions like "3 1/2"
        if ' ' in value:
            whole, frac = value.split(' ')
            num, denom = frac.split('/')
            return float(whole) + float(num) / float(denom)
        elif '/' in value:
            num, denom = value.split('/')
            return float(num) / float(denom)
    except:
        pass

    try:
        return float(value)
    except:
        return np.nan

# Clean both price columns
df['price_cleaned'] = df['price'].apply(clean_price)
df['high_price_cleaned'] = df['high_price'].apply(clean_price)

# Reorder columns for easier comparison
cols = list(df.columns)
for col in ['price_cleaned', 'high_price_cleaned']:
    cols.remove(col)

cols.insert(cols.index('price') + 1, 'price_cleaned')
cols.insert(cols.index('high_price') + 1, 'high_price_cleaned')

df = df[cols]

# Preview cleaned values
print(df[['price', 'price_cleaned', 'high_price', 'high_price_cleaned']].head(20))

#  Save cleaned version
df.to_csv('MenuItem_cleaned.csv', index=False, na_rep='NaN')

print("Price cleaned changes:", (df['price'].astype(str) != df['price_cleaned'].astype(str)).sum())
print("High price cleaned changes:", (df['high_price'].astype(str) != df['high_price_cleaned'].astype(str)).sum())

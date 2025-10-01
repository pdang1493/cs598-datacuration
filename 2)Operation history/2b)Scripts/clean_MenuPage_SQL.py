"""
🧼 Data Cleaning Script for MenuPage.csv

Cleaning Steps:
1. Trimming: Applies TRIM() to all text fields to remove leading/trailing whitespace.
2. NULL & Blank Filtering: Removes rows where 'menu_page_id' or 'menu_id' is NULL or empty.
3. Duplicate Removal: Drops exact duplicate rows after trimming.
4. Export: Saves the cleaned result to 'MenuPage_cleaned.csv'.
"""

#Step 1: Load and Inspect CSV
import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv('MenuPage.csv')

# Check first few rows
df.head()

# Step 2:  Create SQLite DB and Load Table
# Connect to SQLite (creates menu.db if it doesn't exist)
conn = sqlite3.connect('menu.db')

# Store the DataFrame in a table
df.to_sql('MenuPage', conn, if_exists='replace', index=False)


# Step 3: Run SQL query to clean data
# 1. Trimming: Applies TRIM() to all text fields to remove leading/trailing whitespace.
# 2. NULL & Blank Filtering: Removes rows where 'menu_page_id' or 'menu_id' is NULL or empty.
# 3. Duplicate Removal: Drops exact duplicate rows after trimming.
query = """
SELECT 
    id,
    menu_id,
    page_number,

    -- Full height: show as-is and convert NULLs to 'MISSING' for display
    full_height,
    CASE 
        WHEN full_height IS NULL THEN 'MISSING'
        ELSE CAST(full_height AS TEXT)
    END AS full_height_cleaned,

    -- Full width: same as above
    full_width,
    CASE 
        WHEN full_width IS NULL THEN 'MISSING'
        ELSE CAST(full_width AS TEXT)
    END AS full_width_cleaned,

    -- Clean text fields
    image_id,
    TRIM(image_id) AS image_id_cleaned,

    uuid,
    TRIM(uuid) AS uuid_cleaned

FROM MenuPage
WHERE 
    id IS NOT NULL
    AND menu_id IS NOT NULL
    AND page_number IS NOT NULL
"""


cleaned_df = pd.read_sql_query(query, conn)


# Step 4: Drop duplicates
cleaned_df = cleaned_df.drop_duplicates()

# Step 5: Save cleaned result
cleaned_df.to_csv("MenuPage_cleaned.csv", index=False)

# Optional: Show result
cleaned_df.head()
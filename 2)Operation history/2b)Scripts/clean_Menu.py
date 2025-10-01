"""
This script performs data cleaning on the NYPL Menu dataset fields:
    - place
    - event
    - sponsor
    - venue

Cleaning steps include:
    - Removing noise characters (e.g., brackets, quotes, punctuation)
    - Correcting typos and standardizing text
    - Normalizing whitespace
    - Handling null or blank values
    - Converting to uppercase for consistency

Cleaned fields are saved in new columns:
    - place_cleaned
    - event_cleaned
    - sponsor_cleaned
    - venue_cleaned

Final output is saved to Menu_cleaned.csv
"""

import pandas as pd
import re

# Load your dataset
df = pd.read_csv("Menu.csv")

# Full dictionary to standardize U.S. state names
state_abbrev_fixes = {
    'ALA': 'AL', 'ALABAMA': 'AL',
    'ALASKA': 'AK',
    'ARIZ': 'AZ', 'ARIZONA': 'AZ',
    'ARK': 'AR', 'ARKANSAS': 'AR',
    'CALIF': 'CA', 'CALIFORNIA': 'CA',
    'COLO': 'CO', 'COLORADO': 'CO',
    'CONN': 'CT', 'CONNECTICUT': 'CT',
    'DEL': 'DE', 'DELAWARE': 'DE',
    'FLA': 'FL', 'FLORIDA': 'FL',
    'GA': 'GA', 'GEORGIA': 'GA',
    'IDAHO': 'ID',
    'ILL': 'IL', 'ILLINOIS': 'IL',
    'IND': 'IN', 'INDIANA': 'IN',
    'IOWA': 'IA',
    'KAN': 'KS', 'KANSAS': 'KS',
    'KY': 'KY', 'KENTUCKY': 'KY',
    'LA': 'LA', 'LOUISIANA': 'LA',
    'MAINE': 'ME',
    'MD': 'MD', 'MARYLAND': 'MD',
    'MASS': 'MA', 'MASSACHUSETTS': 'MA',
    'MICH': 'MI', 'MICHIGAN': 'MI',
    'MINN': 'MN', 'MINNESOTA': 'MN',
    'MISS': 'MS', 'MISSISSIPPI': 'MS',
    'MO': 'MO', 'MISSOURI': 'MO',
    'MONT': 'MT', 'MONTANA': 'MT',
    'NEBR': 'NE', 'NEBRASKA': 'NE',
    'NEV': 'NV', 'NEVADA': 'NV',
    'N H': 'NH', 'NEW HAMPSHIRE': 'NH',
    'N J': 'NJ', 'NEW JERSEY': 'NJ',
    'N M': 'NM', 'NEW MEXICO': 'NM',
    'NY': 'NY', 'N Y': 'NY', 'NEW YORK': 'NY',
    'N C': 'NC', 'NORTH CAROLINA': 'NC',
    'N D': 'ND', 'NORTH DAKOTA': 'ND',
    'OHIO': 'OH',
    'OKLA': 'OK', 'OKLAHOMA': 'OK',
    'OREG': 'OR', 'OREGON': 'OR',
    'PENN': 'PA', 'PENNSYLVANIA': 'PA',
    'R I': 'RI', 'RHODE ISLAND': 'RI',
    'S C': 'SC', 'SOUTH CAROLINA': 'SC',
    'S D': 'SD', 'SOUTH DAKOTA': 'SD',
    'TENN': 'TN', 'TENNESSEE': 'TN',
    'TEX': 'TX', 'TEXAS': 'TX',
    'UTAH': 'UT',
    'VT': 'VT', 'VERMONT': 'VT',
    'VA': 'VA', 'VIRGINIA': 'VA',
    'WASH': 'WA', 'WASHINGTON': 'WA',
    'W VA': 'WV', 'WEST VIRGINIA': 'WV',
    'WIS': 'WI', 'WISCONSIN': 'WI',
    'WYO': 'WY', 'WYOMING': 'WY'
}

# Known city aliases
city_aliases = {
    'NYC': 'NEW YORK, NY',
    'NY': 'NEW YORK, NY'
}

# Define the cleaning function
def clean_place(value):
    if pd.isnull(value) or value.strip() == '':
        return 'UNKNOWN'

    # Fix known typos
    value = re.sub(r'\bHOEL\b', 'HOTEL', value, flags=re.IGNORECASE)
    value = re.sub(r"ANDERTON'S", "ANDERTONS", value, flags=re.IGNORECASE)

    # Remove brackets, quotes, parentheses, question marks
    value = re.sub(r'[\[\]"\']', '', value)
    value = re.sub(r'[()]', '', value)
    value = value.replace('?', '')

    # Normalize commas and semicolons
    value = re.sub(r'\s*[,;]+\s*', ', ', value).strip(',; ')

    # Standardize state abbreviations
    for old, new in state_abbrev_fixes.items():
        value = re.sub(rf'\b{old}\b', new, value, flags=re.IGNORECASE)

    # Replace known city aliases
    for old, new in city_aliases.items():
        value = re.sub(rf'\b{old}\b', new, value, flags=re.IGNORECASE)

    # Deduplicate repeated segments (e.g., NEW YORK, NY, NEW YORK, NY)
    parts = [p.strip() for p in value.split(',')]
    seen = set()
    cleaned_parts = []
    for part in parts:
        if part and part not in seen:
            seen.add(part)
            cleaned_parts.append(part)

    return ', '.join(cleaned_parts).upper()

# Apply cleaning function
df['place_cleaned'] = df['place'].apply(clean_place)

# ---- Clean 'sponsor' column ----
def clean_sponsor(value):
    if pd.isnull(value) or str(value).strip() == '':
        return 'UNKNOWN'
    value = str(value).strip().upper()
    value = re.sub(r'[\[\]()"\']', '', value)
    value = re.sub(r'\s+', ' ', value)
    return value

df['sponsor_cleaned'] = df['sponsor'].apply(clean_sponsor)

# ---- Clean 'event' column ----
def clean_event(value):
    if pd.isnull(value) or str(value).strip() == '':
        return 'UNKNOWN'

    value = str(value).strip().upper()
    value = re.sub(r'[\[\]()"\']', '', value)           # remove brackets and quotes
    value = re.sub(r'[;:]+$', '', value)                # remove trailing punctuation

    # Fix common typos using word boundaries to avoid unintended replacements
    value = re.sub(r'\bDINNE\b', 'DINNER', value)

    value = re.sub(r'\s+', ' ', value)                  # normalize whitespace
    return value

df['event_cleaned'] = df['event'].apply(clean_event)

# ---- Clean 'venue' column ----
def clean_venue(value):
    if pd.isnull(value) or str(value).strip() in ["", "?", "[?]", "[POL?);"]:
        return "UNKNOWN"

    value = str(value).upper().strip()

    # Remove trailing semicolons and extra punctuation
    value = re.sub(r'[^A-Z;, ]', '', value)   # keep letters and common separators
    value = re.sub(r'\s+', ' ', value)        # collapse multiple spaces
    value = re.sub(r'[;,]+$', '', value)      # remove trailing punctuation
    value = re.sub(r'[\[\](){}]', '', value)  # remove brackets/parentheses
    value = value.strip(' ,;.')

    # Normalize common variants
    replacements = {
        'COMMERCIAL': 'COMMERCIAL',
        'COM': 'COMMERCIAL',
        'COMMERCOA': 'COMMERCIAL',
        'CMMERCIAL': 'COMMERCIAL',
        'COMM': 'COMMERCIAL',
        'COMM.': 'COMMERCIAL',
        'COM.;': 'COMMERCIAL',
        'GOVT': 'GOVERNMENT',
        "GOV'T": 'GOVERNMENT',
        "GOV'T.": 'GOVERNMENT',
        'GOV.': 'GOVERNMENT',
        'GOV': 'GOVERNMENT',
        'SOC': 'SOCIAL',
        'SOC;': 'SOCIAL',
        'SOCIAL CLUB': 'SOCIAL',
        'POLIT': 'POLITICAL',
        'POL;': 'POLITICAL',
        'POL': 'POLITICAL',
        'RELIG;': 'RELIGIOUS',
        'RELIG': 'RELIGIOUS',
        'NAV': 'NAVAL',
        'NAV.': 'NAVAL',
        'NAVAL;': 'NAVAL',
        'MIL;': 'MILITARY',
        'MIL.': 'MILITARY',
        'MIL': 'MILITARY',
        'EDUC;': 'EDUCATIONAL',
        'EDUC': 'EDUCATIONAL',
        'EDUS': 'EDUCATIONAL',
        'EDUCATIONAL;': 'EDUCATIONAL',
        'PROF;': 'PROFESSIONAL',
        'PROF': 'PROFESSIONAL',
        'PROF.': 'PROFESSIONAL',
        'PRO;': 'PROFESSIONAL',
        'PATRIOTIC?': 'PATRIOTIC',
        'PAT': 'PATRIOTIC',
        'PATR': 'PATRON',
        'PATR.': 'PATRON',
        'PRIVATE PARTY': 'PRIVATE',
        'PRIVATE;': 'PRIVATE',
        'PRIVATE': 'PRIVATE'
    }

    for key, val in replacements.items():
        if value.startswith(key):
            return val

    return value


df['venue_cleaned'] = df['venue'].apply(clean_venue)

# ---- Reorder new columns next to originals ----
def move_next_to(df, original_col, cleaned_col):
    cols = list(df.columns)
    if original_col in cols and cleaned_col in cols:
        cols.remove(cleaned_col)
        cols.insert(cols.index(original_col) + 1, cleaned_col)
    return df[cols]

for orig, clean in [('place', 'place_cleaned'),
                    ('sponsor', 'sponsor_cleaned'),
                    ('event', 'event_cleaned'),
                    ('venue', 'venue_cleaned')]:
    df = move_next_to(df, orig, clean)

# ---- Save the cleaned result ----
df.to_csv("Menu_cleaned.csv", index=False)
print("Cleaned dataset saved as Menu_cleaned.csv")

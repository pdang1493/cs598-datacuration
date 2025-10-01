# CS598 Data Curation Project (Fall 2025)

**Student:** Phu Dang  
**Course:** CS598 Data Curation (UIUC)  
**Dataset:** New York Public Library (NYPL) Historical Menus

---

## 📌 Overview
This project implements an **end-to-end reproducible data curation workflow** for the NYPL Historical Menus dataset.  
It demonstrates the **USGS Data Lifecycle model**: acquisition, assessment, cleaning, integration, documentation, and dissemination.

---

## 📂 Repository Structure
- `1)YesWorkflow/` → Workflow provenance (YesWorkflow scripts + diagrams)  
- `2)Operation history/` → Cleaning history and reproducible scripts  
   - `2a)OpenRefine(Dish)/` → OpenRefine JSON history for Dish table  
   - `2b)Scripts/` → Jupyter notebooks & Python scripts for cleaning  
- `3)Queries(MenuPage)/` → SQL queries for MenuPage curation  
- `4)Original and Cleaned datasets/`  
   - `Original/` → Raw input datasets (not pushed due to GitHub 100MB limit)  
   - `Cleaned/` → Curated versions (samples included)  
- `DataLinks.txt` → Links to download the full dataset  
- `README.md` → This file  

---

## ⚠️ Note on Data Size
The **full CSVs** (Menu, MenuItem, MenuPage, Dish) exceed GitHub’s 100MB file limit.  
They are **not included in this repo**, but can be downloaded here:  
👉 [NYPL Menus Dataset](https://menus.nypl.org/data)  

This repo includes **sample CSVs** for reproducibility.

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/pdang1493/cs598-datacuration.git
   cd cs598-datacuration
Open Jupyter notebooks in 2)Operation history/2b)Scripts/ to reproduce the cleaning.

Run SQL scripts in 3)Queries(MenuPage)/ against the dataset.

📑 References
New York Public Library. What’s on the Menu? https://menus.nypl.org/

U.S. Geological Survey (USGS) Data Lifecycle Model. https://www.usgs.gov/datamanagement/data-lifecycle
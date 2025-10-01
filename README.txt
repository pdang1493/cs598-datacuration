
Team 16 - Karaoke Masters

=========================

NYPL Historical Menus – Data Cleaning Project 
---------------------------------------------  
This project involved cleaning and standardizing the NYPL Historical Menu dataset to support Use Case U1: enabling structured and consistent analysis of historical menu records. We focused on resolving data quality issues across multiple tables to support downstream analysis, including dish classification, pricing trends, and historical reconstructions.

Submission Contents  
-------------------

1. **Workflow Model**  
   • Located in `YesWorkflow/`  
   • Files included:  
     - `YesWorkflow.yw` – Annotated workflow script  
     - `YesWorkflow.gv` 
     - `YesWorkflow.dot` / `YesWorkflow.gv` – Graph representations  
     - `YesWorkflow.pdf` – Final rendered workflow diagram  

2. **Operation History**  
   • Located in `OpenRefine(Dish)/`  
   • File:  
     - `Dish_cleaned_OpenRefineHistory.json` – Full OpenRefine transformation history for `Dish.csv`  

     - `Dish_OpenRefine.txt` – Human-readable version of transformation steps applied to `Dish.csv`  

  **Other Scripts and Provenance Files**  
   • Located in `Scripts/`  
   • Files:  
     - `clean_MenuItem.py` – Cleans price-related fields using regex and `word2number`  
     - `clean_Menu.py` – Normalizes textual fields (`place`, `event`, `sponsor`, `venue`)  
     - `clean_MenuPage.sql` – SQL logic to trim and filter `MenuPage.csv`  

3. **Queries**  
   • Located in `Queries(MenuPage)/`  
   • File:  
     - `MenuPage_Query.sql` – SQL statements used to filter and clean the MenuPage dataset  

4. **Original (“Dirty”) and Cleaned Datasets**  
   • Located in `Cleaned_vs_Dirty_Data/`  
   ├── Original/  
   │   - `Menu.csv`  
   │   - `MenuItem.csv`  
   │   - `MenuPage.csv`  
   │   - `Dish.csv`  
   └── Cleaned/  
       - `Menu_cleaned.csv`  
       - `MenuItem_cleaned.csv`  
       - `MenuPage_cleaned.csv`  
       - `Dish_cleaned.csv`  

5. **Box Folder Link**  
   • Located in the root directory:  
   • File:  
     - `DataLinks.txt` – Plain text file containing the URL to the shared Box folder with all project materials  

Contact  
-------
• Phu Dang – phudang2@illinois.edu  
• Emily Scray – escray2@illinois.edu  

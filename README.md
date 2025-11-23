Milk Production Tracker

Overview

The Milk Production Tracker is a simple and efficient system designed to help small dairy farmers record and manage daily milk production.
It allows farmers to register their animals, store milk entries (morning/evening), and generate daily reports.
The system is lightweight, beginner-friendly, and runs on any computer using Python and SQLite.


Features

* Add farmers with contact details

* Add animals (cow/buffalo) with tag ID, breed, DOB, lactation date

* Record milk entries (morning & evening)

* View complete milk entry history

* Generate daily reports

* Auto-calculation of total milk per day

* CLI-based interface (easy to use)

* Data stored locally in SQLite database



Technologies / Tools Used

* Python 3

* SQLite3 (built-in database)

* Jupyter Notebook (testing & verification)

* Command Line Interface (CLI)

* Git & GitHub (version control)



---

Steps to Install & Run the Project

1. Clone or download the project

git clone https://github.com/yuvraj777-cyber/milk-production-tracker
cd milk-tracker

2. Create virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate

3. Run database setup

python3 src/db.py

4. Run the CLI application

python3 src/cli.py


---

Instructions for Testing

1. Add a farmer


2. Add an animal under that farmer


3. Add a milk entry for that animal


4. List milk entries


5. Generate daily report


6. Verify data in Jupyter Notebook using notebooks/day2_test.ipynb




---

CLI Menu Screenshots 

Adding farmer
<img width="535" height="265" alt="cli_add_farmer" src="https://github.com/user-attachments/assets/2a801a33-9cc5-4f82-8846-7462fcb0df50" />


Adding animal
<img width="535" height="304" alt="cli_add_animal" src="https://github.com/user-attachments/assets/40e14e99-8b01-4dfd-a532-49572f747eb5" />


Milk entry report
<img width="535" height="291" alt="cli_add_milk_entry" src="https://github.com/user-attachments/assets/0b58a62c-e6b2-4c58-a2a6-2fbc201d3075" />

Jupyter Notebook Screenshots

Jupyter notebook testing
<img width="1198" height="673" alt="jupyter_notebook_testing" src="https://github.com/user-attachments/assets/1371ae96-09e0-4c9f-b479-f84a058511d4" />

<img width="1212" height="586" alt="jupyter _add_farmer_add_animal_add_milk_entry_testing" src="https://github.com/user-attachments/assets/58542f62-ed5b-4b69-a8d6-e29084200acc" />




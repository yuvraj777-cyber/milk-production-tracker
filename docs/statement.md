Milk Production Tracker – Statement of the Project

1. Problem Statement

Small dairy farmers often record milk production in notebooks or loose papers.
These records are difficult to maintain and can easily be lost or damaged.
Farmers also cannot quickly calculate total daily milk output or track production per animal.
There is a need for a simple and digital system that helps farmers maintain accurate, structured records of milk production.


---

2. Scope of the Project

This project includes the following features:

Farmer registration

Animal registration under each farmer

Daily milk entry storing (morning & evening)

Automatic calculation of total milk per day

Listing of farmers, animals, and milk entries

Daily milk production report

A simple command-line user interface

SQLite database storage


This project DOES NOT include:

Graphical user interface (GUI)

Online/cloud database

Multi-user login system

Automated milk sensors



---

3. Functional Requirements

3.1 Farmer Management

Add new farmers with name, phone, and address.

Display list of all registered farmers.


3.2 Animal Management

Register animals under each farmer with tag ID, name, breed, DOB, and lactation start date.

View all animals or animals belonging to a specific farmer.


3.3 Milk Entry Management

Record daily milk entries for each animal (morning & evening).

Store optional notes for each entry.

Auto-calculate total liters per entry.


3.4 Reporting

Generate daily milk production report.

Calculate average milk per animal.

Display all previous milk entries.



---

4. Non-Functional Requirements

4.1 Usability

The CLI-based interface is simple, text-based, and beginner-friendly.

4.2 Reliability

SQLite ensures safe, consistent storage with proper foreign keys and unique tag IDs.

4.3 Performance

All operations execute quickly since dataset size is small.

4.4 Maintainability

The project is structured into db.py, models.py, and cli.py to allow easy updates.

4.5 Portability

Works on any system with Python installed (Windows, macOS, Linux).


---

5. System Architecture

The system uses a simple 3-layer architecture:

5.1 Database Layer (SQLite)

Stores all data in three tables:

farmers

animals

milk_entries


5.2 Model Layer (models.py + db.py)

Handles:

database connection

CRUD operations

business logic

reporting functions


5.3 Presentation Layer (cli.py + Jupyter Notebook)

CLI shows menu

Takes user input

Displays results of model functions



---

6. ER Diagram (Description)

Entities:

Farmer

id (PK)

name

phone

address


Animal

id (PK)

farmer_id (FK → Farmer.id)

tag_id (Unique)

name

dob

breed

lactation_start_date


MilkEntry

id (PK)

animal_id (FK → Animal.id)

entry_date

morning_liters

evening_liters

total_liters

notes

created_at


Relationships

Farmer 1 — N Animals

Animal 1 — N MilkEntries



---

7. Use Case Diagram (Text Explanation)

Actor: User / Operator

Use cases:

Add Farmer

Add Animal

Add Milk Entry

Generate Daily Report

List Farmers

List Animals

List Milk Entries


User interacts through the CLI to trigger functions.


---

8. Workflow (Process Flow of CLI)

1. User runs python3 src/cli.py


2. Main menu appears (1–8)


3. User chooses an action


4. System asks for necessary input


5. System calls the appropriate model function


6. Output displayed


7. User returns to the menu


8. Ends when user selects Exit




---

9. Testing Approach

Testing was done in two phases:

Phase 1: Jupyter Notebook Testing

Tested add_farmer, add_animal, add_milk_entry

Verified database entries

Checked reporting functions


Phase 2: CLI Testing

End-to-end tests through menu

Valid & invalid inputs

Checked all CRUD and reporting features



---

10. Challenges Faced

Initial import errors in Jupyter

Understanding SQLite foreign keys

Managing Python path for src folder

Learning Git & GitHub workflow

Handling user input safely in CLI



---

11. Learnings

DBMS basics

Python module structure

SQLite database connectivity

CLI application development

Git/GitHub version control

Basic software documentation



---

12. Conclusion

The Milk Production Tracker is a lightweight, efficient system for dairy farms to manage milk records digitally.
It meets all basic requirements, stores data safely, and provides easy reporting.
The project can be expanded into a GUI or web application in the future.

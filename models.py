# src/models.py
"""
Simple DB models for Milk Production Tracker.
Provides functions to add/list farmers and animals.
"""

import sqlite3
from datetime import datetime
from db import get_conn, init_db  # uses the db helper we created

# Ensure the database and tables exist (safe to call multiple times)
init_db()

# ----------------- Farmer functions -----------------
def add_farmer(name, phone=None, address=None):
    """
    Add a farmer.
    Returns the new farmer id.
    Raises ValueError if name is empty.
    """
    if not name or not str(name).strip():
        raise ValueError("Farmer name is required")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO farmers (name, phone, address) VALUES (?, ?, ?)",
                (name.strip(), phone, address))
    conn.commit()
    fid = cur.lastrowid
    conn.close()
    return fid

def list_farmers():
    """
    Return a list of farmers as sqlite3.Row objects.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, address FROM farmers ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_farmer(farmer_id):
    """
    Return a single farmer row or None.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM farmers WHERE id = ?", (farmer_id,))
    row = cur.fetchone()
    conn.close()
    return row

# ----------------- Animal functions -----------------
def add_animal(farmer_id, tag_id, name=None, dob=None, breed=None, lactation_start_date=None):
    """
    Add an animal belonging to a farmer.
    tag_id must be unique.
    Returns new animal ID.
    """
    if not tag_id or not str(tag_id).strip():
        raise ValueError("Tag ID is required")

    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO animals (farmer_id, tag_id, name, dob, breed, lactation_start_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (farmer_id, tag_id.strip(), name, dob, breed, lactation_start_date))

        conn.commit()
        aid = cur.lastrowid
    except sqlite3.IntegrityError:
        conn.rollback()
        raise ValueError("Duplicate tag_id or invalid farmer_id")
    finally:
        conn.close()

    return aid

def list_animals(farmer_id=None):
    conn = get_conn()
    cur = conn.cursor()

    if farmer_id:
        cur.execute("SELECT * FROM animals WHERE farmer_id = ?", (farmer_id,))
    else:
        cur.execute("SELECT * FROM animals ORDER BY id")

    rows = cur.fetchall()
    conn.close()
    return rows

def get_animal_by_tag(tag_id):
    """
    Return the animal row matching tag_id or None.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM animals WHERE tag_id = ?", (tag_id,))
    row = cur.fetchone()
    conn.close()
    return row

def add_milk_entry(animal_id, entry_date, morning_liters=0, evening_liters=0, notes=None):
    """
    Add a milk entry for an animal.
    Returns the new entry ID.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO milk_entries (animal_id, entry_date, morning_liters, evening_liters, total_liters, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            animal_id,
            entry_date,
            morning_liters,
            evening_liters,
            (morning_liters or 0) + (evening_liters or 0),
            notes,
        ),
    )
    conn.commit()
    entry_id = cur.lastrowid
    conn.close()
    return entry_id

def list_milk_entries():
    """
    Return all milk entries as sqlite3.Row objects.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM milk_entries ORDER BY entry_date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def total_milk_by_date(entry_date):
    """
    Return total milk produced on a given date.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT SUM(total_liters) FROM milk_entries WHERE entry_date = ?",
        (entry_date,),
    )
    result = cur.fetchone()[0]
    conn.close()
    return result or 0
def total_milk_by_animal(animal_id):
    """
    Return total milk produced by one animal.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT SUM(total_liters) FROM milk_entries WHERE animal_id = ?",
        (animal_id,),
    )
    result = cur.fetchone()[0]
    conn.close()
    return result or 0

def average_milk_per_animal():
    """
    Return average total milk per animal.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT animal_id, SUM(total_liters) as total FROM milk_entries GROUP BY animal_id"
    )
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return 0

    totals = [row["total"] for row in rows]
    return sum(totals) / len(totals)
    
# src/cli.py
"""
Simple command-line interface for Milk Production Tracker.
"""

from models import (
    add_farmer,
    list_farmers,
    add_animal,
    list_animals,
    add_milk_entry,
    list_milk_entries,
    total_milk_by_date,
    total_milk_by_animal,
    average_milk_per_animal,
)


def ask_int(prompt):
    """Ask for an integer safely."""
    while True:
        value = input(prompt).strip()
        if value == "":
            return None
        try:
            return int(value)
        except ValueError:
            print("Please enter a number (or press Enter to cancel).")


def ask_float(prompt):
    """Ask for a float safely, default 0 if empty."""
    while True:
        value = input(prompt).strip()
        if value == "":
            return 0.0
        try:
            return float(value)
        except ValueError:
            print("Please enter a number (e.g. 4 or 3.5).")


def menu():
    print("\n==============================")
    print("   MILK PRODUCTION TRACKER")
    print("==============================")
    print("1. Add Farmer")
    print("2. List Farmers")
    print("3. Add Animal")
    print("4. List Animals")
    print("5. Add Milk Entry")
    print("6. List Milk Entries")
    print("7. Daily Milk Report")
    print("8. Exit")
    return input("Enter choice (1-8): ").strip()


def handle_add_farmer():
    print("\n--- Add Farmer ---")
    name = input("Farmer name: ").strip()
    phone = input("Phone (optional): ").strip()
    address = input("Address (optional): ").strip()

    if not name:
        print("Name is required.")
        return

    fid = add_farmer(name, phone or None, address or None)
    print(f"✅ Farmer added with ID: {fid}")


def handle_list_farmers():
    print("\n--- Farmers ---")
    farmers = list_farmers()
    if not farmers:
        print("No farmers found.")
        return
    for f in farmers:
        print(
            f"[{f['id']}] {f['name']} | "
            f"Phone: {f['phone'] or '-'} | Address: {f['address'] or '-'}"
        )


def handle_add_animal():
    print("\n--- Add Animal ---")
    farmer_id = ask_int("Farmer ID (owner): ")
    if farmer_id is None:
        print("Cancelled.")
        return

    tag_id = input("Tag ID (unique): ").strip()
    name = input("Animal name (optional): ").strip()
    dob = input("DOB (YYYY-MM-DD, optional): ").strip()
    breed = input("Breed (optional): ").strip()
    lactation_start_date = input("Lactation start date (YYYY-MM-DD, optional): ").strip()

    try:
        aid = add_animal(
            farmer_id,
            tag_id,
            name or None,
            dob or None,
            breed or None,
            lactation_start_date or None,
        )
        print(f"✅ Animal added with ID: {aid}")
    except Exception as e:
        print("❌ Failed to add animal:", e)


def handle_list_animals():
    print("\n--- Animals ---")
    farmer_id = ask_int("Filter by Farmer ID (or Enter for all): ")
    animals = list_animals(farmer_id) if farmer_id else list_animals()
    if not animals:
        print("No animals found.")
        return
    for a in animals:
        print(
            f"[{a['id']}] Tag: {a['tag_id']} | Name: {a['name'] or '-'} "
            f"| Farmer ID: {a['farmer_id'] or '-'} | Breed: {a['breed'] or '-'}"
        )


def handle_add_milk_entry():
    print("\n--- Add Milk Entry ---")
    animal_id = ask_int("Animal ID: ")
    if animal_id is None:
        print("Cancelled.")
        return

    entry_date = input("Date (YYYY-MM-DD): ").strip()
    morning = ask_float("Morning liters (0 if none): ")
    evening = ask_float("Evening liters (0 if none): ")
    notes = input("Notes (optional): ").strip() or None

    try:
        mid = add_milk_entry(
            animal_id=animal_id,
            entry_date=entry_date,
            morning_liters=morning,
            evening_liters=evening,
            notes=notes,
        )
        print(f"✅ Milk entry added with ID: {mid}")
    except Exception as e:
        print("❌ Failed to add milk entry:", e)


def handle_list_milk_entries():
    print("\n--- Milk Entries ---")
    entries = list_milk_entries()
    if not entries:
        print("No milk entries found.")
        return
    for e in entries:
        print(
            f"[{e['id']}] Animal {e['animal_id']} | Date: {e['entry_date']} | "
            f"Morning: {e['morning_liters']} L | Evening: {e['evening_liters']} L | "
            f"Total: {e['total_liters']} L | Notes: {e['notes'] or '-'}"
        )


def handle_daily_report():
    print("\n--- Daily Milk Report ---")
    date = input("Date (YYYY-MM-DD): ").strip()
    total = total_milk_by_date(date)
    avg = average_milk_per_animal()
    print(f"Total milk on {date}: {total} liters")
    print(f"Average milk per animal (all dates): {avg:.2f} liters")


def main():
    while True:
        choice = menu()
        if choice == "1":
            handle_add_farmer()
        elif choice == "2":
            handle_list_farmers()
        elif choice == "3":
            handle_add_animal()
        elif choice == "4":
            handle_list_animals()
        elif choice == "5":
            handle_add_milk_entry()
        elif choice == "6":
            handle_list_milk_entries()
        elif choice == "7":
            handle_daily_report()
        elif choice == "8":
            print("Exiting. Bye! 👋")
            break
        else:
            print("Invalid choice, enter 1–8.")


if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk
import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect("dbname='university professor' user=postgres password=itsmyproject host=localhost port=5432")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def fetch_organizations_data(tree):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ORGANIZATIONS;")
        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", "end", values=(row[0], row[1]))

        conn.close()

def insert_organization_data(org_name_entry, org_sector_entry):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        org_name = org_name_entry.get()
        org_sector = org_sector_entry.get()

        cursor.execute("INSERT INTO ORGANIZATIONS (ORGANIZATION, ORGANIZATION_SECTOR) VALUES (%s, %s)",
                       (org_name, org_sector))

        conn.commit()
        conn.close()

        fetch_organizations_data()

        org_name_entry.delete(0, tk.END)
        org_sector_entry.delete(0, tk.END)

def delete_organization_data(org_name_entry):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        org_name = org_name_entry.get()

        cursor.execute("DELETE FROM ORGANIZATIONS WHERE ORGANIZATION = %s", (org_name,))

        conn.commit()
        conn.close()

        fetch_organizations_data()

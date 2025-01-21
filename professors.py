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

def fetch_professors_data(tree):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PROFESSORS;")
        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))  # Ensure column order is correct

        conn.close()

def insert_professor_data(first_name_entry, last_name_entry, university_id_entry):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        university_id = university_id_entry.get()

        cursor.execute("INSERT INTO PROFESSORS (FIRSTNAME, LASTNAME, UNIVERSITY_ID) VALUES (%s, %s, %s)",
                       (first_name, last_name, university_id))

        conn.commit()
        conn.close()

        fetch_professors_data()

        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        university_id_entry.delete(0, tk.END)

def delete_professor_data(first_name_entry, last_name_entry, university_id_entry):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        university_id = university_id_entry.get()

        cursor.execute("DELETE FROM PROFESSORS WHERE FIRSTNAME = %s AND LASTNAME = %s AND UNIVERSITY_ID = %s",
                       (first_name, last_name, university_id))

        conn.commit()
        conn.close()

        fetch_professors_data()

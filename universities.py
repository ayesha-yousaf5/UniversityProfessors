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

def fetch_universities_data(tree):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UNIVERSITIES;")
        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", "end", values=(row[0], row[1], row[2]))

        conn.close()

def insert_university_data(university_name_entry, university_city_entry):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        university_name = university_name_entry.get()
        university_city = university_city_entry.get()

        cursor.execute("INSERT INTO UNIVERSITIES (UNIVERSITY, UNIVERSITY_CITY) VALUES (%s, %s)",
                       (university_name, university_city))

        conn.commit()
        conn.close()

        fetch_universities_data()

        university_name_entry.delete(0, tk.END)
        university_city_entry.delete(0, tk.END)

def delete_university_data(university_name_entry):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        university_name = university_name_entry.get()

        cursor.execute("DELETE FROM UNIVERSITIES WHERE UNIVERSITY = %s", (university_name,))

        conn.commit()
        conn.close()

        fetch_universities_data()

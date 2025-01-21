import tkinter as tk
from tkinter import ttk
from professors import fetch_professors_data, insert_professor_data, delete_professor_data
from affiliations import fetch_affiliations_data, insert_affiliation_data, delete_affiliation_data
from organizations import fetch_organizations_data, insert_organization_data, delete_organization_data
from universities import fetch_universities_data, insert_university_data, delete_university_data

# Main window
root = tk.Tk()
root.title("University Database Management")

# Tabs for each table
tab_control = ttk.Notebook(root)

### Professors Tab ###
professors_tab = ttk.Frame(tab_control)
tab_control.add(professors_tab, text="Professors")

professors_tree = ttk.Treeview(professors_tab, columns=("ID", "First Name", "Last Name", "University ID"), show="headings")
professors_tree.heading("ID", text="ID")
professors_tree.heading("First Name", text="First Name")
professors_tree.heading("Last Name", text="Last Name")
professors_tree.heading("University ID", text="University ID")
professors_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Button(professors_tab, text="Fetch Data", command=lambda: fetch_professors_data(professors_tree)).grid(row=1, column=0, pady=5)

tk.Label(professors_tab, text="First Name").grid(row=2, column=0, sticky="e")
professors_first_name_entry = tk.Entry(professors_tab)
professors_first_name_entry.grid(row=2, column=1)

tk.Label(professors_tab, text="Last Name").grid(row=3, column=0, sticky="e")
professors_last_name_entry = tk.Entry(professors_tab)
professors_last_name_entry.grid(row=3, column=1)

tk.Label(professors_tab, text="University ID").grid(row=4, column=0, sticky="e")
professors_university_id_entry = tk.Entry(professors_tab)
professors_university_id_entry.grid(row=4, column=1)

tk.Button(professors_tab, text="Insert Data", command=lambda: insert_professor_data(
    professors_first_name_entry, professors_last_name_entry, professors_university_id_entry)).grid(row=5, column=0)

tk.Button(professors_tab, text="Delete Data", command=lambda: delete_professor_data(
    professors_first_name_entry, professors_last_name_entry, professors_university_id_entry)).grid(row=5, column=1)

# ### Affiliations Tab ###
# affiliations_tab = ttk.Frame(tab_control)
# tab_control.add(affiliations_tab, text="Affiliations")

# affiliations_tree = ttk.Treeview(affiliations_tab, columns=("function", "organization_id", "professors_id"), show="headings")

# affiliations_tree.heading("Function", text="Function")
# affiliations_tree.heading("Organization ID", text="Organization ID")
# affiliations_tree.heading("Professors ID", text="Professors ID")
# affiliations_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# tk.Button(affiliations_tab, text="Fetch Data", command=lambda: fetch_affiliations_data(affiliations_tree)).grid(row=1, column=0, pady=5)

# tk.Label(affiliations_tab, text="Function").grid(row=2, column=0, sticky="e")
# function_entry = tk.Entry(affiliations_tab)
# function_entry.grid(row=2, column=1)

# tk.Label(affiliations_tab, text="Organization ID").grid(row=3, column=0, sticky="e")
# Organization_ID_entry = tk.Entry(affiliations_tab)
# Organization_ID_entry.grid(row=3, column=1)

# tk.Label(affiliations_tab, text="Professors ID").grid(row=4, column=0, sticky="e")
# Professors_ID_entry = tk.Entry(affiliations_tab)
# Professors_ID_entry.grid(row=4, column=1)

# tk.Button(affiliations_tab, text="Insert Data", command=lambda: insert_affiliation_data(
#     function_entry, Organization_ID_entry, Professors_ID_entry)).grid(row=5, column=0)

# tk.Button(affiliations_tab, text="Delete Data", command=lambda: delete_affiliation_data(
#     function_entry,  Organization_ID_entry, Professors_ID_entry)).grid(row=5, column=1)

### Organizations Tab ###
organizations_tab = ttk.Frame(tab_control)
tab_control.add(organizations_tab, text="Organizations")

organizations_tree = ttk.Treeview(organizations_tab, columns=("ID", "Organization_sector"), show="headings")
organizations_tree.heading("ID", text="ID")
organizations_tree.heading("Organization_sector", text="Organization_sector")

organizations_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Button(organizations_tab, text="Fetch Data", command=lambda: fetch_organizations_data(organizations_tree)).grid(row=1, column=0, pady=5)

tk.Label(organizations_tab, text="Organization_sector").grid(row=2, column=0, sticky="e")
Organization_sector_entry = tk.Entry(organizations_tab)
Organization_sector_entry.grid(row=2, column=1)



tk.Button(organizations_tab, text="Insert Data", command=lambda: insert_organization_data(
    Organization_sector_entry)).grid(row=5, column=0)

tk.Button(organizations_tab, text="Delete Data", command=lambda: delete_organization_data(
    Organization_sector_entry)).grid(row=5, column=1)

### Universities Tab ###
universities_tab = ttk.Frame(tab_control)
tab_control.add(universities_tab, text="Universities")

universities_tree = ttk.Treeview(universities_tab, columns=("ID", "University Name", "Location"), show="headings")
universities_tree.heading("ID", text="ID")
universities_tree.heading("University Name", text="University Name")
universities_tree.heading("Location", text="Location")

universities_tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Button(universities_tab, text="Fetch Data", command=lambda: fetch_universities_data(universities_tree)).grid(row=1, column=0, pady=5)

tk.Label(universities_tab, text="University Name").grid(row=2, column=0, sticky="e")
universities_name_entry = tk.Entry(universities_tab)
universities_name_entry.grid(row=2, column=1)

tk.Label(universities_tab, text="Location").grid(row=3, column=0, sticky="e")
universities_location_entry = tk.Entry(universities_tab)
universities_location_entry.grid(row=3, column=1)


tk.Button(universities_tab, text="Insert Data", command=lambda: insert_university_data(
    universities_name_entry, universities_location_entry)).grid(row=5, column=0)

tk.Button(universities_tab, text="Delete Data", command=lambda: delete_university_data(
    universities_name_entry, universities_location_entry)).grid(row=5, column=1)

# Add tabs to the main window
tab_control.pack(expand=1, fill="both")

# Run the application
root.mainloop()

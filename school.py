import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()
    gender = gender_var.get()
    address = entry_address.get()

    if name and age and grade and gender and address:
        # You can add database code here to save this data
        messagebox.showinfo("Form Submission", "Form submitted successfully!")
    else:
        messagebox.showwarning("Form Submission", "Please fill in all fields")

# Create the main window
root = tk.Tk()
root.title("School Admission Form")

# Form fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2, sticky="w")

tk.Label(root, text="Address:").grid(row=4, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=5, columnspan=2, pady=10)

# Start the GUI main loop
root.mainloop()

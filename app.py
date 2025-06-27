import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import os

# --- Configuration ---
# You can customize the form questions by editing this list
QUESTIONS = ["Name", "Email", "Favorite Color"]
EXCEL_FILE = "responses.xlsx"
# ---------------------

class FormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form to Excel")
        self.root.geometry("450x250")

        self.entries = {}
        self.create_form()

    def create_form(self):
        """Creates the GUI form with labels, entries, and a submit button."""
        form_frame = tk.Frame(self.root, padx=20, pady=20)
        form_frame.pack(expand=True, fill="both")

        for i, question in enumerate(QUESTIONS):
            label = tk.Label(form_frame, text=f"{question}:", font=("Arial", 12))
            label.grid(row=i, column=0, padx=5, pady=8, sticky="w")
            entry = tk.Entry(form_frame, width=40, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=5, pady=8)
            self.entries[question] = entry

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat")
        submit_button.pack(pady=10, padx=20, fill="x")

    def submit_form(self):
        """Handles the form submission event."""
        responses = {question: entry.get() for question, entry in self.entries.items()}

        if any(not value for value in responses.values()):
            messagebox.showwarning("Warning", "Please fill out all fields.")
            return

        responses["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.save_to_excel(responses):
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Your response has been saved successfully.")

    def save_to_excel(self, data):
        """Saves the submitted data to the Excel file."""
        columns = ["Timestamp"] + QUESTIONS
        new_entry_df = pd.DataFrame([data])

        try:
            if not os.path.exists(EXCEL_FILE):
                df = new_entry_df
            else:
                existing_df = pd.read_excel(EXCEL_FILE)
                df = pd.concat([existing_df, new_entry_df], ignore_index=True)

            # Reorder columns to keep a consistent structure
            other_cols = [col for col in df.columns if col not in columns]
            final_columns = columns + other_cols
            df = df[final_columns]
            
            df.to_excel(EXCEL_FILE, index=False)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop() 
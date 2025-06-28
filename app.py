import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import pandas as pd
from datetime import datetime
import os

# --- Configuration ---
# You can customize the default form questions by editing this list
QUESTIONS = ["Name", "Email", "Favorite Color"]
# EXCEL_FILE = "responses.xlsx"
# ---------------------

class RemoveQuestionDialog(simpledialog.Dialog):
    def __init__(self, parent, title, questions):
        self.questions = questions
        self.selection = None
        super().__init__(parent, title)

    def body(self, master):
        self.listbox = tk.Listbox(master, selectmode="multiple", exportselection=False)
        for q in self.questions:
            self.listbox.insert(tk.END, q)
        self.listbox.pack(padx=15, pady=15)
        return self.listbox  # Set initial focus

    def apply(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            self.selection = [self.listbox.get(i) for i in selected_indices]

class FormApp:
    def __init__(self, root, excel_file, initial_questions=None):
        self.root = root
        self.excel_file = excel_file
        # Extract just the filename for the title
        file_title = os.path.basename(self.excel_file)
        self.root.title(f"Form to Excel - {file_title}")
        self.root.geometry("450x250")

        if initial_questions is not None:
            self.questions = initial_questions
        else:
            self.questions = list(QUESTIONS)  # Start with default questions
        
        self.entries = {}
        
        self.form_frame = tk.Frame(self.root, padx=20, pady=20)
        self.form_frame.pack(expand=True, fill="both")

        self._redraw_form()
        self.create_action_buttons()

    def _redraw_form(self):
        """Clears and recreates the GUI form based on the current questions."""
        # Clear existing widgets
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        
        # Re-populate with current questions
        self.entries = {}
        for i, question in enumerate(self.questions):
            label = tk.Label(self.form_frame, text=f"{question}:", font=("Arial", 12))
            label.grid(row=i, column=0, padx=5, pady=8, sticky="w")
            entry = tk.Entry(self.form_frame, width=40, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=5, pady=8)
            self.entries[question] = entry

    def create_action_buttons(self):
        """Creates the Submit, Add, and Remove Question buttons."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10, padx=20, fill="x", side="bottom")

        submit_button = tk.Button(button_frame, text="Submit", command=self.submit_form, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat")
        submit_button.pack(side="left", expand=True, fill="x", padx=(0, 5))

        add_question_button = tk.Button(button_frame, text="Add Question", command=self.add_question, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat")
        add_question_button.pack(side="left", expand=True, fill="x", padx=(5, 5))

        remove_question_button = tk.Button(button_frame, text="Remove Question", command=self.remove_question, font=("Arial", 14), bg="#f44336", fg="white", relief="flat")
        remove_question_button.pack(side="left", expand=True, fill="x", padx=(5, 0))

    def remove_question(self):
        """Opens a dialog to remove one or more questions from the form."""
        if not self.questions:
            messagebox.showinfo("Info", "There are no questions to remove.", parent=self.root)
            return

        dialog = RemoveQuestionDialog(self.root, "Remove Question", self.questions)
        questions_to_remove = dialog.selection

        if questions_to_remove:
            num_removed = len(questions_to_remove)
            for q in questions_to_remove:
                self.questions.remove(q)
            self._redraw_form()
            # Adjust window size
            self.root.geometry(f"450x{self.root.winfo_height() - (40 * num_removed)}")

    def add_question(self):
        """Prompts user and adds a new question to the form."""
        new_question = simpledialog.askstring("Add Question", "Enter the new question:", parent=self.root)

        if new_question and new_question.strip():
            new_question = new_question.strip()
            if new_question in self.questions:
                messagebox.showwarning("Warning", "This question already exists.")
                return

            self.questions.append(new_question)
            self._redraw_form()
            
            # Adjust window size
            self.root.geometry(f"450x{self.root.winfo_height() + 40}")

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
        columns = ["Timestamp"] + self.questions
        new_entry_df = pd.DataFrame([data])

        try:
            if not os.path.exists(self.excel_file):
                df = new_entry_df
            else:
                existing_df = pd.read_excel(self.excel_file)
                df = pd.concat([existing_df, new_entry_df], ignore_index=True)

            # Reorder columns to keep a consistent structure
            other_cols = [col for col in df.columns if col not in columns]
            final_columns = columns + other_cols
            df = df[final_columns]
            
            df.to_excel(self.excel_file, index=False)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")
            return False

if __name__ == "__main__":
    # Create a hidden root window to act as parent for the dialog
    root = tk.Tk()
    root.withdraw()

    # Ask if user wants to open an existing file.
    open_existing = messagebox.askyesno(
        "Open Existing File?",
        "Do you want to open and modify an existing response file?",
        parent=root
    )

    filepath = None
    questions_from_file = None

    if open_existing:
        # User wants to open a file
        filepath = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Select a response file to open",
            parent=root
        )
        if filepath:
            try:
                df = pd.read_excel(filepath)
                # Load questions from columns, excluding the timestamp
                questions_from_file = [col for col in df.columns if col != 'Timestamp']
            except Exception as e:
                messagebox.showerror("Error", f"Could not read the file: {e}", parent=root)
                filepath = None  # Reset filepath so app doesn't open
    else:
        # User wants to create a new file
        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Create a new response file",
            initialfile="responses.xlsx",
            parent=root
        )

    if filepath:
        # If we have a filepath, show the main window and start the app
        root.deiconify()
        app = FormApp(root, filepath, initial_questions=questions_from_file)
        root.mainloop()
    else:
        # If user cancels, destroy the hidden root window and exit
        root.destroy() 
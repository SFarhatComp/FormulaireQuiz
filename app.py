import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import pandas as pd
from datetime import datetime
import os
from questions_data import FORMS_DATA

class FormWizardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical History Form")
        self.root.geometry("800x700")

        self.form_keys = list(FORMS_DATA.keys())
        self.current_page = 0
        self.patient_data = {}
        self.pages = {}
        self.widget_map = {}

        # Main container for the pages
        self.page_container = tk.Frame(root)
        self.page_container.pack(side="top", fill="both", expand=True)
        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        self._create_pages()
        self._create_navigation()
        self.show_page(0)

    def _create_pages(self):
        for i, form_key in enumerate(self.form_keys):
            form_data = FORMS_DATA[form_key]
            frame = tk.Frame(self.page_container, padx=10, pady=10)
            self.pages[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            title = ttk.Label(frame, text=form_data["title"], font=("Arial", 16, "bold"))
            title.pack(pady=(0, 20))

            # Canvas and Scrollbar for scrollable content
            canvas = tk.Canvas(frame)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            self._populate_page(scrollable_frame, form_data["questions"])

            # Add some bottom padding to prevent the last widget from being cut off
            ttk.Frame(scrollable_frame, height=20).pack()

    def _populate_page(self, parent, questions):
        self.widget_map[parent] = {}
        for question in questions:
            row_frame = tk.Frame(parent)
            row_frame.pack(fill="x", pady=2)
            
            if isinstance(question, dict): # Conditional question
                q_label = question["label"]
                var = tk.StringVar(value="No") # Default to 'No'
                self.patient_data[q_label] = var
                
                label = ttk.Label(row_frame, text=q_label, width=40)
                label.pack(side="left", padx=5)

                yes_rb = ttk.Radiobutton(row_frame, text="Yes", variable=var, value="Yes")
                no_rb = ttk.Radiobutton(row_frame, text="No", variable=var, value="No")
                yes_rb.pack(side="left")
                no_rb.pack(side="left")
                
                # Store widgets to be hidden
                self.widget_map[parent][q_label] = {
                    "hides": question["hides"], 
                    "widgets_to_hide": []
                }
                var.trace_add("write", lambda *args, q=question, p=parent: self._toggle_visibility(q, p))

            else: # Standard question
                q_label = question
                var = tk.StringVar()
                self.patient_data[q_label] = var

                label = ttk.Label(row_frame, text=q_label, width=40)
                entry = ttk.Entry(row_frame, textvariable=var, width=50)
                label.pack(side="left", padx=5)
                entry.pack(side="left", padx=5, fill="x", expand=True)
                
                # If this widget can be hidden, add it to the map
                for conditional_q, data in self.widget_map.get(parent, {}).items():
                    if q_label in data["hides"]:
                        data["widgets_to_hide"].append(row_frame)

    def _toggle_visibility(self, question_data, parent):
        var = self.patient_data[question_data["label"]]
        is_visible = var.get() == "Yes"
        
        widgets_to_hide = self.widget_map[parent][question_data["label"]]["widgets_to_hide"]
        for widget_row in widgets_to_hide:
            if is_visible:
                widget_row.pack(fill="x", pady=2)
            else:
                widget_row.pack_forget()

    def _create_navigation(self):
        nav_frame = tk.Frame(self.root, pady=10)
        nav_frame.pack(side="bottom", fill="x")

        self.back_button = ttk.Button(nav_frame, text="Back", command=self.prev_page, state="disabled")
        self.next_button = ttk.Button(nav_frame, text="Next", command=self.next_page)
        self.submit_button = ttk.Button(nav_frame, text="Submit", command=self.submit, state="disabled")

        self.back_button.pack(side="left", padx=20)
        self.submit_button.pack(side="right", padx=20)
        self.next_button.pack(side="right")

    def show_page(self, page_number):
        if page_number in self.pages:
            self.current_page = page_number
            frame = self.pages[page_number]
            frame.tkraise()

            self.back_button["state"] = "normal" if self.current_page > 0 else "disabled"
            self.next_button["state"] = "normal" if self.current_page < len(self.pages) - 1 else "disabled"
            self.submit_button["state"] = "normal" if self.current_page == len(self.pages) - 1 else "disabled"

    def next_page(self):
        next_page_index = self.current_page + 1
        
        # Handle preliminary questions for skipping forms
        if next_page_index < len(self.form_keys):
            form_key = self.form_keys[next_page_index]
            form_data = FORMS_DATA[form_key]
            
            if "preliminary_question" in form_data:
                proceed = messagebox.askyesno(
                    form_data["title"],
                    form_data["preliminary_question"],
                    parent=self.root
                )
                if not proceed:
                    # Mark all questions in this form to be skipped
                    fill_value = form_data.get("fill_value", "N/A")
                    for q in form_data["questions"]:
                        self.patient_data[q] = tk.StringVar(value=fill_value)
                    
                    # Try to skip to the page after this one
                    self.current_page += 1
                    self.next_page()
                    return

        self.show_page(next_page_index)

    def prev_page(self):
        self.show_page(self.current_page - 1)

    def submit(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Save Response",
            initialfile="patient_response.xlsx",
        )
        if not filepath:
            return

        # Prepare data for saving
        final_data = {}
        # Add a timestamp first
        final_data["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for form_key in self.form_keys:
            form_info = FORMS_DATA[form_key]
            
            # Add a separator for clarity in Excel
            final_data[f"--- {form_info['title']} ---"] = ""

            for question in form_info["questions"]:
                q_label = question["label"] if isinstance(question, dict) else question
                
                # Handle conditional questions where the answer is "No"
                if isinstance(question, dict) and self.patient_data[q_label].get() == "No":
                    final_data[q_label] = "No"
                    fill_value = question.get("fill_value", "N/A")
                    for hidden_q in question["hides"]:
                        final_data[hidden_q] = fill_value
                else:
                    var = self.patient_data.get(q_label)
                    final_data[q_label] = var.get() if var else ""

        try:
            new_entry_df = pd.DataFrame([final_data])

            # Use ExcelWriter to gain access to the worksheet and adjust column widths
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                if os.path.exists(filepath):
                    existing_df = pd.read_excel(filepath)
                    # Align columns before concatenating
                    all_cols = existing_df.columns.union(new_entry_df.columns)
                    existing_df = existing_df.reindex(columns=all_cols)
                    new_entry_df = new_entry_df.reindex(columns=all_cols)
                    df = pd.concat([existing_df, new_entry_df], ignore_index=True)
                else:
                    df = new_entry_df
                
                df.to_excel(writer, index=False, sheet_name='Responses')
                
                # Auto-fit columns
                worksheet = writer.sheets['Responses']
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = (max_length + 2)
                    worksheet.column_dimensions[column_letter].width = adjusted_width

            messagebox.showinfo("Success", f"Data saved successfully to\n{filepath}")
            self.root.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormWizardApp(root)
    root.mainloop() 
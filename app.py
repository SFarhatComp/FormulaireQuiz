import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import pandas as pd
from datetime import datetime
import os
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill
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

    def _bind_scroll(self, widget, canvas):
        """Binds mouse scroll events to a widget to scroll a canvas."""
        # For Windows/macOS
        widget.bind("<MouseWheel>", lambda e, c=canvas: c.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        # For Linux
        widget.bind("<Button-4>", lambda e, c=canvas: c.yview_scroll(-1, "units"))
        widget.bind("<Button-5>", lambda e, c=canvas: c.yview_scroll(1, "units"))

    def _bind_recursive(self, widget, canvas):
        """Binds mouse scroll events recursively to a widget and all its children."""
        self._bind_scroll(widget, canvas)
        for child in widget.winfo_children():
            self._bind_recursive(child, canvas)

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
            self._bind_recursive(scrollable_frame, canvas)

            # Add some bottom padding to prevent the last widget from being cut off
            padding_frame = ttk.Frame(scrollable_frame, height=20)
            padding_frame.pack()
            self._bind_scroll(padding_frame, canvas)

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
                    # Mark all questions in this form to be skipped by storing the value directly
                    fill_value = form_data.get("fill_value", "N/A")
                    for q in form_data["questions"]:
                        self.patient_data[q] = fill_value
                    
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
            
            for question in form_info["questions"]:
                q_label = question["label"] if isinstance(question, dict) else question
                
                # Handle conditional questions where the answer is "No"
                if isinstance(question, dict) and self.patient_data[q_label].get() == "No":
                    final_data[q_label] = "No"
                    fill_value = question.get("fill_value", "N/A")
                    for hidden_q in question["hides"]:
                        final_data[hidden_q] = fill_value
                else:
                    value = self.patient_data.get(q_label)
                    if isinstance(value, tk.StringVar):
                        final_data[q_label] = value.get()
                    else: # This is a raw value from a skipped form
                        final_data[q_label] = value if value is not None else ""

        try:
            new_entry_df = pd.DataFrame([final_data])
            
            # Prepare the final dataframe BEFORE opening the file for writing
            if os.path.exists(filepath):
                existing_df = pd.read_excel(filepath)
                
                # Get the order of columns from the existing file and add new ones to the end
                final_ordered_columns = existing_df.columns.tolist()
                for col in new_entry_df.columns:
                    if col not in final_ordered_columns:
                        final_ordered_columns.append(col)

                # Reindex both dataframes to this final, preserved order
                existing_df = existing_df.reindex(columns=final_ordered_columns)
                new_entry_df = new_entry_df.reindex(columns=final_ordered_columns)
                df_to_save = pd.concat([existing_df, new_entry_df], ignore_index=True)
            else:
                df_to_save = new_entry_df

            # Now, write the final dataframe to the file using ExcelWriter
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                df_to_save.to_excel(writer, index=False, sheet_name='Responses')
                
                worksheet = writer.sheets['Responses']
                
                # Define colors for each form section
                section_fills = [
                    PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"), # Light Red
                    PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"), # Light Green
                    PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"), # Light Yellow
                    PatternFill(start_color="B4C6E7", end_color="B4C6E7", fill_type="solid"), # Light Blue
                    PatternFill(start_color="F2B4D0", end_color="F2B4D0", fill_type="solid"), # Pink
                    PatternFill(start_color="D9D9F3", end_color="D9D9F3", fill_type="solid"), # Lavender
                    PatternFill(start_color="FFDAB9", end_color="FFDAB9", fill_type="solid"), # Peach
                    PatternFill(start_color="E0FFFF", end_color="E0FFFF", fill_type="solid"), # Light Cyan
                    PatternFill(start_color="F0FFF0", end_color="F0FFF0", fill_type="solid"), # Honeydew
                    PatternFill(start_color="FFFACD", end_color="FFFACD", fill_type="solid"), # Lemon Chiffon
                    PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid"), # Light Grey
                    PatternFill(start_color="BDB76B", end_color="BDB76B", fill_type="solid"), # Dark Khaki
                    PatternFill(start_color="ADD8E6", end_color="ADD8E6", fill_type="solid")  # Light Blue 2
                ]

                # Create a map of question -> color
                column_to_color_map = {}
                color_index = 0
                for form_key in self.form_keys:
                    fill = section_fills[color_index % len(section_fills)]
                    for q in FORMS_DATA[form_key]["questions"]:
                        q_label = q["label"] if isinstance(q, dict) else q
                        column_to_color_map[q_label] = fill
                    color_index += 1

                # Auto-fit columns and color headers
                for i, column_name in enumerate(df_to_save.columns):
                    column_letter = get_column_letter(i + 1)
                    
                    # Color the header cell
                    if column_name in column_to_color_map:
                        worksheet.cell(row=1, column=i + 1).fill = column_to_color_map[column_name]

                    # Auto-sizing logic
                    max_length = len(str(column_name))
                    for cell in worksheet[column_letter]:
                        if cell.row == 1:
                            continue
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
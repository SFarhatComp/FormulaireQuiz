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
        self.patient_data = {} # Will use a unique key: (page_index, question_label)
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
            
            self._populate_page(scrollable_frame, form_data["questions"], i)
            self._bind_recursive(scrollable_frame, canvas)

            # Add some bottom padding to prevent the last widget from being cut off
            padding_frame = ttk.Frame(scrollable_frame, height=20)
            padding_frame.pack()
            self._bind_scroll(padding_frame, canvas)

    def _populate_page(self, parent, questions, page_index):
        self.widget_map[parent] = {}
        for question in questions:
            row_frame = tk.Frame(parent)
            row_frame.pack(fill="x", pady=2)
            
            if isinstance(question, dict) and question.get("type") == "dropdown":
                q_label = question["label"]
                unique_key = (page_index, q_label)

                display_options, value_map = [], {}
                for option in question["options"]:
                    parts = option.split('=', 1)
                    value = parts[0].strip()
                    display_text = f"{value}: {parts[1].strip()}" if len(parts) > 1 else value
                    display_options.append(display_text)
                    value_map[display_text] = value

                actual_value_var = self.patient_data.get(unique_key)
                if not isinstance(actual_value_var, tk.StringVar):
                    actual_value_var = tk.StringVar()
                    self.patient_data[unique_key] = actual_value_var

                display_var = tk.StringVar()

                label = ttk.Label(row_frame, text=q_label, width=40)
                label.pack(side="left", padx=5)

                combobox = ttk.Combobox(row_frame, textvariable=display_var, values=display_options, state="readonly", width=37)
                combobox.pack(side="left", fill="x", expand=True, padx=5)

                def on_select(event, var=actual_value_var, vmap=value_map, d_var=display_var):
                    actual_value = vmap.get(d_var.get(), "")
                    var.set(actual_value)
                
                combobox.bind("<<ComboboxSelected>>", on_select)

                saved_value = actual_value_var.get()
                if saved_value:
                    for text, val in value_map.items():
                        if val == saved_value:
                            display_var.set(text)
                            break
            
            elif isinstance(question, dict): # Catches 'yesno' and 'yesno_conditional'
                q_label = question["label"]
                unique_key = (page_index, q_label)
                var = tk.StringVar(value="No")
                
                # Use existing var if it's there (from loading data)
                if unique_key in self.patient_data and isinstance(self.patient_data.get(unique_key), tk.StringVar):
                    var = self.patient_data[unique_key]
                else:
                    self.patient_data[unique_key] = var

                label = ttk.Label(row_frame, text=q_label, width=40)
                label.pack(side="left", padx=5)

                yes_rb = ttk.Radiobutton(row_frame, text="Yes", variable=var, value="Yes")
                no_rb = ttk.Radiobutton(row_frame, text="No", variable=var, value="No")
                yes_rb.pack(side="left")
                no_rb.pack(side="left")
                
                if question.get("type") == "yesno_conditional":
                    self.widget_map[parent][q_label] = {
                        "hides": question["hides"], 
                        "widgets_to_hide": []
                    }
                    var.trace_add("write", lambda *args, q=question, p=parent, key=unique_key: self._toggle_visibility(q, p, key))

            else: # Standard question (text entry)
                q_label = question
                unique_key = (page_index, q_label)
                var = tk.StringVar()
                self.patient_data[unique_key] = var

                label = ttk.Label(row_frame, text=q_label, width=40)
                entry = ttk.Entry(row_frame, textvariable=var, width=50)
                label.pack(side="left", padx=5)
                entry.pack(side="left", padx=5, fill="x", expand=True)
                
                # If this widget can be hidden, add it to the map
                for conditional_q, data in self.widget_map.get(parent, {}).items():
                    if q_label in data["hides"]:
                        data["widgets_to_hide"].append(row_frame)

                # When an item is selected, update the actual_value_var
                def on_select(event):
                    display_text = var.get()
                    actual_value = value_map.get(display_text, "")
                    var.set(actual_value)
                
                entry.bind("<<ComboboxSelected>>", on_select)

                # Pre-fill if data exists
                if unique_key in self.patient_data and isinstance(self.patient_data[unique_key], tk.StringVar):
                    saved_value = self.patient_data[unique_key].get()
                    if saved_value:
                        var.set(saved_value)
                        # Find the corresponding display text for the saved value
                        for text, val in value_map.items():
                            if val == saved_value:
                                var.set(text)
                                break

    def _toggle_visibility(self, question_data, parent, key):
        var = self.patient_data[key]
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
                        unique_key = (next_page_index, q)
                        self.patient_data[unique_key] = fill_value
                    
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

        final_data = {"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        column_counts = {}

        # First pass: collect all data with unique keys
        for i, form_key in enumerate(self.form_keys):
            form_info = FORMS_DATA[form_key]
            
            for question in form_info["questions"]:
                base_label = question['label'] if isinstance(question, dict) else question
                
                # Generate unique column name
                count = column_counts.get(base_label, 0) + 1
                column_counts[base_label] = count
                unique_col_name = f"{base_label}_{count}" if count > 1 else base_label

                # Get value using unique (page, label) key
                unique_data_key = (i, base_label)
                value = self.patient_data.get(unique_data_key)

                if isinstance(question, dict): # Conditional
                    is_yes = value.get() == "Yes"
                    final_data[unique_col_name] = "Yes" if is_yes else "No"

                    if not is_yes and question.get("type") == "yesno_conditional":
                        fill_value = question.get("fill_value", "N/A")
                        for hidden_q_label in question['hides']:
                            hidden_page_index = self._find_question_page(hidden_q_label)
                            hidden_key = (hidden_page_index, hidden_q_label)
                            hidden_unique_name = self._generate_unique_column_name(final_data, hidden_q_label)
                            final_data[hidden_unique_name] = fill_value
                            # Ensure the var is also updated for consistency
                            if hidden_key in self.patient_data:
                                self.patient_data[hidden_key].set(fill_value)
                
                else: # Standard or skipped question
                    if isinstance(value, tk.StringVar):
                        final_data[unique_col_name] = value.get()
                    elif value is not None: # Skipped page
                        final_data[unique_col_name] = value
                    else: # Failsafe
                        final_data[unique_col_name] = ""
        
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

                # Create a map of question base label -> color
                section_color_map = {}
                color_index = 0
                for form_key in self.form_keys:
                    fill = section_fills[color_index % len(section_fills)]
                    for q in FORMS_DATA[form_key]["questions"]:
                        q_label = q["label"] if isinstance(q, dict) else q
                        section_color_map[q_label] = fill
                    color_index += 1

                # Auto-fit columns and color headers
                for i, column_name in enumerate(df_to_save.columns):
                    column_letter = get_column_letter(i + 1)
                    
                    # Find base label to look up color
                    base_label = column_name.rsplit('_', 1)[0] if '_' in column_name and column_name.rsplit('_', 1)[1].isdigit() else column_name
                    if base_label in section_color_map:
                        worksheet.cell(row=1, column=i + 1).fill = section_color_map[base_label]

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
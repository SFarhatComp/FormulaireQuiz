# Project Design: Multi-Page Medical Questionnaire

This document outlines the design and evolution of a multi-page, offline-first medical questionnaire application built with Python and `tkinter`. The application guides the user through a series of forms, implements conditional logic based on user input, and saves the complete patient record into a single row in a user-specified Excel file.

---

## 1. Core Architecture: The Form Wizard

The application is architected as a "wizard," presenting the user with a sequence of 13 forms. This structure ensures that data is collected in a logical and orderly manner.

-   **Multi-Page Interface:** The UI is managed in a single window with a content area that displays one form at a time.
-   **Sequential Navigation:** "Next" and "Back" buttons allow the user to move between the different sections of the questionnaire.
-   **Centralized Data Store:** A single Python dictionary holds the user's responses in memory as they navigate through the forms. Data is keyed by a `(page_index, question_label)` tuple to ensure uniqueness, even for questions with identical labels on different forms.

---

## 2. Key Features & Design Evolution

### 2.1. Dynamic & Interactive Form Rendering

The initial design used simple text entry fields for all questions. This was updated to a more interactive and user-friendly approach to improve data entry speed and reduce errors.

-   **Separation of Concerns:** The entire 13-form structure, including all questions, types, and conditional rules, is defined in a dedicated `questions_data.py` file. This cleanly separates the form's data model from the application's UI logic in `app.py`.

-   **Dynamic Widget Generation:** The UI is not hard-coded. Instead, `app.py` reads the structure from `questions_data.py` and dynamically renders the appropriate widget for each question.
    -   **Yes/No Questions:** Questions phrased with a `?` are rendered as clickable **Yes/No radio buttons**. This was a significant usability improvement over manual text entry.
    -   **Multiple Choice Questions:** Questions offering a selection from a numbered list (e.g., `(1=x, 2=y)`) are rendered as **dropdown menus (`Combobox`)**. This prevents invalid entries and clearly presents all options to the user.
    -   **Standard Text Entry:** All other questions default to a standard text input field.

-   **Enhanced User Experience:**
    -   **Reliable Scrolling:** All form pages, especially long ones, feature robust mouse-wheel scrolling that is bound to all UI elements, ensuring a smooth and predictable user experience.
    -   **UI Padding:** Sufficient padding is added to the end of each form to prevent the last question from being obscured by the navigation buttons.

### 2.2. Advanced Conditional Logic

To handle the complexity of a medical questionnaire, the application implements two layers of conditional logic:

-   **Field-level conditions:** Answering "No" to specific questions (e.g., "Congenital Malformation?", "Postop MRI?") automatically hides irrelevant sub-questions from the UI. When hidden, their corresponding data fields are assigned a specific placeholder value (`"0"` or `"N/A"`) upon submission.
-   **Form-level conditions:** For certain sections (e.g., "Follow Up Echo 1, 2, 3"), the application first asks if the event occurred. If the user answers "No," the entire form is skipped, and all of its associated data fields are automatically filled with "N/A" for the final export.

### 2.3. Intelligent & Robust Data Export

The data export process was designed to be both robust and user-friendly, creating a clean and readable Excel file.

-   **User-Directed File Handling:** Upon startup, the application prompts the user to either create a new response file (choosing the name and location) or open an existing one to append new records.
-   **Unique Column Naming:** A critical bug was discovered where questions with identical labels on different forms (e.g., "ST junction (mm)") would overwrite each other's data. This was resolved by implementing a system that generates unique column names (e.g., `ST junction (mm)_1`, `ST junction (mm)_2`) in the Excel output, ensuring all data is preserved.
-   **Visual Grouping in Excel:** To enhance readability, the header cell for each question is given a background color corresponding to its form section. This provides clear visual grouping without the need for extra separator columns.
-   **Auto-Sized Columns:** Excel columns are automatically resized to fit the length of the longest content, including the question headers, eliminating the need for manual adjustments by the user.

---

## 3. Technical Implementation

-   **Language:** Python 3
-   **GUI Library:** `tkinter` (using the modern `ttk` themed widgets).
-   **Data Handling:** `pandas` and `openpyxl` for creating and appending data to the `.xlsx` file.
-   **Distribution:** `PyInstaller` is included in the project to facilitate the creation of standalone executables for users without a Python environment.
-   **Containerization:** A `Dockerfile` is provided for building and running the application in a containerized environment.

---

## 4. Final File Structure

```
.
├── app.py                  # Main Python application script (wizard logic, UI rendering)
├── questions_data.py       # Defines the structure and rules of all 13 forms
├── requirements.txt        # Python dependencies (pandas, openpyxl, pyinstaller)
├── Dockerfile              # Containerization instructions
├── README.md               # User-facing documentation and build instructions
└── Design.md               # This design document
```


If you need to download any dependencies make sure youre in the vmsource ~/venv/FormulaireVenv/bin/activate.fish



orm to Excel (Offline & Container-Ready)

This project is a **local, offline form** built using Python that allows users to input responses into a simple GUI. Upon submission, responses are **saved to an Excel file** (`responses.xlsx`). This solution is:

- ✅ Completely offline
- ✅ Easy to use and extend
- ✅ Compatible with or without Docker
- ✅ Suitable for local record-keeping and small deployments

---

## ✨ Features

- GUI form using `tkinter`
- Input fields for user data (e.g., Name, Email)
- Data saved in `.xlsx` file using `pandas`
- No need for a web server or internet connection
- Optional Docker containerization
- Start with default question , they should be customizable after. The workflow is to have every submission equal one line in excell
with each question being one column

---

## 📦 Requirements

### Python Dependencies

Install requirements with:

```bash
pip install pandas openpyxl

📁 File Structure
.
├── app.py          # Python form application
├── responses.xlsx  # Excel file with responses (auto-created)
├── Dockerfile      # Optional containerization
└── README.md       # Documentation

Add timestamp to each entry


Im thinking Running the code, it opens a gui, the line is saved on each submission ( possibly through a submit button ) and it append to the xlsx in real time 
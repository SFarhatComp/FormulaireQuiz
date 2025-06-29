# Project Design: Multi-Page Medical Questionnaire

This document outlines the design for a multi-page, offline-first medical questionnaire application built with Python and `tkinter`. The application guides the user through a series of forms, implements conditional logic, and saves the complete patient record into a single row in an Excel file.

---

## 1. Core Architecture: The Form Wizard

The application is architected as a "wizard," presenting the user with a sequence of 13 forms. This structure ensures that data is collected in a logical and orderly manner.

-   **Multi-Page Interface:** The UI is managed in a single window with a content area that displays one form at a time.
-   **Sequential Navigation:** "Next" and "Back" buttons allow the user to move between the different sections of the questionnaire.
-   **Centralized Data Store:** A single data object holds the user's responses in memory as they navigate through the forms, ensuring data integrity until final submission.

## 2. Key Features

-   **Structured Form Definitions:**
    -   The entire 13-form structure, including all questions and conditional rules, is defined in a dedicated `questions_data.py` file. This separates the form data from the application's view logic.

-   **Dynamic Form Rendering:**
    -   Each form page is generated dynamically from the `questions_data.py` structure.
    -   Long forms are equipped with a scrollbar to ensure all fields are accessible.

-   **Advanced Conditional Logic:**
    -   **Field-level conditions:** Answering "No" to specific questions (e.g., "Congenital Malformation?", "Postop MRI?") automatically hides irrelevant sub-questions from the UI.
    -   **Form-level conditions:** For certain sections (e.g., "Follow Up Echo 1, 2, 3"), the application first asks if the event occurred. If the answer is "No," the entire form is skipped.

-   **Intelligent Data Export:**
    -   Upon pressing "Submit" on the final page, the user is prompted to choose a save location for the Excel file.
    -   All collected data from the 13 forms is consolidated into a single row.
    -   Skipped fields or forms are automatically populated with `"0"` or `"N/A"` as specified in the rules, ensuring a complete and consistently structured data set.
    -   Form sections are demarcated in the Excel file with separator columns (e.g., `--- Medical History ---`) for enhanced readability.

## 3. Technical Implementation

-   **Language:** Python 3
-   **GUI Library:** `tkinter` (using the modern `ttk` themed widgets).
-   **Data Handling:** `pandas` for creating and appending data to the `.xlsx` file.
-   **Containerization & Distribution:** The existing `Dockerfile` and `PyInstaller` configurations remain valid for containerizing and creating standalone executables of this new version.

## 4. File Structure

```
.
├── app.py                  # Main Python application script (wizard logic)
├── questions_data.py       # Defines the structure of all 13 forms
├── requirements.txt        # Python dependencies
├── Dockerfile              # Containerization instructions
├── README.md               # User-facing documentation
├── .gitignore              # Specifies files for Git to ignore
└── Custom.txt              # The source text for the questionnaire
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
# FormulaireQuiz Application Design

This document outlines the design and architecture of the FormulaireQuiz application, a multi-page medical data collection tool built with Python's `tkinter` library.

## 1. Core Functionality

The application is a wizard-style questionnaire designed to capture detailed patient data across 13 distinct forms. It provides a user-friendly interface for clinicians to enter data, which is then saved into a structured Excel file for analysis.

## 2. Architecture

### 2.1. Main Application (`app.py`)

- **Technology:** `tkinter` for the GUI.
- **Structure:** A single-window application, `FormWizardApp`, that manages multiple pages.
- **Navigation:** Users can navigate forwards and backwards through the forms using "Next" and "Back" buttons. A "Submit" button is available on the final page.
- **Lazy Loading:** To ensure fast startup times, the application uses a lazy loading mechanism. The UI widgets for each page are only created the first time the user navigates to that page.

### 2.2. Data Definition (`questions_data.py`)

- **Centralized Data:** All form structures, including titles, questions, and conditional logic, are defined in a single Python dictionary called `FORMS_DATA`. This separation of data from the UI logic makes the application easier to maintain and update.
- **Form Structure:** The application consists of 13 forms, covering:
    1.  Medical History
    2.  PreOP State Evaluation
    3.  Valve Lesion
    4.  Pre op Echo
    5.  Operative Data
    6.  PostUp Early Outcomes
    7.  PostOP Echo 1
    8.  Postop MRI
    9.  Follow Up Echo 1
    10. Follow Up Echo 2
    11. Follow Up Echo 3
    12. Post OP Clinical Follow Up Data (3 months)
    13. Latest Clinical Data

## 3. UI Components and Logic

The application dynamically generates three types of input fields based on the definitions in `questions_data.py`:

1.  **Text Entry:** Standard text fields for open-ended data.
2.  **Yes/No Questions:** Implemented as a pair of radio buttons for binary choices.
3.  **Dropdown Menus:** `ttk.Combobox` widgets are used for questions with a predefined set of options (e.g., `(1=x, 2=y)`). The UI displays descriptive text, but the corresponding numerical value is saved to the output file.

### 3.1. Conditional Logic

- **Hiding Fields:** Some "Yes/No" questions can conditionally hide or show a subsequent set of related questions based on the user's selection. For example, answering "No" to "Congenital Malformation?" will hide all detailed questions about specific malformations.
- **Skipping Pages:** Certain forms (e.g., "Follow Up Echo") are preceded by a dialog box asking if the form should be filled out. If the user selects "No," the application skips the entire page and fills the corresponding data columns with "N/A".

## 4. Data Handling

### 4.1. File Management

- **Startup Prompt:** On launch, the user is prompted to either create a new Excel response file or append data to an existing one via native file dialogs.

### 4.2. Data Submission and Excel Export

- **Data Aggregation:** Upon submission, data from all 13 forms is collected into a single row.
- **Unique Column Names:** To prevent data loss from questions with identical labels on different forms, a unique, incrementing suffix (e.g., `Question_1`, `Question_2`) is appended to each column header in the Excel file.
- **Excel Formatting:**
    - **Colored Headers:** The header cell for each question is given a unique background color corresponding to its form/section, providing clear visual grouping of the data.
    - **Auto-Sized Columns:** Column widths are automatically adjusted to fit the content, including the header.
- **Form Reset:** After a successful submission, the form resets to its initial state, ready for the next patient entry.

## 5. Deployment and CI/CD

- **Cross-Platform Executable:** The repository includes a GitHub Actions workflow (`.github/workflows/build-windows-exe.yml`) that automatically builds a standalone Windows `.exe` file using `PyInstaller` whenever code is pushed to the `main` branch. This simplifies distribution to non-technical users.

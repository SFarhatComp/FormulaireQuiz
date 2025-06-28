# Project Design: Dynamic Form Application

This document outlines the design for a local, offline form application built with Python and `tkinter`. The application allows for dynamic form creation and saves responses directly to a user-specified Excel file.

---

## 1. Core Functionality

-   **GUI Form:** A simple, clean graphical user interface built with `tkinter`.
-   **Offline Data-Entry:** The application works completely offline, requiring no internet connection.
-   **Excel Integration:** Saves all submitted responses into a single `.xlsx` file using the `pandas` and `openpyxl` libraries.

## 2. Key Features

-   **Flexible File Handling:**
    -   On startup, the user is prompted to either **create a new response file** or **open an existing one**.
    -   **Open Existing File:** If an existing `.xlsx` file is opened, the application reads its column headers to dynamically reconstruct the form, allowing the user to seamlessly continue a previous session.
    -   **Create New File:** If creating a new file, a native file dialog allows the user to select a save location and filename.
    -   The chosen filename is displayed in the application's title bar.

-   **Dynamic Question Management:**
    -   The application starts with a default set of questions if creating a new file.
    -   **Add Question:** A dedicated button allows the user to add new questions to the form at runtime.
    -   **Remove Question:** A button allows the user to select and remove one or more questions from the form via a multi-select dialog.
    -   The form layout dynamically adjusts as questions are added or removed.

-   **Data Submission:**
    -   A "Submit" button collects all data from the input fields.
    -   Each submission is saved as a new row in the selected Excel file.
    -   A timestamp is automatically added to each entry to record when it was submitted.

## 3. Technical Implementation

-   **Language:** Python 3
-   **GUI Library:** `tkinter` (standard library, but may require separate installation on some OSes).
-   **Data Handling:** `pandas` for creating and appending data to the Excel file.
-   **Containerization:** A `Dockerfile` is provided to run the application in an isolated container, ensuring consistent behavior across different environments.
-   **Executable Bundling:** The project is configured to be bundled into a single standalone executable using `PyInstaller`, making it easy to distribute to non-technical users.

## 4. File Structure

```
.
├── app.py          # Main Python application script
├── requirements.txt# Python dependencies
├── Dockerfile      # Containerization instructions
├── README.md       # User-facing documentation
├── .gitignore      # Specifies files for Git to ignore
└── responses.xlsx  # Example output file (auto-created)
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
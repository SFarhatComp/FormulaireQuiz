# Form to Excel (Offline & Container-Ready)

This project is a **local, offline form** built using Python that allows users to input responses into a simple GUI. Upon submission, responses are **saved to an Excel file** (`responses.xlsx`). This solution is:

- ✅ Completely offline
- ✅ Easy to use and extend
- ✅ Compatible with or without Docker
- ✅ Suitable for local record-keeping and small deployments

---

## ✨ Features

- GUI form using `tkinter`
- Input fields for user data (e.g., Name, Email, Favorite Color)
- Data saved in `.xlsx` file using `pandas`
- A timestamp is recorded for each submission.
- No need for a web server or internet connection
- Optional Docker containerization for portability.

---

## 🚀 Getting Started

### 1. Without Docker (Local Setup)

**a. Set up a virtual environment (recommended):**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**b. Install dependencies:**

```bash
pip install -r requirements.txt
```

**c. Run the application:**

```bash
python3 app.py
```

A GUI window will open. Fill in the form and click "Submit". Your responses will be saved in `responses.xlsx`.

### 2. With Docker

**a. Build the Docker image:**

```bash
docker build -t form-app .
```

**b. Run the Docker container:**

To run a GUI application from a Docker container, you need to share your host's display with the container.

**For Linux:**
```bash
xhost +local:docker
docker run \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
  -v $(pwd):/app \
  --rm \
  form-app
```

**For macOS (with XQuartz):**
First, open XQuartz. In the XQuartz preferences, go to the "Security" tab and make sure "Allow connections from network clients" is checked. Then run in your terminal: `xhost + 127.0.0.1`.

```bash
docker run -e DISPLAY=host.docker.internal:0 -v $(pwd):/app --rm form-app
```

**For Windows (with VcXsrv or Xming):**
You'll need to install and run an X server like VcXsrv. When configuring it, make sure to disable access control.

```bash
docker run -e DISPLAY=host.docker.internal:0 -v $(pwd):/app --rm form-app
```
*Note*: The `-v $(pwd):/app` part mounts the current directory into the container. This allows the `responses.xlsx` file to be created and saved on your host machine.

---

## 📁 File Structure

```
.
├── app.py          # Python form application
├── requirements.txt# Python dependencies
├── responses.xlsx  # Excel file with responses (auto-created)
├── Dockerfile      # Optional containerization
└── README.md       # This documentation
```

## 🔧 Customization

You can easily customize the form questions by editing the `QUESTIONS` list at the top of the `app.py` file.

```python
# app.py
# --- Configuration ---
QUESTIONS = ["Name", "Email", "Your New Question"]
# ...
```
The Excel columns will be updated automatically to include new questions. Existing columns will be preserved.

---

## 📦 Creating a Standalone Executable

To make the application easy to share and run on other computers without requiring a Python installation, you can package it into a single executable file using `PyInstaller`.

### Instructions for Linux (Debian/Ubuntu/Fedora)

1.  **Install Prerequisites:**
    You need Python, Pip, and Tkinter. If you don't have them, open a terminal and run:
    ```bash
    # For Debian/Ubuntu
    sudo apt-get update
    sudo apt-get install python3 python3-pip python3-tk

    # For Fedora
    sudo dnf install python3 python3-pip python3-tkinter
    ```

2.  **Install PyInstaller:**
    ```bash
    pip3 install pyinstaller
    ```

3.  **Build the Executable:**
    Navigate to the project directory and run:
    ```bash
    pyinstaller --onefile --windowed app.py
    ```

4.  **Find the Executable:**
    The final executable will be located in the `dist/` directory. You can send this single `app` file to other Linux users.

### Instructions for Windows

1.  **Install Python:**
    - Download Python from the [official website](https://www.python.org/downloads/windows/).
    - **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**.
    - On the "Optional Features" screen, ensure **"tcl/tk and IDLE"** is checked to install Tkinter.

2.  **Open Command Prompt:**
    Press `Win + R`, type `cmd`, and press Enter.

3.  **Navigate to Project Folder:**
    Use the `cd` command to navigate to your project folder.
    ```cmd
    cd C:\path\to\your\FormulaireQuiz
    ```

4. **Set up a virtual environment (recommended):**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

5.  **Install Dependencies:**
    ```cmd
    pip install -r requirements.txt
    ```

6.  **Build the Executable:**
    ```cmd
    pyinstaller --onefile --windowed app.py
    ```

7.  **Find the Executable:**
    The final executable will be in the `dist\` folder, named `app.exe`. You can send this file to any Windows user. 
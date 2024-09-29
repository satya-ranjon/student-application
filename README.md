![Screenshot1](https://i.ibb.co.com/ZWPdr05/Screenshot-25.png)

![Screenshot2](https://i.ibb.co.com/kK94PVQ/Screenshot-24.png)

![Screenshot3](https://i.ibb.co.com/wdG0hhJ/Screenshot-26.png)

# Project Setup Guide

This guide will help you navigate through the steps to set up and run the student CRUD application project.

---

### 1. Navigate to the Project Root

In your terminal, use the following command to navigate to the project's root directory:

```bash
cd student-application
```

### 2. Prepare the Project Environment

In your terminal, use the following command to navigate to the project's root directory:

```bash
pwebcli project update
```

### 3. Activate the Virtual Environment

Activate the virtual environment by using the following command:

```bash
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```

### 4. Initialize the Database

Run this command to initialize the database:

```bash
pweb db-cli init
```

### 5. Run the Project

To run the project, execute the following command:

```bash
python pweb_app.py
```

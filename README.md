# Hospital Database Management System

Welcome to the **Hospital Database Management System**!  
This project is designed to streamline and manage hospital records using a simple, user-friendly interface. It integrates Python with a MySQL database to handle patients, doctors, appointments, and more.

---

## 🚀 Features

- Patient, Doctor, and Appointment Management
- Intuitive CLI (Command Line Interface)
- Secure, reliable, and scalable
- Easy to extend and maintain

---

## 🛠️ Technologies Used

- **Python** (Backend Logic)
- **MySQL** (Database)
- **mysql-connector-python** (Python-MySQL Bridge)

---

## 💻 Getting Started

Follow these steps to set up and run the project on your computer:

### 1. Clone the Repository

```bash
git clone https://github.com/anaghanoop/Hospital-Database-management-system-.git
cd Hospital-Database-management-system-
```

### 2. Install Python

Make sure you have **Python 3.x** installed.

- [Download Python](https://www.python.org/downloads/)

Verify the installation:

```bash
python --version
```

### 3. Install MySQL Server

- [Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/)

Follow the installation wizard and set a root password.

### 4. Install Required Python Packages

You need the `mysql-connector-python` package to connect Python with MySQL.

```bash
pip install mysql-connector-python
```


### 5. Set Up the Database

1. Open MySQL Workbench or use the MySQL CLI.
2. Create the database and tables as required (refer to any provided SQL scripts like `db_setup.sql`).
3. Update the database credentials in your Python files (usually in a config section or at the top of the main script):

```python
mydb = mysql.connector.connect(
  host="localhost",
  user="your_mysql_user",
  password="your_mysql_password",
  database="hospital_db"
)
```

### 6. Run the Project

Find the main Python file (such as `main.py` or `app.py`). Execute it:

```bash
python main.py
```

---

## 📋 Usage

- Follow the CLI prompts to add, update, or view patient and doctor records.
- Ensure your MySQL server is running before starting the application.

---

## 🤝 Contribution

Contributions are welcome!  
Feel free to fork the repository, make enhancements, and submit pull requests.

---

## 📧 Support

For any issues, please [open an issue](https://github.com/anaghanoop/Hospital-Database-management-system-/issues) in this repository.

---

## ⭐️ Don't forget to star the repo if you find it useful!

---

# 📊 dlt to PostgreSQL Pipeline (Beginner Data Engineering Project)

## 🚀 Overview

This project demonstrates building a simple **data pipeline** using **Python**, **dlt (data load tool)**, and **PostgreSQL**.

The pipeline loads sample (dummy) data into a PostgreSQL database while automatically handling:

* Schema creation
* Table creation
* Data insertion

The goal of this project is to understand **core data engineering fundamentals**, including:

* Data pipeline structure
* Database connections
* Configuration management
* Debugging real-world issues

---

## 🧠 Architecture

```
Python (dlt pipeline)
        ↓
PostgreSQL Database (dlt_db)
        ↓
Schema (test_dataset)
        ↓
Table (users)
```

---

## 🛠️ Tech Stack

* Python 3.x
* dlt (data load tool)
* PostgreSQL
* WSL (Windows Subsystem for Linux)
* Virtual Environment (venv)

---

## 📁 Project Structure

```
api_to_warehouse/
│
├── src/
│   ├── pipeline.py
│   └── .dlt/
│       └── secrets.toml.example   # sample config (no real credentials)
│
├── venv/                          # ignored
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install dlt psycopg2-binary
```

---

### 3. Start PostgreSQL (WSL)

```bash
sudo service postgresql start
```

---

### 4. Create Database & User

Open PostgreSQL:

```bash
sudo -u postgres psql
```

Run:

```sql
CREATE DATABASE dlt_db;
CREATE USER dlt_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE dlt_db TO dlt_user;
```

---

### 5. Configure dlt Credentials

Create file:

```
src/.dlt/secrets.toml
```

Add:

```toml
[destination.postgres.credentials]
database = "dlt_db"
username = "dlt_user"
password = "your_password"
host = "localhost"
port = 5432
```

⚠️ This file is excluded from Git using `.gitignore`.

---

### 6. Run the Pipeline

```bash
python src/pipeline.py
```

---

## ✅ Output

* Schema created: `test_dataset`
* Table created: `users`
* Data successfully loaded into PostgreSQL

---

## 🔍 Verification

Connect to database:

```bash
psql -U dlt_user -d dlt_db
```

Run:

```sql
SELECT * FROM test_dataset.users;
```

---

## ⚠️ Errors Faced & Solutions

### 1. PostgreSQL Authentication Error

**Error:**

```
Peer authentication failed
```

**Cause:**
PostgreSQL default authentication method (`peer`) was used.

**Solution:**
Updated config file:

```
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

Changed:

```
local   all   all   peer
```

To:

```
local   all   all   md5
```

Restarted PostgreSQL:

```
sudo service postgresql restart
```

---

### 2. Missing Credentials (dlt)

**Error:**

```
ConfigFieldMissingException
```

**Cause:**
`secrets.toml` was not in the expected directory.

**Solution:**
Moved `.dlt` folder inside `src/`.

---

### 3. Schema vs Database Confusion

**Clarification:**

* Database → `dlt_db`
* Schema → `test_dataset`
* Table → `users`

Query format:

```
schema_name.table_name
```

---

## 🔐 Security Best Practices

* Credentials are stored in `.dlt/secrets.toml` (not committed)
* `.gitignore` excludes sensitive files
* A template file (`secrets.toml.example`) is provided

---

## 💡 Key Learnings

* Understanding dlt pipeline structure
* Difference between database, schema, and table
* Handling PostgreSQL authentication issues
* Importance of configuration management
* Debugging real-world setup errors

---

## 🚀 Future Improvements

* Replace dummy data with real API (e.g., SpaceX API)
* Implement incremental loading
* Add logging and error handling
* Dockerize the pipeline
* Schedule pipeline execution

---

## 📌 Conclusion

This project builds a strong foundation in data engineering by focusing on core concepts and real-world debugging scenarios. It serves as a stepping stone toward building production-ready data pipelines.
# test

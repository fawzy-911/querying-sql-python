# Querying with SQL & Python

A Jupyter Notebook project that connects Python to the Chinook sample music-store database with SQLite, explores its schema, answers three business questions with SQL, loads results into Pandas, and charts the best-selling tracks.

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

## Setup and run

Create a virtual environment, activate it, and install dependencies:

```bash
python -m venv .venv
```

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
```

Download the sample database from the source project, then open the notebook:

```bash
python download_db.py
jupyter notebook chinook_queries.ipynb
```

The database is saved to `data/Chinook_Sqlite.sqlite`. It is downloaded from the [Chinook Database project](https://github.com/lerocha/chinook-database); the database file is not committed to this repository. Its MIT license is included in `CHINOOK_LICENSE.txt`.

## What the notebook answers

1. **Top-selling tracks:** total invoice-line quantity sold, with revenue as a tie-breaker.
2. **Top revenue country:** summed invoice totals grouped by billing country.
3. **Top sales employee:** total invoice revenue from customers assigned to each sales representative.

The notebook also lists database tables, columns, and foreign-key relationships. It uses `sqlite3`, Pandas, and Matplotlib; no database server is required.

## Project page

[roadmap.sh — Querying with SQL & Python](https://roadmap.sh/projects/querying-sql-python)


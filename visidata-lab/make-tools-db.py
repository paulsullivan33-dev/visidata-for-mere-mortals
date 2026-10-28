#!/usr/bin/env python3
"""Rebuild the lab's SQLite fixture, tools.db.

The guide opens tools.db with VisiData to show a database file
becoming a sheet of its tables. The database holds one table,
tools: a community tool library's lending shelf. Run this script
in this folder to recreate the file from scratch:

    python3 make-tools-db.py
"""

import os
import sqlite3

ROWS = [
    ("Step ladder", "Access", "no"),
    ("Cordless drill", "Power tools", "yes"),
    ("Hedge trimmer", "Garden", "yes"),
    ("Wheelbarrow", "Garden", "no"),
    ("Pressure washer", "Cleaning", "no"),
    ("Extension lead", "Electrical", "yes"),
]


def main():
    if os.path.exists("tools.db"):
        os.remove("tools.db")
    con = sqlite3.connect("tools.db")
    con.execute("CREATE TABLE tools (tool TEXT, category TEXT, on_loan TEXT)")
    con.executemany("INSERT INTO tools VALUES (?, ?, ?)", ROWS)
    con.commit()
    con.close()
    print("tools.db rebuilt: 1 table, 6 rows")


if __name__ == "__main__":
    main()

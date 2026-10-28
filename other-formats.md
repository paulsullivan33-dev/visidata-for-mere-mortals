# JSON, SQLite and Other Formats

VisiData's party trick is that the file's format mostly stops mattering once it is open: the sheet behaves the same whether it came from text, JSON or a database. But the *arrival* differs, and the differences teach you something about the formats themselves. This chapter opens the lab's other two fixtures.

## JSON: the types travel with the data

The workshops file, `visidata-lab/workshops.json`, is a list of six garden workshops, each an object with a title, a room, seats, bookings and a level. Open it exactly as you opened the CSV:

```bash
vd workshops.json
```

Check the headers against the catalogue's (transcript `visidata-lab/transcripts/t41-open-json.txt`):

```text
 booked │ level        │ room         │ seats │ title                     ║
 9     #│ beginner     │ Potting Shed │ 12   #│ Sowing Your First Seeds   ║
 20    #│ beginner     │ Garden Hall  │ 20   #│ Compost Basics            ║
```

`booked#`, `seats#` — integer marks, already there, and the numbers sit right-aligned from the first moment. Nobody pressed `#`. JSON *says* which of its values are numbers (they are written without quotes), and VisiData honours the file's own word. Put the two arrivals side by side and chapter 5's rule sharpens: **a format either carries types or it doesn't.** CSV doesn't, so its types are your job; JSON does, so they arrive done. Sorting, totalling and describing all work on this sheet immediately, for the same reason.

This file is flat — a list of objects with plain values. Real-world JSON nests: objects inside objects, lists inside objects. VisiData has machinery for unfolding those (expanding a nested value into columns of its own), which this guide describes rather than demonstrates: the lab's JSON was built flat on purpose, so the arrival story stayed clean. The principle survives the nesting — the types are in the file — but the *shape* work is a topic of its own, and chapter 14 lists it among the limits.

## SQLite: a database opens as its own index

The third fixture, `visidata-lab/tools.db`, is a SQLite database — the kind of single-file database the SQLite guide in this series is about — holding one table, `tools`, a tool library's lending shelf. (The lab's `make-tools-db.py` rebuilds it if you want to start clean.) Open it the same way:

```bash
vd tools.db
```

A database is not one table, so the first sheet is an **index of the tables inside** (transcript t42):

```text
 name  ║ rows   #│ cols#│ keys │ source ║
 tools ║       6 │    4 │      │ tools  ║
```

One row per table, with its row count. Press Enter on a table and you dive into it, exactly as you dived from a frequency row in chapter 7 (transcript t43):

```text
 tool            │ category    │ on_loan ║#│
 Step ladder     │ Access      │ no      ║
 Cordless drill  │ Power tools │ yes     ║
 Hedge trimmer   │ Garden      │ yes     ║
```

Three columns of data, and a slim fourth at the right edge, headed `#`: the table's **rowid**, the row numbers the database itself keeps, shown because a database row needs a handle and that is the handle it has. The status line keeps the stack from chapter 2 — `1›tools | 2›tools` — index below, table on top, `q` to climb back down. From here, everything you know applies: sort the shelf by category, count `on_loan` in a frequency table to learn how much of the library is currently out (three of six, the table says — try it), and so on. Sorts and selections are still views; saving edits back into a database is saving with the same care as chapter 9, on a file you have backed up first.

## The wider world of formats

These three are a sample, not the catalogue. VisiData ships with loaders for a long list — Excel workbooks, Parquet and other columnar files, HTML tables, XML, log files, even a directory of files treated as rows — and more arrive as plugins. The *behaviour* transfers: whatever opens becomes a sheet, with the same cursor, commands and stack. What varies is the arrival: whether types come with the file, whether the file holds one table or many, and whether saving back is possible at all. Those arrivals, for formats beyond the three the lab ran, are described from the project's documentation rather than demonstrated, and `criteria.md` keeps them in the documented-only column where they belong.

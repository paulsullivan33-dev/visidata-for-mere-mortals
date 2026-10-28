# VisiData for Mere Mortals

Somewhere on your machine there is a CSV file you need to understand: a catalogue, an export, a log somebody saved as a spreadsheet. Opening it in a full spreadsheet program works, but it is heavy machinery for a quick question — *what is in here, what is the biggest, how many of each kind are there, which rows are about to run out?* **VisiData** answers questions like those from the terminal. It opens a data file as a **sheet** — rows and columns on the screen — and lets you sort, select, summarise and even edit it with a handful of keystrokes, then puts the file back when you are done. Its command is `vd`.

This guide explains how that works: how a file becomes a sheet, how to read the screen, how to sort a column — and the trap hiding inside sorting, because a column of numbers can be in *word* order until you tell VisiData they are numbers. It covers selecting the rows you care about and lifting them into a sheet of their own, the frequency table that counts how many of each thing you have, the describe sheet that summarises every column at once, and the careful business of editing a cell and saving the file again. It also opens a JSON file and a SQLite database, and shows VisiData working with no screen at all, as a file converter.

The lab behind this guide ran the real thing: **VisiData 3.4**, installed with pip into a fresh virtual environment on a small Linux machine, driven in a terminal against three fixtures the lab made for the purpose — a fourteen-row seed catalogue as a CSV, six garden workshops as JSON, and a SQLite database of a tool library's lending shelf. Against those files the lab sorted (wrongly, then rightly), selected rows two different ways, counted crops in a frequency table and added up their stock, edited a price and saved it, and read the saved file back from disk to prove the change had landed. The mistakes are kept, not tidied away: a selection that matched nothing, an edit that mangled the price into `2.752.50`, a save the program refused because the lab answered its question wrong. Each one taught something the tidy version would have hidden, and each is labelled where it appears.

What the lab could not do, it did not fake. VisiData has more loaders than three — Excel workbooks, Parquet files, web APIs and a directory full of other formats are described from the documentation and labelled as such. Its graph view needs a screen to look at, so plotting is likewise described rather than demonstrated. `criteria.md` keeps the full ledger of what was run and what was only read.

## What this guide covers

- [**What VisiData is**](what-visidata-is.md) — the mental model: a file becomes a sheet, questions become keystrokes, and the screen is a view, not the data
- [**The moving parts**](the-moving-parts.md) — sheets and the sheet stack, columns and their types, the cursor, the status line that names every command you run, and where your changes live until you save
- [**Installing VisiData**](installing-visidata.md) — the pip install into a virtual environment, checking the version, and what `vd` needs to run
- [**Your first sheet**](your-first-sheet.md) — opening the seed catalogue, reading the screen, moving around, and searching a column
- [**Sorting and types**](sorting-and-types.md) — the sort that put 5 after 47, why it happened, and the one key that fixes it: a column's type is a claim you make, not a guess the tool makes for you
- [**Selecting rows**](selecting-rows.md) — marking rows with a bullet, lifting them into a sheet of their own, and the pattern select that matches against one column only
- [**Frequency tables**](frequency-tables.md) — counting how many of each thing, diving from a count into the rows behind it, and adding up a number per group
- [**The Describe and Columns sheets**](describe-and-columns.md) — two sheets about your sheet: one lists every column and its type, the other hands you the statistics
- [**Editing and saving**](editing-and-saving.md) — changing a cell, the quit that throws your edit away without asking, and the save dialog with its overwrite question
- [**JSON, SQLite and other formats**](other-formats.md) — a JSON file whose numbers arrive already typed, and a database that opens as an index of its tables
- [**VisiData without the screen**](without-the-screen.md) — batch mode: converting one format to another with a single command and no interface at all
- [**Recipes**](recipes.md) — the reorder list, the price check, the quick census of any column, tidying an export for someone else
- [**The neighbours**](the-neighbours.md) — spreadsheet programs, the database's own command line, pandas, csvkit and Miller: what each does that VisiData doesn't, and vice versa
- [**Limits**](limits.md) — one sheet in memory at a time, types it will not guess, formats it cannot write back, and the files too big for the room, stated plainly
- [**Troubleshooting**](troubleshooting.md) — numbers in the wrong order, a selection that matched nothing, an edit that grew a tail, a save that said *disconfirmed*, and the traps this guide's lab fell into so you don't have to
- [**Glossary**](glossary.md) — the terms, collected in one place

## What it doesn't cover

VisiData as a programming platform — it is extensible with Python, and people build on it, but this guide stays with the tool as its users meet it. Heavy data engineering, joining warehouse-scale tables, and the statistical work that belongs to a notebook are pointed at, not taught; chapter 13 names the neighbours that do those jobs. The graph and plot views are described from the documentation, because a chart is something to look at and this lab's evidence is text. And one boundary worth stating in the open: a tool that can rewrite a data file in place can also ruin one, so the guide's editing chapter works on a copy first — a habit worth keeping, not a limitation of the tool.

## How to use this guide

Read chapter 1 for the model and chapter 2 before opening anything — knowing which part holds what turns later confusion into a named problem. Chapter 4 opens your first sheet in the same sitting as the install, against the lab's seed catalogue; keep that file nearby, because chapters 5 to 8 all work on it. Do not skip chapter 5: the sorting trap is the single most important lesson in the guide, and it is much cheaper to meet it in the lab's file than in your own. Chapter 9 is the one that turns a viewer into an editor — work on a copy of a file, as the lab did, until saving feels boring. The lab's fixtures live in `visidata-lab/` and its session transcripts in `visidata-lab/transcripts/`; `visidata-lab/lab-notes.txt` explains what each one is.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [SQLite for Mere Mortals](https://paulsullivan33-dev.github.io/sqlite-for-mere-mortals/)
- [DuckDB for Mere Mortals](https://paulsullivan33-dev.github.io/duckdb-for-mere-mortals/)
- [Text Processing for Mere Mortals](https://paulsullivan33-dev.github.io/text-processing-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/visidata-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/visidata-for-mere-mortals/blob/main/LICENSE-CODE).

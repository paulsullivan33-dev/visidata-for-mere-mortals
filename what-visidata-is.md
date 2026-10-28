# What VisiData Is

Most data in ordinary life sits in **tabular files**: rows and columns saved as text. A CSV of a shop's stock, a JSON export from some service, a small database that came with an application. When you want to know something about one of these files, the usual options are out of proportion to the question. A spreadsheet program opens a window, a ribbon, a recent-documents list. A programming language wants a script. A database wants the file imported first.

**VisiData opens the file as a sheet, in the terminal you already have open.** Type `vd` and the file's name, and the data is on the screen: rows down the side, columns across the top, a cursor you move with the arrow keys or `h`/`j`/`k`/`l`. From there, questions become keystrokes. Sort this column: one key. Count how many of each thing there are: two keys. Show me only the rows that are about to run out: a few keys. The file itself is not touched while you explore — the sheet is a view of the data, held in memory — and if you do change something, nothing reaches the disk until you deliberately save.

A **sheet**, in VisiData's vocabulary, is any screenful of rows and columns it shows you. The word covers more than files. A sheet can be the rows of a CSV, yes — but also a table inside a database, a count of how often each value appears, a list of the columns themselves, or a summary of statistics. Sheets open on top of each other, and half of learning VisiData is learning to see a question as *the sheet that would answer it* (chapter 2 takes this apart properly).

## Why anyone would do this

Four honest reasons account for most of it:

- **The quick question.** A file lands on your machine and you need to know what is in it before you decide what to do with it. VisiData answers in seconds, without importing, uploading or reformatting anything.
- **The tidy-up.** Exports arrive with the wrong order, extra rows, one wrong value. Sorting, selecting and a small edit — all checkable on the screen before anything is written — are often the whole job.
- **The census.** *How many of each? What is the total per group? What is the average?* The frequency table and describe sheet (chapters 7 and 8) are these questions, built in.
- **The conversion.** The file is CSV and the next program wants JSON, or the other way round. VisiData reads one format and writes another, including with no screen at all (chapter 11).

## A first taste

After installing (chapter 3), open the lab's seed catalogue — a small garden shop's stock list, kept in `visidata-lab/`:

```bash
vd seeds.csv
```

The screen fills with the catalogue. The status line at the bottom introduces the sheet, as in the lab's transcript `visidata-lab/transcripts/t01-open-csv.txt`:

```text
 crop      │ variety            │ packets │ price │ sow_month │ days_to_harvest ║
 Tomato    │ Gardener's Delight │ 42      │ 2.50  │ March     │ 70              ║
 Tomato    │ Moneymaker         │ 17      │ 2.20  │ March     │ 75              ║
 Carrot    │ Nantes 2           │ 58      │ 1.80  │ April     │ 70              ║
```

and at the very bottom:

```text
1›seeds|                                                                                                              14 rows [1/1]
```

Fourteen rows, one sheet, nothing yet changed. Every chapter from here is a way of asking this sheet a sharper question.

## Who it is for

The person who receives data files more often than they build them. The maintainer of a small system whose truth lives in a CSV somewhere. The curious, who learn a dataset the way they learn a room — by walking around in it. The common thread is one person, one file, and a question the file itself can answer if you can see it properly.

## What it is not

VisiData is not a database: it holds the file it opened in memory and lets it go when you quit; there is no server, no accounts, no permanence of its own (for that, the SQLite guide in this series goes deeper). It is not a spreadsheet program either, in the ways that matter to some people: there are no formulas living in cells waiting to recalculate, no charts to polish for a presentation, no printing to speak of — chapter 13 is honest about the neighbours that do those things. It is not a programming language, though it will happily run a small Python expression if you ask (and chapter 12 shows one doing honest work). And it is not a viewer in the passive sense: it can edit and overwrite your files, which is power worth respecting — the guide's standing advice, from chapter 9 on, is to learn on copies.

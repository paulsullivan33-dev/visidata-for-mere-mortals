# The Neighbours

VisiData lives in a crowded neighbourhood of tools that touch tabular data. These are characterised, not benchmarked — what each one *is*, and the shape of job where it beats this guide's tool, and vice versa.

## The spreadsheet programs

Excel, LibreOffice Calc, Google Sheets and their kin are the incumbents: cells you can see and format, formulas that live in the grid and recalculate, charts, printing, comments, several people editing at once. For a document that is *meant to be looked at* — a budget, a report, a form — they are the right tool and it is not close. VisiData's ground is the opposite end of the job: a file nobody formatted for looking at, a question that takes twenty seconds, a machine with no desktop at all. If the file is an *artifact to explore*, VisiData opens it faster and asks less of you; if it is a *document to present*, take the spreadsheet.

## The database's own tools

The `sqlite3` command line (and DuckDB, whose guide is a sibling of this one) speak **SQL**: a real query language. Joins between tables, grouping with conditions, the same question asked every day against fresh data — that is SQL's home, and no amount of keystrokes replaces it. VisiData reads a SQLite file beautifully (chapter 10) but it is *looking*, not *querying*: when the question has an *and the rows from the other table where…* in it, you have outgrown the sheet and should go where the language is. The honest workflow many people settle into is both: VisiData to learn what the data looks like, SQL to interrogate it.

## pandas

pandas is Python's data library: load a file into a program and every statistical, reshaping and plotting operation becomes code. It is incomparably more powerful than anything in this guide — and it is *programming*: you write, run, read an error, write again. VisiData is what you reach for before pandas, to see whether the file is what the sender claimed, and sometimes instead of it, when the question was only ever *how many of each*.

## csvkit

csvkit is a family of small command-line tools — `csvlook` to print a CSV readably, `csvstat` for summary statistics (a close cousin of chapter 8's describe sheet), `csvgrep`, `csvcut`, and friends. Each does one job and passes the result along a pipeline, *streaming* the file rather than loading it, so files far too big for memory are ordinary work. VisiData cannot stream: its whole model is the file, present, in front of you. If the file fits on a screen's worth of attention, VisiData is the pleasanter place; if it doesn't fit in memory at all, csvkit's country begins.

## Miller

Miller (`mlr`) is cut, sort and join rebuilt for structured records — CSV, JSON and several more — with verbs instead of column positions, also streaming, also pipeline-shaped. It overlaps csvkit's territory with a more uniform grammar. The difference from VisiData is the same as with pandas, in miniature: Miller is something you *write*; VisiData is somewhere you *stand*.

## jq

jq is a complete query language for JSON alone: filtering, reshaping, and rebuilding JSON documents in a pipeline, from the Text Processing family of skills. VisiData opens JSON as a sheet and lets you wander it; jq performs surgery on it without ever showing it to you. Chapter 11's conversions are where they meet: a jq user converts nothing — they transform. A VisiData user converts constantly and transforms by hand. Know which job you have.

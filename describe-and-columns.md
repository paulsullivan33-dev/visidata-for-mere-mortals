# The Describe and Columns Sheets

Two of VisiData's sheets are about your sheet rather than in it. Between them they answer *what shape is this data?* — the question to ask before any other.

## The Columns sheet: the sheet's table of contents

Press `Shift+C` anywhere and you get one row per column (transcript `visidata-lab/transcripts/t12-columns-sheet.txt`):

```text
 name            ║ width#│ type │ fmtstr │ value       │ aggregators │ sortorder#║
 crop            ║    11 │      │        │ Carrot      │             │          ⌀║
 variety         ║    20 │      │        │ Autumn King │             │          ⌀║
 packets         ║     9 │      │        │ 0           │             │         1 ║
```

Each row tells you the column's name, its display width, the value it holds on the row your cursor came from, any aggregators attached (chapter 7), and its place in the current sort order — packets shows `1` because it was the sort key. And the column this guide keeps pointing at: **type**, empty for all six in this capture, because the catalogue is a CSV and chapter 5's rule held. The Columns sheet is the quickest health check a new file can get: one glance tells you which columns the tool understands as numbers and which it is still reading as words.

## The Describe sheet: every column, summarised

Press `Shift+I` and VisiData computes a row of statistics per column (transcript t25):

```text
 column          ║ errors  ♯│ nulls   ♯│ distinct♯│ mode    ~│ min     ~│ max     ~│ sum      │ median  ~│ mean    %│ stdev   %║
 crop            ║        0 │        0 │       11 │ Carrot   │          │          │          │          │         !│         !║
 packets         ║        0 │        0 │       14 │ 0        │ 0        │ 73       │ 422     #│ 23.5     │    30.14 │    23.22 ║
 sow_month       ║        0 │        0 │        4 │ April    │          │          │          │          │         !│         !║
```

Read it in two halves. The left half is for every column: how many values failed to be what they claim (**errors**), how many are empty (**nulls**), how many distinct values there are, and the commonest value (**mode** — April is the busiest sowing month; there are only four distinct months in the file). The right half is for numbers only, and it is where the type lesson completes itself. The packets column — the one the lab typed with `#` — gets the full treatment: minimum 0, maximum 73, a total stock of 422 packets, median 23.5, mean 30.14. The untyped columns get blanks for min and max, and for mean and standard deviation a blunt `!`: *this cannot be computed*, the error mark rather than a silent zero. VisiData would rather show you a refusal than a plausible-looking nothing.

That pairing — the Columns sheet to see the types, the Describe sheet to see their consequences — is the two-minute examination to give any file you have just been handed. A column of numbers that shows `!` for its mean is a column to type (chapter 5) before you believe anything computed from it. A distinct count that surprises you — eleven crops, really? — is an invitation to that column's frequency table (chapter 7) to see the values themselves.

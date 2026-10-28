# Glossary

**Aggregator** — a summary attached to a column, such as `sum` or `mean`, whose results appear when another column is grouped in a frequency table. Added with `+`.

**Batch mode** — VisiData run with `-b`, with no screen: read this file, write that format, exit. Chapter 11.

**Bin** — the set of source rows sharing one value in a frequency table; also, the frequency table's row that stands for them.

**Bullet** — the `•` marking a selected row at the sheet's left edge. The status line counts them (`•3`).

**Cell editor** — the small text field a cell becomes when you press `e`. It has its own keys; Ctrl+K and Ctrl+U clear rightward and leftward from the cursor.

**Column, current** — the column the cursor is standing on. Most commands act on it, which makes "which column am I on?" the first diagnostic question.

**Columns sheet** — the sheet (Shift+C) listing your sheet's columns with their widths, types, aggregators and sort places.

**Describe sheet** — the sheet (Shift+I) of per-column statistics: errors, nulls, distinct values, mode, and — for typed numeric columns — min, max, sum, median, mean and standard deviation.

**Dup sheet** — a new sheet holding only the selected rows, opened with `"`. A view; the source sheet is unchanged.

**Expression column** — a column VisiData computes from a Python expression over the other columns, added with `=`.

**Frequency table** — the sheet (Shift+F on a column) counting each distinct value's occurrences, with percentages and a histogram.

**Key column** — the column treated as the rows' identity, drawn with the heavier edge. By default, the first column.

**Loader** — the part of VisiData that knows how to read one format — CSV, JSON, SQLite and many more — and present it as a sheet.

**Modified** — the `[M]` in the status line: the sheet holds changes the file does not. Unsaved changes live in memory only.

**Quitguard** — the option (`quitguard`, off by default; the `guard-sheet` command sets it per sheet) that makes VisiData confirm before closing a modified sheet.

**Regular expression** — the pattern notation for matching text, used by `/` searching and `|` selecting within a column: `^Lettuce` means *begins with Lettuce*.

**Rowid** — the row number a SQLite table keeps for each of its rows, shown by VisiData as a slim extra column when a table is opened.

**Saver** — the counterpart of a loader: the part that writes a sheet back out as a file, in its format's dialect.

**Sheet** — any screenful of rows and columns VisiData shows: a file, a table, a frequency table, a list of columns, a set of statistics.

**Sheet stack** — the pile of sheets you have opened, one on another, shown at the left of the status line (`1›seeds | 2›tools`). `q` pops the top one off.

**Status line** — the bottom line of the screen: the stack, the last command's name, the row count, the selection count, and `[M]`. VisiData narrates itself here; read it first when confused.

**Statuses** — the little stack of recent messages kept in the corner above the status line, where confirmations and refusals (such as `disconfirmed`) are recorded.

**Type** — a column's declared kind: text, integer (`#`), decimal (`%`), date (`@`), and others. Decides sorting, arithmetic and what the statistics can compute. CSV columns arrive untyped; the type is set by you.

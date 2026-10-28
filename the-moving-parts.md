# The Moving Parts

VisiData is one program, but five ideas do all the work. Learn these and every chapter afterwards is a variation on a theme.

## Sheets, and the stack of sheets

A **sheet** is a screenful of rows and columns. Your file opens as one. Press a key and another sheet may open on top of it — the rows behind one count, the list of columns, the statistics. The sheets form a **stack**, and the bottom line of the screen keeps your place in it. When the lab had dived from the seed catalogue into one table of a database, the status line read:

```text
1›tools | 2›tools|
```

That is the stack: sheet 1 underneath (the database's index of tables), sheet 2 on top (the table itself). The key `q` closes the top sheet and puts you back on the one below; closing the bottom sheet leaves the program. Nothing about exploring is destructive, because opening a sheet never changes the one beneath it.

## The cursor, in two halves

The cursor has a row half and a column half, and VisiData cares about them separately. Moving up and down (`k` and `j`, or the arrow keys) chooses the row you are looking at. Moving left and right (`h` and `l`) chooses the **current column** — and most commands apply to the current column: sorting sorts by it, the frequency table counts it, searching searches *inside* it (chapter 4). A remarkable number of beginner surprises are really "the command did exactly what I asked, to the column I was standing on, which was not the column I was thinking about." This guide's lab produced two of those, and kept both.

## Columns and their types

Every column has a **type**: text, integer, decimal number, date, and a few more. The type decides how the column behaves — how it sorts, whether it can be totalled, how it is written back to disk. Here is the fact the whole guide turns on, stated early so chapter 5's trap is no ambush:

> **For a CSV file, VisiData guesses nothing. Every column arrives untyped — its values are text — until you set a type yourself.**

Other formats differ: a JSON file's numbers are numbers in the file itself, so they arrive typed (chapter 10 shows the contrast on the screen). For CSV, the type is yours to declare, with one key per kind: `#` makes the current column integers, `%` makes it decimals, `~` makes it text, `@` makes it dates. A typed column shows its mark in the header — `packets#` is an integer column named packets — and its numbers line up on the right, where numbers belong.

## Rows you can mark

Rows can be **selected**: marked with a bullet, `•`, at the left edge. Selection is how you say *these ones* — the rows to copy into a sheet of their own (chapter 6), the rows a count or a save should care about. Unselected rows are not deleted or hidden; they are simply not the ones you marked. Selection is a view, like everything else here, until the moment you save.

## The status line, your narrator

The bottom line of the screen is worth learning to read, because it narrates. On the left, the sheet stack and the sheet's name. In the middle, when you run a command, **the command's name appears** — `#` echoes as `type-int`, `s` as `select-row`, `[` as `sort-asc`. This is a quiet gift to learners: every key you press tells you the name of the thing it did, and those names are the vocabulary of the built-in help. On the right, the shape of the sheet: `14 rows`, a `•3` if three rows are selected, and `[M]` if the sheet holds changes that are not yet saved. That `[M]` matters more than it looks; chapter 9 is about it.

Above the status line, in the corner, VisiData also keeps a little stack of recent messages — things it wants you to know it did, including refusals. When a save in chapter 9 was declined, the reason (`disconfirmed`) was waiting in that corner. If a command seems to have done nothing, look there before pressing more keys.

## Where your changes live

Until you save, everything — sorts, selections, edits, new types — lives in memory, as the sheet's opinion about the file, not the file. Saving is a separate, deliberate act (Ctrl+S), and quitting is happy to discard the opinion without asking (chapter 9 shows that happening, once, to the lab). This split is the tool's character: **looking is free and safe; writing is a decision.** Learn to love the split and VisiData is a safe place to explore data you would not dare open in something that writes as it goes.

# Frequency Tables

*How many of each?* It is the commonest question asked of any dataset, and VisiData answers it with a sheet of its own: the **frequency table**. Stand on a column, press `Shift+F`, and every distinct value in that column gets a row, with the count of how often it occurs, its share as a percentage, and a bar drawn to scale.

Here it is for the crop column of the seed catalogue (transcript `visidata-lab/transcripts/t04-frequency-crop.txt`):

```text
 crop      ║↓count  ♯│ percent%│ histogram                             ~║
 Lettuce   ║       2 │   14.29 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 Carrot    ║       2 │   14.29 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 Tomato    ║       2 │   14.29 │ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║
 Radish    ║       1 │    7.14 │ ■■■■■■■■■■■■■■■■■■■                    ║
```

Three crops are stocked in two varieties each; the other eight have one apiece. The table arrives sorted by count, biggest first — note the `↓` on the count column — and it is an ordinary sheet in every other way: you can sort it by the value column instead, or move around it like any other. When it opens, a description panel explains what you are looking at; it is worth reading once, because it also explains the next trick.

## Diving into a row

Each row of the frequency table stands for a set of rows back in the source sheet — a **bin**. Press Enter on a bin and VisiData opens a copy of the source sheet holding *only that bin's rows*. On the Lettuce bin, the lab got the whole lettuce department (transcript t05): Butterhead and Lollo Rosso, both rows, nothing else. `q` closes the copy and returns to the frequency table; another `q` returns to the catalogue. Counting and inspecting become one motion: *how many lettuces? two — which ones? these.*

## Adding up, per group

Counts are the beginning. Often the question is a total per group: not how many tomato varieties, but how many tomato *packets*. That takes an **aggregator** — a summary you attach to a column. Stand on the packets column (typed as integers, as chapter 5 taught), press `+`, and a chooser opens at the bottom of the screen:

```text
choose aggregators: _
```

Type the summary's name — `sum` — then Tab to complete it and Enter to attach it (the lab's chooser is transcript t27). Now open the frequency table on crop again (transcript t29):

```text
 crop      ║↓count  ♯│ packets_sum#║
 Tomato    ║       2 │          59 ║
 Carrot    ║       2 │          58 ║
 Lettuce   ║       2 │          54 ║
 Pea       ║       1 │          64 ║
```

A new column, `packets_sum`, carries the totals: tomatoes 42 + 17 = 59 packets, carrots 58 + 0 = 58, lettuces 33 + 21 = 54 — and the pea, a single row, outranks them all with 64. Other aggregators live in the same chooser (`min`, `max`, `mean`, and more); the mechanism is identical: attach to a column first, then group by another column in its frequency table. Two habits protect you here. The column being added must be *typed* — an aggregator over words has nothing to add, which is chapter 5's lesson arriving by another road. And the frequency table is a summary, not the data: when a number looks odd, dive into its bin with Enter and read the rows themselves before believing it.

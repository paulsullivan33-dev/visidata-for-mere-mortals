# VisiData Without the Screen

Everything so far has needed a person at a keyboard. But the same engine that draws sheets also runs as a plain command — **batch mode** — for the jobs that are pure conversion: *this file, as that format*. No screen opens; the command reads, writes, and returns your prompt.

```bash
vd -b seeds.csv -o seeds-converted.json
```

The `-b` says batch. The output format is chosen by the name you give the output: `.json` here, so the catalogue becomes a JSON array of objects, one per row (transcript `visidata-lab/transcripts/t44-batch-convert.txt`):

```text
[
{"crop": "Tomato", "variety": "Gardener's Delight", "packets": "42", "price": "2.50", "sow_month": "March", "days_to_harvest": "70"},
{"crop": "Tomato", "variety": "Moneymaker", "packets": "17", "price": "2.20", "sow_month": "March", "days_to_harvest": "75"},
```

Read those values once more, because batch mode repeats chapter 5's lesson in a new accent: `"packets": "42"` — the stock count came out as a **string**, in quotes, because it went in as one. The conversion was faithful: it converted the file VisiData had, and what VisiData had was untyped text. A conversion is not a cleansing. If the output's types matter to whoever receives it, open the file interactively first, set the types there, and save — or accept strings knowingly.

The other direction is just as plain. The workshops, JSON to a tab-separated file for a spreadsheet-bound colleague:

```bash
vd -b workshops.json -o workshops.tsv
```

```text
booked	level	room	seats	title
9	beginner	Potting Shed	12	Sowing Your First Seeds
20	beginner	Garden Hall	20	Compost Basics
```

Batch mode is the right size for a surprising amount of real work: the nightly export that must change shape, the database table a colleague wants as a CSV, the JSON a program produced that a human wants as a table. It uses the same loaders and savers as the interactive tool — chapter 10's formats included — so a conversion you have checked once by eye, in the sheet, behaves the same way unattended. The division of labour this guide recommends: **explore interactively, where mistakes are visible; convert in batch, once the shape is known.** A batch conversion of a file you have never opened is a leap of faith in exactly the places — types, shapes, stray rows — where this guide has watched faith go unrewarded.

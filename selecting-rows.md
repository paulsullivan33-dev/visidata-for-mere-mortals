# Selecting Rows

Sorting arranges the whole sheet. **Selecting** is the opposite move: you point at a few rows and say *these are the ones I mean* — the ones about to run out, the ones from one supplier, the ones to copy somewhere else. Selected rows wear a bullet, `•`, at the left edge. This chapter selects the seed catalogue's three lowest-stock rows, and — because the lab got it wrong first — shows the wrong way as well.

## One key, one row, one step down

The key is `s`, and its full behaviour is: *select this row, then step down one.* That second half is a convenience once you know it and a trap until you do. The lab, not yet knowing, pressed `s j s j s` — select, down, select, down, select — expecting three neighbours. It got rows 1, 3 and 5 (transcripts t20 and t21): the bullets landed on the carrots with 0 packets, the leeks with 15 and the lettuces with 21, skipping the peppers and courgettes entirely, because each `s` had already done the stepping and each `j` stepped again.

Knowing the rule, the job is simply `s` three times from the top of the packets-sorted sheet (transcript t23):

```text
 crop      │ variety            │↑packets#│ price │ sow_month │ days_to_harvest ║
•Carrot    │ Autumn King        │       0 │ 1.95  │ May       │ 80              ║
•Pepper    │ California Wonder  │       5 │ 2.90  │ February  │ 85              ║
•Courgette │ Defender           │       9 │ 2.30  │ May       │ 50              ║
```

Check the status line as you go: it counts for you — `14 rows  [M] •3` once three rows are marked. (`[M]` appears because a selection, like any change of mind about the sheet, is an unsaved state; chapter 9 explains.) To start over, `g` then `u` unselects everything — *unselect-rows* — and the bullets and the count vanish.

## Lifting the marked rows into their own sheet

A selection is most useful when it becomes a sheet of its own. Press `"` — the *dup-selected* command — and a new sheet opens holding only the selected rows (transcript t24):

```text
1›seeds | 3›seeds_selectedref|                                                               "   dup-selected          3 rows [1/1]
```

There is the reorder list, alone on a screen: carrots, peppers, courgettes. This sheet can be saved under its own name (chapter 9's save works on any sheet), printed, or simply read and closed with `q`. The original sheet underneath is untouched — still fourteen rows, still sorted. Dup sheets are views, all the way down.

## Selecting by pattern — and its honest limit

Selecting by hand suits a handful of rows. For *every row where this column says so*, there is `|`: stand on a column, press `|`, type a pattern, and every row whose value in **that column** matches is selected. Standing on crop, the lab typed `^Lettuce` — *begins with Lettuce* — and got exactly the two lettuce rows (transcript t30, status: `select-col-regex … •2`).

The pattern language is a **regular expression** — the pattern notation from the Text Processing guide in this series — matched against the one column you are standing on. Hold on to that limit, because the lab's first attempt broke on it. Wanting "packets under 10", the lab stood on the crop column, pressed `|` and typed `packets < 10`, expecting something like a spreadsheet's filter formula. What it got (transcript t07) was a polite nothing:

```text
selected 0 rows
```

— because no *crop name* contains the text `packets < 10`. VisiData even opened the follow-up dup sheet without complaint: an empty sheet, header and no rows (transcript t08). No error, because no error occurred: a pattern matched against the wrong column simply matches nothing. The tool is literal-minded in a way that rewards a second's thought about *which column, which language* before pressing keys. For "numbers below a value", the working method is this chapter's first half: type the column (chapter 5), sort it, and select the rows at the top by hand. For "text matching a pattern in this column", `|` is the tool. Each does one job; the craft is knowing which job you have.

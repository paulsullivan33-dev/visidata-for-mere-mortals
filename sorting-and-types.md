# Sorting and Types

Sorting is the first thing most people ask a sheet to do, and VisiData makes it one key: stand on a column and press `[` for ascending order, `]` for descending. The header grows an arrow to show the sort — `↑price` means *this sheet is in rising price order*. This chapter sorts the seed catalogue twice. The first sort looks perfect and the second is quietly wrong, and the difference between them is the most useful thing in this guide.

## The sort that looked right

Stand on the price column (three `l` presses from the left edge) and press `[`. The catalogue lines up from the 1.20 radishes to the 2.90 peppers (transcript `visidata-lab/transcripts/t03-sorted-by-price.txt`):

```text
 crop      │ variety            │ packets │↑price │ sow_month │ days_to_harvest ║
 Radish    │ French Breakfast   │ 73      │ 1.20  │ April     │ 30              ║
 Spinach   │ Perpetual          │ 47      │ 1.50  │ March     │ 40              ║
 Lettuce   │ Butterhead         │ 33      │ 1.60  │ April     │ 45              ║
```

Cheapest at the top, priciest at the bottom, exactly as asked. Nothing about this screen warns you about anything.

## The sort that told the truth

Now stand on the packets column (two `l` presses) and press `[` again — sort by stock, least first, to find what is running out. Check the result against your expectations (transcript t11):

```text
 crop      │ variety            │↑packets │ price │ sow_month │ days_to_harvest ║
 Carrot    │ Autumn King        │ 0       │ 1.95  │ May       │ 80              ║
 Bean      │ Blue Lake          │ 12      │ 2.40  │ May       │ 60              ║
 Leek      │ Musselburgh        │ 15      │ 2.05  │ April     │ 100             ║
 Tomato    │ Moneymaker         │ 17      │ 2.20  │ March     │ 75              ║
```

So far, plausible — and then, further down, the order falls apart: after 47 comes **5**, then 58, 64, 73, and dead last, **9**. The peppers with 5 packets and the courgettes with 9 are not at the top where they belong. Nothing crashed. The sort did precisely what it was asked to do — *to text*. Look at the sequence as words: `0`, `12`, `15`, `17`, `21`, `26`, `33`, `42`, `47`, `5`, `58`, `64`, `73`, `9`. As spellings, that is perfect alphabetical order: everything beginning with 1, then 2, then 3, then 4, then — at last — the words beginning with 5 and 9. The packets were never numbers in VisiData's eyes. They were little strings that happened to be made of digits.

Why did price escape? Because in this file every price is written the same way — one digit, a point, two decimals — so word order and number order agree, pair by pair. The trap does not announce itself; it waits for a column whose spellings vary in length.

## Types: the claim you make

Recall chapter 2's rule: **a CSV brings no types with it.** Every column arrives untyped, its values held as text, and such operations as sorting treat them accordingly. The Columns sheet — press `Shift+C` — shows the situation plainly (transcript t12): one row per column, and the *type* cell empty for every single one.

The fix is a claim, made by you, with one key per type. Stand on the packets column and press `#` — the command for *this column is integers*. Check the header (transcript t18):

```text
 crop      │ variety            │ packets#│ price │ sow_month │ days_to_harvest ║
 Tomato    │ Gardener's Delight │      42 │ 2.50  │ March     │ 70              ║
```

Three things changed at once. The header now reads `packets#` — the `#` is the integer mark. The values line up on the **right**, as numbers do. And the status line names what happened: `#   type-int`. The family of type keys is small and worth learning whole:

- `#` — integers
- `%` — decimal numbers (floats)
- `~` — text, for when a column of digits is really a code and should be treated as words
- `@` — dates

Now press `[` on packets again (transcript t19):

```text
 Carrot    │ Autumn King        │       0 │ 1.95  │ May       │ 80              ║
 Pepper    │ California Wonder  │       5 │ 2.90  │ February  │ 85              ║
 Courgette │ Defender           │       9 │ 2.30  │ May       │ 50              ║
 Bean      │ Blue Lake          │      12 │ 2.40  │ May       │ 60              ║
```

0, 5, 9, 12 — number order, and the reorder list writes itself: Autumn King carrots are *out*, peppers and courgettes are nearly out.

## The lesson to keep

Sorting never lies; it sorts what the column *is*, and for a CSV what the column is, is text until you say otherwise. So the habit to build is: **before trusting any order, total or average from a CSV, glance at the headers.** A `#` or `%` where you expect numbers means the tool knows. No mark means you are reading words that look like numbers — which is fine for reading, and treacherous for everything else. Chapter 8's statistics make the same point from the other side: the describe sheet simply refuses to average a column of words.

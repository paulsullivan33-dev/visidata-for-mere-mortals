# Your First Sheet

This chapter opens one file and reads it properly: what the screen is showing you, how to move around in it, and how to find a word — with every step checked against the lab's own session.

The file is the lab's seed catalogue, `visidata-lab/seeds.csv`: fourteen rows of seeds for a small garden shop, with columns for the crop, the variety, how many packets are in stock, the price, the sowing month, and how long the crop takes. Open it:

```bash
vd seeds.csv
```

Check: your sheet appears, headed by the column names from the file's first row, with the first row of data under the cursor (transcript `visidata-lab/transcripts/t01-open-csv.txt`):

```text
 crop      │ variety            │ packets │ price │ sow_month │ days_to_harvest ║
 Tomato    │ Gardener's Delight │ 42      │ 2.50  │ March     │ 70              ║
 Tomato    │ Moneymaker         │ 17      │ 2.20  │ March     │ 75              ║
 Carrot    │ Nantes 2           │ 58      │ 1.80  │ April     │ 70              ║
 Carrot    │ Autumn King        │ 0       │ 1.95  │ May       │ 80              ║
```

Read the screen in three bands. Across the top, a menu line (File, Edit, View, and friends) and VisiData's name — mostly decoration for now. In the middle, the data, with a header row: the first column is marked with a heavier edge because crop is the sheet's **key column**, the column VisiData took as the rows' identity (the first column, by default). At the bottom, the status line from chapter 2: `1›seeds | 14 rows [1/1]` — one sheet on the stack, named *seeds* after the file, fourteen rows in it.

## Moving

The cursor keys all work, and so do the letter keys from the vi tradition: `k` up, `j` down, `h` left, `l` right. Two jumps are worth learning on the first day:

- `gg` goes to the first row. The status line confirms it in its narrating way: `gg   go-top`.
- `Shift+G` goes to the last row — the lab's status line again: `Shift+G   go-bottom` (transcript t45).

Move the row cursor down the catalogue and the column cursor across it, and watch what changes: the row and column you are standing on are highlighted, and *that pair* — this row, this column — is where the next command will act. Almost every VisiData skill is a way of putting the cursor somewhere meaningful and then pressing one meaningful key.

## Finding a word

Press `/` and type a word, then Enter, to search. The catch — the first appearance of a theme in this guide — is that **search looks in the column you are standing on**, not the whole sheet. Standing on the crop column, the lab searched for the leeks (transcript t46):

```text
1›seeds|                                                                                       /   search-col         14 rows [1/1]
```

The cursor landed on the Leek row. Press `n` to go to the next match (`search-next`); here there is only one leek, so the search wraps back to it. If you search a column for a word that lives in a different column, you will be told there are no matches, and the message is telling the truth — about that column. When a search finds nothing, the first question to ask is not *is it in the file?* but *am I standing in the right column?*

## Leaving

Press `q`. The sheet closes; since it was the only one, VisiData leaves and hands you your terminal back. You changed nothing by visiting — sorting, searching and looking are all in the free-and-safe category from chapter 2. Take that as the chapter's real outcome: **you can open any tabular file you own and look around, and the file will never know you were there.** The chapters that follow add the verbs: arrange it (5), mark the interesting rows (6), count it (7), summarise it (8), and — carefully, on a copy — change it (9).

# Recipes

Small jobs, done whole. Each recipe names its starting point and its check; all of them were run in the lab, on the fixtures in `visidata-lab/`.

## The reorder list

*From the stock file to a file of only what is running out.*

1. Open `seeds.csv`. Stand on packets, press `#` (integers — chapter 5; without this, the sort lies).
2. Press `[`. The three emptiest rows are on top: 0, 5, 9.
3. Press `s` three times. Three bullets, status counting `•3`.
4. Press `"` to lift them into their own sheet.
5. Ctrl+S. **Read the name you are offered.** It is the *source* file's name (transcript t48) — accepting it would aim three rows at the whole catalogue, saved from disaster only by the overwrite question. Clear the field (Ctrl+E to the end, Ctrl+U to erase) and type `reorder.csv`, then Enter. A new file asks no overwrite question.

Check: the file holds the header and exactly the three rows (transcript t49; the shell agrees):

```text
crop,variety,packets,price,sow_month,days_to_harvest
Carrot,Autumn King,0,1.95,May,80
Pepper,California Wonder,5,2.90,February,85
Courgette,Defender,9,2.30,May,50
```

## A column the file doesn't have

*What is the stock on each row worth? The file has packets and prices, but no totals.*

1. Type the ingredients: `#` on packets, `%` on price.
2. Press `=` and give the expression: `packets * price`. Column names are the variables; the expression is ordinary Python.
3. A new column appears beside the cursor with the products (transcript t47): 42 × 2.50 = 105.0 on the first row.

Check it with your eyes before you trust it, and expect honesty of a floating-point kind: 17 × 2.20 shows as `37.400000000000006`. That is not VisiData misbehaving; it is how binary arithmetic writes that sum, and any tool showing you a cleaner number has chosen to tidy it. For money, treat computed decimals as estimates, or work in pennies.

## The census, with totals

*How much stock of each crop, not just how many varieties?*

Attach `sum` to the packets column (stand on it, `+`, type `sum`, Tab, Enter), then open the frequency table on crop with `Shift+F`. The `packets_sum` column answers: tomatoes 59, carrots 58, lettuces 54, and the single pea variety out-stocking them all at 64 (transcript t29). Dive into any bin with Enter when a total looks wrong.

## The two-minute health check

*Someone hands you a file you have never seen.*

1. `Shift+C`: the Columns sheet. Which columns have types? For a CSV, expect none — that is now information, not a surprise.
2. `Shift+I`: the Describe sheet. Scan three things: the **errors** column (values that failed to be what the file claims), the **nulls** (how much is missing), and **distinct** (a column you expected to be all-unique, or all one value, telling you otherwise).
3. Any mean showing `!` names an untyped column of numbers — type it (chapter 5) before computing anything else from it.

Two minutes, and you know more about the file than the person who sent it may.

## The export for someone else

*A program's JSON, as a table a colleague can open.*

```bash
vd -b workshops.json -o workshops.tsv
```

One command, no screen (transcript t44). The check is the same as always: open the output and read it. If the colleague needs numbers as numbers in a JSON output, open the source interactively first and set the types — batch conversion carries the file's types as it finds them (chapter 11).

# Troubleshooting

Every entry here happened — most of them to this guide's lab, in the sessions whose transcripts sit in `visidata-lab/transcripts/`. They are ordered roughly by how early a new user meets them.

## My numbers are sorted in the wrong order

*You see:* a sorted column runs 0, 12, 15, … 47, **5**, 58, 64, 73, **9**.

*What happened:* the column is untyped, so its values are text and the order is word order. With prices written uniformly (`1.20`, `2.90`) the two orders coincide and the problem hides; with mixed lengths it jumps out.

*Fix:* stand on the column and set its type — `#` for integers, `%` for decimals — then sort again. Chapter 5 is this entry, at length. Transcript t11 is the before; t19 is the after.

## Search says there are no matches, but the word is right there

*You see:* `/` and your word, and no jump, no match.

*What happened:* `/` searches the **column you are standing on** (`search-col`, as the status line says), not the whole sheet.

*Fix:* move to the column the word lives in, and search again. Transcript t46 is the search behaving; the lab only ever hit the empty version by standing in the wrong column.

## My pattern select chose nothing at all

*You see:* `selected 0 rows` after pressing `|`, and a follow-up dup sheet that is empty.

*What happened:* `|` matches a regular expression against the **current column's values** — it is not a formula box. The lab typed `packets < 10` while standing on the crop column; no crop is named that, so nothing matched, correctly.

*Fix:* for text patterns, stand on the column the pattern is about (transcript t30: `^Lettuce` on crop, two rows). For numeric conditions, there is no expression filter of that kind in this guide's toolkit — type the column, sort it, and select the rows at the top by hand (chapters 5 and 6). Transcript t07 is the failure; t08 is its empty sheet.

## I selected every other row

*You see:* bullets on rows 1, 3, 5 when you wanted 1, 2, 3.

*What happened:* `s` selects the row **and steps down one**, ready for the next. Adding your own `j` between presses steps twice.

*Fix:* press `s` alone, once per row. Transcript t20 is the skip; t23 is the same job done right. Started wrong? `g` then `u` clears all selections and you begin again.

## My edited cell has two values glued together

*You see:* a price of `2.752.50`, or similar.

*What happened:* the cell editor opens with the cursor at the **start** of the old value, so typing inserts in front of it — and Ctrl+U, the clear-the-line key from other programs, here clears only the text *before* the cursor, which was nothing.

*Fix:* reopen the cell with `e`, press Ctrl+K (clear from the cursor to the end — from the start, everything), type the value, Enter. And always read the cell back afterwards. Transcript t32 is the glue; t33 is the repair.

## I quit and my edit was gone

*You see:* the reopened file, unchanged, although the sheet clearly showed your edit.

*What happened:* edits live in memory until you save (watch for `[M]` in the status line), and `q` on the last sheet leaves without asking. The quitguard that would make it ask exists but is off by default.

*Fix:* Ctrl+S before `q`, whenever `[M]` is showing and the change matters. Consider the `guard-sheet` command for files you edit often. Chapter 9 tells the lab's version of this story in full.

## The save said "disconfirmed" and nothing was written

*You see:* after Ctrl+S and the overwrite box, a status in the corner — `disconfirmed: seeds-edit.csv exists. overwrite?` — and the file on disk unchanged, `[M]` still up.

*What happened:* the overwrite box does not take Enter. It takes a plain **y** or **n** keystroke; anything else counts as *no*.

*Fix:* Ctrl+S again, and press `y` at the box. Then check the statuses corner and read the file back from the shell. Transcripts t36 and t37 are the box and the refusal; t39 is the save landing.

## Saving offered me the wrong filename

*You see:* Ctrl+S on a partial sheet (a dup of selected rows), and the prefilled name is the *original* file's.

*What happened:* the save form prefills the sheet's source name, whatever sheet you are on. Accepting it on a partial sheet would replace the whole file with the part — stopped only by the overwrite question.

*Fix:* read the name every time. Clear it (Ctrl+E, then Ctrl+U) and type the name you mean. Transcript t48 is the offer; the recipe in chapter 12 is the save done right.

## After one small edit, every line of the file "changed"

*You see:* a diff claiming the whole file was rewritten, for a one-cell change.

*What happened:* saving rewrites the file, and VisiData's CSV writer ends lines with carriage return plus newline where the original used newline alone.

*Fix:* none needed for most readers — programs accept both endings. If the file is version-controlled and the noise matters, that is a real consideration in choosing where to edit; chapter 9 shows the byte-level evidence (t40).

## My converted JSON has all its numbers in quotes

*You see:* `"packets": "42"` in the JSON your batch conversion produced.

*What happened:* conversion carries types as it finds them; the CSV's values were untyped text on the way in, so they are strings on the way out.

*Fix:* open the file interactively, set the column types (`#`, `%`), then convert — or say, in writing to whoever receives it, that the numbers are strings on purpose. Chapter 11 is the whole story.

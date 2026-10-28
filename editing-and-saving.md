# Editing and Saving

Everything so far has been looking. This chapter crosses the line into changing — carefully, and on a copy. The lab made the copy first, and so should you:

```bash
cp seeds.csv seeds-edit.csv
vd seeds-edit.csv
```

The job: the Gardener's Delight tomatoes have gone up in price, from 2.50 to 2.75.

## The cell editor, and the tail it grew

Stand on the price cell of the first row and press `e`. The cell opens for editing with its current value in place (transcript `visidata-lab/transcripts/t31-edit-cell-prompt.txt`):

```text
 Tomato    │ Gardener's Delight │ 42      │2.50___  March     │ 70              ║
```

The editor is a small text field with its own keys, and the one to know is where the cursor starts: at the **beginning** of the value. Type now and your text goes *in front*. The lab learned this the way everyone does. Reaching for the familiar Ctrl+U to clear the field did not clear it — in this editor Ctrl+U deletes the text *before* the cursor, and with the cursor at the start there was nothing before it to delete. The lab typed `2.75`, pressed Enter, and read the cell back in horror (transcript t32):

```text
 Tomato    │ Gardener's Delight │ 42      │ 2.752…│ March     │ 70              ║
```

The cell held `2.752.50`: the new price glued to the front of the old one. Nothing warned; the sheet just wore the result. The repair is the editor's other kill key: `Ctrl+K` deletes from the cursor to the **end** of the field, which — cursor at the start — empties it completely. `e`, Ctrl+K, type the new value, Enter (transcript t33):

```text
 Tomato    │ Gardener's Delight │ 42      │ 2.75  │ March     │ 70              ║
```

Two editor keys worth memorising, then: **Ctrl+K clears from the cursor rightward; Ctrl+U clears from the cursor leftward.** Between them they cover every starting position. And the deeper habit, again: read the cell back after editing, the way you would check a total. The status line also shows `[M]` now — the sheet is **modified**, holding a change the file does not have yet.

## The quit that does not ask

Here the lab lost its edit, and the loss is the lesson. Press `q` on a modified sheet and VisiData quits. No prompt, no *are you sure*, no saved-by-accident: the program closes and the edit, which only ever lived in memory, evaporates. The lab reopened the file and found 2.50, unharmed and unimproved.

This is deliberate design, not an oversight: VisiData's position is that quitting means *stop*, and a **quitguard** — an option to demand confirmation before closing a modified sheet — exists but is **off by default**. There is a `guard-sheet` command to switch it on for a sheet you care about. Until you arrange that, treat `[M]` in the status line as the only guard there is: *modified* means *not yet real*, and `q` means *throw it away*. When you want the change, save first.

## Saving: a name, a type, and a question

Ctrl+S saves the sheet. It is not one keystroke but a short conversation. First a form at the bottom of the screen asks where, and as what (transcript t35):

```text
as filetype:
save to: seeds-edit.csv___
```

The name is prefilled with the sheet's own file, and for an ordinary save you press Enter and accept it. (Chapter 12 shows why you should still *read* it: when the lab saved a partial sheet, the prefilled name was the source file's — accepting blindly would have aimed three rows at the whole catalogue. The overwrite question below is the safety net, but reading the name is the safety habit.) Because `seeds-edit.csv` already exists, a confirmation box appears (transcript t36):

```text
seeds-edit.csv exists. overwrite?
        yes                no
```

The box takes a plain letter: press `y` for yes or `n` for no — not Enter. The lab's first attempt fumbled this and pressed keys that answered nothing; the save was refused, and the refusal was recorded in the corner of the screen (transcript t37):

```text
disconfirmed: seeds-edit.csv exists. overwrite?
```

with the file on disk still showing the old price, and `[M]` still standing — the sheet honestly reporting *not saved*. With `y` pressed, the save completed and the `[M]` cleared (transcript t39). A new file gets no such question; the box exists only because a save that replaces a file should have to say so.

## Read it back

Never trust a save you have not read. Back at the shell, the lab checked the file itself:

```text
$ grep Gardener seeds-edit.csv
Tomato,Gardener's Delight,42,2.75,March,70
```

The 2.75 is real. But a full diff against the original held one more surprise (transcript t40): **every line differed**, though only one value had changed. Byte inspection explained it — the original file ends its lines with the Unix newline alone, and VisiData's CSV writer ends them with the Windows pair, carriage return plus newline. Strip the carriage returns away and the diff shrinks to exactly the one price. Most programs accept either ending without comment, so the practical risk is small; but if your files live under version control, a one-cell edit in VisiData will light up the whole file in a diff, and now you know why. Editing in VisiData rewrites the file as a whole — faithfully, in its own dialect.

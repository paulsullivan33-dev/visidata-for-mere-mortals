# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a key, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's files are small, invented and ordinary.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 14 names what the tool
   cannot do: files too big for memory, types it will not
   guess, saves that rewrite in its own dialect, nesting that
   needs unfolding, and the unguarded quit.
8. **The safety rule is in the text, early.** The README and
   chapter 1 state the rule plainly — *looking never writes;
   learn to edit on a copy* — before any procedure depends on
   it, and the editing chapter works on a copy throughout.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox.
VisiData **3.4** was installed with pip into its own fresh
virtual environment (Python 3.12.3) and driven interactively
in a terminal multiplexer against the three fixtures in
`visidata-lab/`: `seeds.csv` (a fourteen-row seed catalogue),
`workshops.json` (six workshops) and `tools.db` (a one-table
SQLite database, rebuildable with `make-tools-db.py`). All
transcripts live in `visidata-lab/transcripts/`; `lab-notes.txt`
there maps each one to what it proves.

Run for real, with transcripts as evidence:

- Install and version: `vd --version` reports
  `saul.pw/VisiData v3.4` (t00).
- Opening the CSV and reading the sheet; `gg` and `Shift+G`
  moving to the first and last rows, named in the status line
  as `go-top` and `go-bottom` (t01, t45); searching the current
  column with `/` and following matches with `n` (t46).
- Sorting: by price, where word order and number order
  coincide (t03); by packets, where they do not — the column
  sorted as text, 5 and 9 stranded after 47 and 73 (t11).
- The Columns sheet showing every type cell empty for the
  CSV (t12); `~` setting a column to text (t13); `#` setting
  packets to integer, with the `packets#` header and
  right-aligned values (t18), and the same sort then running
  in true number order (t19); `%` setting price to float
  (header `price%` in t47).
- Selecting: the lab's own wrong way first — `s j s j s`
  landing on rows 1, 3, 5 (t20, t21) — then `s` alone picking
  the three lowest-stock rows (t23), the dup sheet holding
  exactly those rows (t24), and `gu` clearing a selection
  (t22). Pattern selecting with `|`: the lab's expression
  typed at the wrong column selecting 0 rows (t07) and
  producing an empty dup sheet (t08); `^Lettuce` on the right
  column selecting exactly two (t30).
- Frequency tables: counts and histogram for crop (t04);
  Enter diving from a bin into its two source rows (t05);
  the `+` aggregator chooser (t27) and a frequency table
  carrying a `packets_sum` column (t29). The sums were checked
  by hand against the fixture.
- The Describe sheet (t25): full statistics for the typed
  packets column (sum 422, checked by hand), blanks and the
  error mark `!` for the untyped ones.
- Editing: the `e` cell editor open on a price (t31); the
  lab's mangled `2.752.50`, produced by typing in front of
  the old value after Ctrl+U cleared the wrong side (t32);
  the repair with Ctrl+K (t33); an unsaved edit discarded
  by an unguarded `q`, confirmed by the file itself still
  reading 2.50 when next examined; the save conversation —
  filename form (t35), overwrite box (t36), a refusal
  recorded as `disconfirmed` with the file untouched (t37),
  and the save landing on a plain `y` (t39, with the written
  file grepped for the new price).
- The saved file compared byte-wise: a one-cell edit left
  every line changed, because the CSV writer uses CRLF line
  endings; with carriage returns stripped, the only
  difference is the edited price (t40 and the lab's byte
  check).
- A partial sheet saved under its own name: the save form
  offering the *source* filename for a three-row dup sheet
  (t48), the name replaced, and `reorder.csv` on disk holding
  exactly the header and the three selected rows (t49).
- A computed column: `=` with `packets * price` adding a
  float column, floating-point tails left visible (t47).
- Opening the JSON file, its numbers arriving typed —
  `booked#`, `seats#` — without any type key being pressed
  (t41); opening the SQLite database as an index of its
  tables (t42) and diving into the table, rowid column and
  all (t43).
- Batch mode: CSV converted to JSON, numbers emitted as
  strings because they were untyped on the way in; JSON
  converted to TSV (t44).

Documented only — described from the project's documentation
or the installed program's own command list, not run, and the
text does not claim otherwise:

- Install routes other than pip (distribution packages,
  Homebrew, Windows arrangements).
- The descending sort key `]`, the `guard-sheet` command,
  and the editor's remaining keys, stated from the installed
  program's command definitions; every key the chapters walk
  through step by step was run in a session.
- Loaders beyond CSV, JSON and SQLite (Excel, Parquet, APIs
  and the rest), nested-JSON expansion, read-only sources
  that cannot be saved back, and the graph and plot views,
  which need a screen to look at rather than a transcript to
  keep.
- The comparison tools in chapter 13 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic: a seed
catalogue for an unnamed garden shop, six invented workshops,
and a tool library's shelf. No example is modelled on any real
person, shop, library or organisation, and every number quoted
in the chapters can be re-derived from the fixtures by hand.

# Limits

An honest account of where VisiData stops — some of these the lab ran into directly, and those say so; the rest are stated from the project's documentation and marked as such.

**The file must fit in the room.** VisiData loads what it opens into memory and works on it there. A file of millions of rows on a modest machine will be slow or will not open at all; there is no streaming mode underneath the sheet. The lab's machine (2 CPUs, 7.7 GB) and its fourteen-row fixture never approached this edge, so the number where *your* files become a problem is yours to find — but the streaming neighbours in chapter 13 exist precisely for the country beyond it.

**CSV types are your responsibility.** This is chapter 5, listed here because it is a limit and not only a lesson: nothing in a plain CSV records that a column is numeric, VisiData will not guess, and every computed result downstream inherits the omission. Files whose senders quote everything, mix formats inside a column, or pad numbers with spaces will need cleaning that a type key alone cannot do.

**Saving is a rewrite, in VisiData's dialect.** A save writes the whole sheet out again — chapter 9 watched a one-cell edit change every line's ending from LF to CRLF. Column order, quoting and number formatting may likewise come back in the writer's habits rather than the file's original ones. For a working file that is usually harmless; for a file under version control, or one another program parses strictly, read the result before you rely on it. And some formats are one-way: VisiData reads more formats than it writes, and a sheet from a read-only source (an API response, a database view) may have nowhere to be saved *to* except another format — described from the documentation; the lab's three formats all saved or converted without meeting the wall.

**Editing is cell-by-cell, and formulas do not live in the file.** There is no cell that *contains* `=A2*B2` waiting to recalculate tomorrow. Chapter 12's expression columns are computed by VisiData, in the sheet, while you watch; they are a way of *seeing* a derived value, not of teaching the file to derive it. A spreadsheet's living formulas are a different tool's whole purpose (chapter 13).

**Nested data needs unfolding.** Flat files are the home ground. JSON with objects inside objects arrives as values that must be expanded and unfurled step by step before they are columns — possible, and a skill of its own, but the tidy arrival in chapter 10 was a flat file's arrival, chosen honestly for the purpose.

**It will let you quit and lose work.** Stated in chapter 9 and repeated here because it is the limit most likely to bite a new user once: unsaved changes live only in memory, the quit guard is off by default, and `q` does not ask. The counterweight is real — exploration can never damage a file by accident — but the pair of facts must be learned together.

**One pair of eyes at a time.** A sheet is a personal view; there is no shared editing, no comments, no record of who changed what beyond what you keep yourself. Data that several people maintain belongs in the database or the shared spreadsheet, and VisiData is the visitor you send to look at it.

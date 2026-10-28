# Installing VisiData

VisiData is a Python program, and the honest way to install it is the Python way: into a **virtual environment** — a private folder of Python packages that belongs to this tool alone and cannot quarrel with anything else on the machine. That is how the lab installed it, and how this chapter does it.

You need Python 3 already present. Then:

```bash
python3 -m venv ~/vd-venv
~/vd-venv/bin/pip install visidata
```

The install pulls in VisiData and the small set of libraries it stands on. What lands is a single command, `vd`, inside the environment's `bin` folder. Run it by its full path, or put that folder on your path, or — the arrangement the lab used for its sessions — call it through the environment each time:

```bash
~/vd-venv/bin/vd --version
```

Check: the version answers with the program's home and version, as in the lab's transcript `visidata-lab/transcripts/t00-install.txt`:

```text
$ vd --version
saul.pw/VisiData v3.4
$ pip show visidata | head -3
Name: visidata
Version: 3.4
Summary: terminal interface for exploring and arranging tabular data
```

Every screen in this guide is that version, 3.4. VisiData moves quickly and its keys occasionally move with it; if your version differs and a key in this guide behaves differently, the status line (chapter 2) will tell you the name of what your key actually did, and the built-in help under that name is the authority.

Three practical notes from the install:

- **The terminal matters a little.** VisiData draws its screen with the terminal's own characters — box corners, bullets, bars. A modern terminal handles all of it. If your screen shows stray letters where lines should be, the fix is almost always the terminal's character encoding (it wants UTF-8), not VisiData.
- **The window wants room.** The sheets in this guide were captured in a window 132 columns wide. A narrow window still works — columns scroll sideways — but a wide one makes the first hours pleasanter.
- **No file is touched by installing or opening.** Installation writes only into the environment folder. Opening a file reads it into memory. The first moment in this guide where a disk changes is the deliberate save in chapter 9, and it announces itself.

Other routes exist — most Linux distributions package VisiData, as do Homebrew on a Mac and the usual Windows arrangements — and they are listed in the project's documentation. They are described here, not demonstrated: the lab used the pip route above, and it is the one whose steps this chapter can stand behind. Whichever route you take, `vd --version` is the check that you and this guide are looking at the same tool.

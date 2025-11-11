

# Onyx Notes

A terminal-based Note-taking app for managing Markdown files. built with Python and Textual.

## Features

- **Multiple Vaults**: create , delete, and manage multiple vaults.
- **Search Vaults**: quickly search and select vault on startup.
- **Keyboard Driven**: Efficient navigation throughout the app.
- **Multi-panel interface**: edit , preview, and show stats of a note simltaneously.
- **Modular panel mangement**: open , close, and orginize UI panels needed using keyboard shortcuts.
- **Nested folders**: Orginize note in hierarchial directory.
- **Note statistics**: word count, line count, and metadata tracking.

## Installation

### Prerequisites

- Python 3.12 or higher (lower version might work)
- pip
### Option 1: Portable (Recommended for Users)

1. Download the latest release: 
    - [onyx-notes-v0.1.0-portable.zip]()

2. Extract the archive to your preferred location:

    ```
    unzip onyx-notes-v0.1.0-portable.zip -d onyx-notes
    cd onyx-notes
    ```
3. Navigate to the extracted folder and run:
    ```
    ./start.sh   # Linux/Mac
    start.bat    # Windows
    ```

### Option 2: From Source (For Developers)

1. Clone the repository:

```bash
git clone https://github.com/o0n1x/onyx-notes.git
cd onyx-notes
```

2. Create virtual enviroment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python -m src.tui
```

## Usage

As a TUI, it can be used with a mouse, but it can be used completely using keyboard shortcuts. below will list all the shortcuts for each page.

### Vault Selection

On first launch, you'll see the vault selection screen.
<!-- Add Image of Vault -->

- **Ctrl+N** : Create a new vault
- **Ctrl+O**/**Enter** : Open selected/first vault
- **Ctrl+D** : Delete selected/first vault with confirmation
- **Ctrl+R** : refresh vault list
- **Ctrl+Q** : Quit application
- **Type to search** : Filter vaults by name



### Note Editing

After selecting a vault, this page will open.

<!-- Add Image of Note Editor -->

- **Ctrl+N** : Create a new note
    - Enter a path like `folder/note.md` to create note with folder(s) if needed
    - End with / like `new_folder/sub_folder/`to create empty folder(s)
- **Ctrl+S** :Save current note
- **Ctrl+D** : Delete current note
- **Ctrl+B** : Toggle directory tree visibility
- **Ctrl+Q** : Return to vault Selection
- **↑/↓** : Navigate directory tree (if editor is not focused)
- **Enter**: Open selected note (if editor is not focused)

### Panel Managment

Panels can be shown/hidden independently to customize your workspace.

- **F1** : Toggle Editor Panel
- **F2** : Toggle Viewer Panel
- **F1** : Toggle Statistics Panel


<!-- Add Video showcasing this -->

## File Structure

```
onyx-tui/
├──src
│   ├── __init__.py  # Package init
│   ├── tui.py       # Main TUI application     
│   ├── note.py      # Note data model           
│   ├── vault.py     # Vault management         
│   ├── note_io.py   # File I/O operations
│   ├── graph.py     # planned feature        
│   ├── style.tcss   # Textual CSS styling     
├── requirements.txt # Dependancies  
└── README.md        # Documentation
```

## Note Format

Notes are stored as markdown files with YAML forntmatter similar to Obsidian.

Example:

```markdown
---
title: My Note
tags: [example, demo]
created: 2025-01-15 10:30:00
last_modified: 2025-01-15 14:20:00
---

# My Note

Note content goes here...
```

## Configurations

Vaults are stored in `~/.config/ onyx-notes/vaults.txt`
Each vault entry contains
- Display Name
- Path

## Roadmap

- [ ] Graph Page
    - [ ] wiki-style links between notes
    - [ ] Custom interactive graph widget

- [ ] add custom tags to notes 
- [ ] ability to add custom metadata
 

## Acknowledgments

Version: 0.1.0
Author: o0n1x - Abdullah Alamoudi
Status: Beta

### Additional Files to Include:

**requirements.txt:**
```
 frontmatter>=3.0.8
 textual[syntax]>=6.5.0
```
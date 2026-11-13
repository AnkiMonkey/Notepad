**Notepad by AnkiMonkey – settings**

Easiest: the ⚙ Settings button in the panel (`Alt+S`) – every option is explained there.

| Key | What it does |
|---|---|
| `dock_area` | `right` / `left` – panel side (restart) |
| `dock_width`, `min_width`, `width_step`, `remember_width` | panel width in px, narrowest width, step of Narrower / Wider, keep width after restart |
| `collapsed` | panel collapsed to a thin strip |
| `font_size`, `font_family` | font of your notes |
| `show_logo`, `logo_height` | AnkiMonkey logo (restart) |
| `mode` | `text` = free scratchpad, `table` = Base / Notes table |
| `clear_after_answer` | table: Notes column emptied, Base kept; text: emptied |
| `auto_focus` | cursor jumps into the panel when a question is shown (Space then types into the panel) |
| `hide_outside_review` | hide the panel outside review |
| `remember_zoom` | keep the card zoom (Ctrl + / Ctrl −) after restarting Anki |
| `template_dir` | folder with TXT templates; empty = `user_files/templates` inside the add-on |
| `auto_load_template`, `default_template` | load a template for every card; file used when nothing matches |
| `tag_rules` | e.g. `[{"tag": "Pharma", "file": "pharma.txt"}]`; first match from the top wins |
| `rules_first_tag_only` | rules look only at the note's first tag |
| `table_separator`, `table_headers` | separator in the TXT (default tab), names of the 2 columns |
| `table_template_readonly` | template column cannot be edited |
| `table_empty_rows`, `table_numbered`, `table_ask_rows` | rows without a template, numbering 1, 2, 3 …, "Rows?" box on every card without a template |
| `shortcut_*` | keyboard shortcuts; changes apply after restart |

**Template matching** (first found wins): tag rules → tags (most specific first, `A::B` → `A__B.txt`, then `A.txt`) → deck (same way) → `default.txt`.

**TXT for the table:** one line = one row. Text before the tab goes to column 1, after it (optional) to column 2.

Changes in this JSON apply after an Anki restart.

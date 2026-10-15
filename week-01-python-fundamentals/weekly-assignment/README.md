# Week 1 — Python Fundamentals

This assignment includes 20 beginner Python exercises in `basics.ipynb` and a script that analyzes 30 sample messages from `messages.csv`.

## Requirements

Python 3.8 or newer. No external packages are required for the script or tests. Open `basics.ipynb` in Jupyter or another notebook editor with a Python 3 kernel.

## Run the script

From the repository root:

```sh
cd week-01-python-fundamentals/weekly-assignment
python message_stats.py
```

The script reads the CSV beside it and writes `summary.json` in the same folder. The sample data produces:

```text
Total messages: 30
Average message length: 34.27
Longest message: The application keeps crashing whenever I try to open my account settings
Summary saved to summary.json
```

## Run the five tests

From the weekly-assignment folder:

```sh
python -m unittest discover -s tests -v
```

Tests use temporary files and leave the original `messages.csv` unchanged.

## File handling

- Missing CSV files raise `FileNotFoundError`.
- Empty files and files containing only the header raise `ValueError`.
- Empty message text counts as a message with zero characters.
- Malformed CSV files raise `ValueError`. The header must be `message_id,text`, every row must have two fields, and CSV quoting must be valid.

Message length includes spaces and punctuation. The average is rounded to two decimal places. If messages tie for longest, the first one is returned.

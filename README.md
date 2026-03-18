# Password Strength Analyzer

A Python CLI tool that analyzes the strength of a password and gives improvement suggestions.

## Features

- Scores passwords from 0–100 based on length and character variety
- Calculates entropy to measure how hard a password is to crack
- Checks against a list of commonly breached passwords
- Gives top 3 suggestions for improving weak passwords
- Keeps a history of the last 5 passwords checked

## DSA Concepts Used

- **HashSet (Set)** — enables constant-time O(1) lookup for breached passwords
- **Lists / Arrays** — used for character classification and counting
- **Queue-like List** — maintains fixed-size history with FIFO removal
- **Iteration & Conditional Logic** — used for scoring and validation


## How to Run

Make sure you have Python 3 installed, then run:

```bash
python3 password_analyzer.py
```

## Usage

```
=== Password Strength Analyzer ===

1. Check a password
2. View history
3. Quit
```

## Example Output

```
Score: 100/100 - Strong
Entropy: 91.76 bits (very hard to crack)
Length: 14 | Upper: 2 | Lower: 6 | Digits: 4 | Special: 2
Great password! No suggestions.
```

## Requirements

- Python 3.x
- No external libraries needed

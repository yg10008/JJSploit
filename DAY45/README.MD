
# Day 45 – Python Practice Task (Game + Outlier Detection)

This directory contains two Python mini-projects designed to enhance Python fluency and real-world logic building through basic game development and data preprocessing.

---

## 🎲 TASK 1 – Mystery Card Game

This is a fun, interactive CLI game that simulates picking a card from a shuffled deck. It uses random number logic and simple game rules to give users a lucky draw experience.

### 🔍 Features:
- Uses `numpy.random.permutation()` to shuffle cards
- User is asked to guess a number (0–9) and select a card position (1–10)
- Game responds with win/loss based on the match
- Adds suspense using `time.sleep()` to simulate a shuffling effect

### 🧠 Concepts Applied:
- `numpy` for randomization
- `input()` and indexing
- Simple conditional logic (`if/else`)
- `time.sleep()` for simulated delays

### ▶️ How to Run:
```bash
python mystery_card_game.py
```

---

## 📊 TASK 2 – Outlier Detection on Titanic Dataset

This script demonstrates how to detect and handle outliers in real-world tabular datasets like the Titanic dataset. It applies statistical rules like the IQR method and provides multiple strategies to address detected outliers.

### 🔍 Features:
- Loads `titanic.csv` from local path
- Uses IQR method to identify outliers
- Functions include:
  - `check_outliers()`
  - `grab_outliers()`
  - `remove_outliers()`
  - `replace_with_thresholds()`

### 📦 Packages Used:
- `numpy`, `pandas`, `matplotlib`, `seaborn`, `missingno`
- `sklearn.preprocessing`, `sklearn.model_selection`, `sklearn.neighbors`

### 📌 File-Based Functions:
- `outlier_thresholds()`: Returns lower and upper bounds for a feature
- `check_outliers()`: Checks for presence of outliers
- `grab_outliers()`: Prints or returns index of outliers
- `remove_outliers()`: Drops outliers from dataset
- `replace_with_thresholds()`: Caps outlier values at limits

### ▶️ How to Run:
Ensure your dataset paths are correct in the script, then run:
```bash
python outlier_detection.py
```

> Example output includes IQR values, outlier existence confirmation, and outlier indices.

---

## 📁 File Structure

```
DAY45/
├── mystery_card_game.py             # TASK 1: Card guessing game
├── outlier_detection.py            # TASK 2: Titanic data outlier analysis
```

---

## ✅ Learning Outcome

- Applied probability, indexing, and randomness via game logic
- Understood how to identify and handle outliers using IQR and other preprocessing techniques
- Practiced modular Python design and clear function separation

